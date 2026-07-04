#!/usr/bin/env python
"""
Gravador do jarbas-revisao — grava o microfone padrão até aparecer o arquivo-sinal
de parada (ou até o teto de segurança). Local e privado.

Uso:
    python gravar.py <saida.flac> <stop_flag> [--max-horas 3]

Comportamento:
- Grava mono 16 kHz (ideal p/ Whisper) em FLAC (~metade do tamanho de WAV).
- Padrão canônico do sounddevice: o callback de áudio SÓ enfileira; escrita e flush
  acontecem na thread principal (evita corromper o FLAC e input overflow).
- Para quando <stop_flag> passar a existir; escreve <saida>.done ao fechar.
- Flush periódico: mesmo que o processo morra (ex.: Modern Standby), o áudio até ali sobrevive.
- Marcadores no stdout: "[pid] N" no início; "[gravando] dispositivo: ..." SÓ depois
  de o stream abrir de verdade (é o health-check do skill); progresso a cada 30 s.
"""
import argparse
import os
import queue
import sys
import time
from pathlib import Path


def main() -> None:
    try:  # console Windows (cp1252) quebra em acentos; força utf-8
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Gravação de microfone até sinal de parada.")
    ap.add_argument("saida", help="arquivo de saída (.flac)")
    ap.add_argument("stop_flag", help="caminho do arquivo-sinal: quando existir, para")
    ap.add_argument("--max-horas", type=float, default=3.0,
                    help="teto de segurança se esquecerem a gravação ligada (padrão: 3h)")
    args = ap.parse_args()

    print(f"[pid] {os.getpid()}", flush=True)

    try:
        import sounddevice as sd
        import soundfile as sf
    except ImportError:
        sys.exit("faltam dependências: pip install sounddevice soundfile")

    out = Path(args.saida)
    stop = Path(args.stop_flag)
    done = Path(str(out) + ".done")
    out.parent.mkdir(parents=True, exist_ok=True)
    stop.parent.mkdir(parents=True, exist_ok=True)
    # Limpeza de execuções anteriores: flag/done/áudio velhos não podem contaminar esta.
    for velho in (stop, done, out):
        if velho.exists():
            velho.unlink()

    q: "queue.Queue" = queue.Queue()

    def cb(indata, frames, t, status):
        if status:
            print(f"[aviso] {status}", flush=True)
        q.put(indata.copy())  # NUNCA I/O de disco aqui (thread de áudio)

    sr = 16000
    t0 = time.time()
    try:
        dev = sd.query_devices(kind="input")
        with sf.SoundFile(str(out), mode="w", samplerate=sr, channels=1,
                          format="FLAC", subtype="PCM_16") as f, \
             sd.InputStream(samplerate=sr, channels=1, dtype="int16", callback=cb):
            # Marcador de sucesso SÓ com o stream aberto — health-check do skill.
            print(f"[gravando] dispositivo: {dev['name']} -> {out.name}", flush=True)
            ultimo_flush = 0.0
            while not stop.exists():
                try:
                    f.write(q.get(timeout=0.3))
                except queue.Empty:
                    pass
                s = time.time() - t0
                if s - ultimo_flush >= 30:
                    ultimo_flush = s
                    f.flush()  # sobrevive a morte do processo
                    print(f"[gravando] {int(s) // 60}m{int(s) % 60:02d}s...", flush=True)
                if s > args.max_horas * 3600:
                    print("[teto] duração máxima atingida - parando.", flush=True)
                    break
            while True:  # drena o resto da fila antes de fechar
                try:
                    f.write(q.get_nowait())
                except queue.Empty:
                    break
    except Exception as e:
        sys.exit(f"falha na gravação: {e}")

    if stop.exists():
        stop.unlink()
    done.write_text("ok", encoding="utf-8")
    dur = int(time.time() - t0)
    print(f"OK - gravado {dur // 60}m{dur % 60:02d}s: {out}", flush=True)


if __name__ == "__main__":
    main()
