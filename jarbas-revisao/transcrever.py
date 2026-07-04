#!/usr/bin/env python
"""
Transcreve áudio/vídeo para .txt (PT-BR) — local, grátis e privado (faster-whisper).
Versão do jarbas-revisao: aceita --prompt (vocabulário do projeto vira initial_prompt
do Whisper — corrige nomes próprios NA FONTE, ex.: "Âmbar", "casei", "scrapbook").
Origem: casei/docs/jarbas/ux/transcricao/transcrever.py (lá tem também --diarizar).

Uso:
    python transcrever.py <arquivo> [--modelo small] [--idioma pt] [--prompt "Âmbar, casei, ..."]

Saída: <mesmo nome>.txt (linhas com timestamp)
"""
import argparse
import datetime
import sys
from pathlib import Path


def fmt(t: float) -> str:
    return str(datetime.timedelta(seconds=int(t)))


def main() -> None:
    try:  # console Windows (cp1252) quebra em emoji/acentos; força utf-8
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Transcrição local (faster-whisper).")
    ap.add_argument("arquivo", help="caminho do áudio/vídeo (.flac, .wav, .mp4, .m4a…)")
    ap.add_argument("--modelo", default="small",
                    help="tiny/base/small/medium/large-v3 — maior = melhor e mais lento (padrão: small)")
    ap.add_argument("--idioma", default="pt", help="código do idioma (padrão: pt)")
    ap.add_argument("--prompt", default=None,
                    help="vocabulário/contexto para guiar a decodificação (nomes próprios do projeto)")
    args = ap.parse_args()

    src = Path(args.arquivo)
    if not src.exists():
        sys.exit(f"arquivo não encontrado: {src}")

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("faster-whisper não instalado. Rode: pip install faster-whisper")

    print(f"[1/2] carregando modelo '{args.modelo}' (CPU, int8)...", flush=True)
    model = WhisperModel(args.modelo, device="cpu", compute_type="int8")

    print(f"[2/2] transcrevendo {src.name}...", flush=True)
    segments, info = model.transcribe(str(src), language=args.idioma,
                                      vad_filter=True, initial_prompt=args.prompt)
    dur = getattr(info, "duration", None)

    # Escrita incremental: se o processo morrer no meio, o parcial sobrevive.
    out = src.with_suffix(".txt")
    n = 0
    with out.open("w", encoding="utf-8") as f:
        for seg in segments:
            f.write(f"[{fmt(seg.start)}] {seg.text.strip()}\n")
            n += 1
            if n % 25 == 0:
                f.flush()
                pct = f" (~{seg.end / dur * 100:.0f}%)" if dur else ""
                print(f"[progresso] {fmt(seg.end)}{pct}", flush=True)
    print(f"OK - salvo: {out}  ({n} segmentos)", flush=True)


if __name__ == "__main__":
    main()
