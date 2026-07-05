---
name: jarbas-feedback
description: Ative com /jarbas-feedback (toggle gravar→parar), /jarbas-feedback <arquivo(s)> para gravações prontas, ou quando Oscar disser "feedback de usuário", "analisar teste com usuário real", "sessão de feedback". Irmão LEVE do /jarbas-revisao para gravações de USUÁRIOS REAIS usando o app - transcreve local (Whisper $0), normaliza + ANONIMIZA, e organiza os pontos POR PÁGINA/SEÇÃO/SUBSEÇÃO do app — 👍 elogios · 👎 reclamações · 💡 sugestões — ligando de leve aos artefatos de UX e dando UMA sugestão de execução por ponto; Oscar seleciona por código (F-NN-k) o que executar. Tudo entra no ACUMULADO estruturado que revela temas recorrentes (🔥 quando ≥2 feedbacks citam o mesmo ponto). Argumentos - caminhos de arquivo/pasta (fluxo ARQUIVOS), status, cancelar.
---

# Jarbas — feedback de usuários reais (triagem por área do app)

Irmão do `/jarbas-revisao`, para quando quem fala é um **usuário real** (não Oscar revisando a
própria interface). O objetivo NÃO é o comitê profundo — é **organizar o que o usuário disse por
área do app**, com leitura de UX curta e uma sugestão por ponto, e **acumular estruturadamente**
para enxergar temas recorrentes entre feedbacks.

Carregar antes: `_jarbas/persona.md` e `_jarbas/projetos.md` (§ *Feedbacks de usuários*).

## revisao × feedback — quando usar qual

| | `/jarbas-revisao` | `/jarbas-feedback` |
|---|---|---|
| Quem fala | Oscar (± convidado) revisando | usuário real usando o app |
| Profundidade | comitê UX+Eng, trade-offs, esforço/custo | triagem leve, 1 sugestão por ponto |
| Saída | proposta R1..Rn para executar já | mapa por página/seção + ACUMULADO de temas |
| Sensibilidade | conteúdo interno | dado de terceiro → **LGPD** (ver Convenções) |

## Motor compartilhado (não duplicar código)

A captura usa o **MOTOR** do jarbas-revisao — scripts e venv de `..\jarbas-revisao\`
(`gravar.py`, `transcrever.py`, `.venv\Scripts\python.exe`). O **ESTADO é local** deste skill:
`RAIZ\state\` e `RAIZ\gravacoes\` (RAIZ = `~\.claude\skills\jarbas-feedback\`). Locks separados:
dá para gravar um feedback com uma revisão ativa em outra janela, sem colisão.

## Captura (gravar · arquivos · parar · recuperar)

Seguir o protocolo do `..\jarbas-revisao\SKILL.md` **§§0–2b** com DUAS substituições:
1. **RAIZ** (lock `state\gravacao.json`, sinal `state\PARAR`, `gravacoes\`) = a pasta DESTE skill;
2. **Scripts e python** = os do MOTOR (`..\jarbas-revisao\...`).

O resto é idêntico: lock atômico ANTES de gravar, nome com segundos, health-check
`[pid]` + `[gravando]` pós-abertura do stream, fluxo **ARQUIVOS** para mídia/transcrição pronta
(o caso mais comum aqui: Meet, celular), **RECUPERAR** para gravação morta/lock órfão.
Vocabulário do Whisper: o **glossário do projeto** (mesmo das revisões, via `projetos.md`).

## Normalizar + ANONIMIZAR

Como no revisao §3 (glossário, falantes, telas, timestamps), **mais**:
- o usuário vira **F-NN** + perfil curto (ex.: "noiva, E2, interior de SP") — **nome completo
  nunca** entra nos `.md` versionados;
- a transcrição normalizada é salva como `transcricao.txt` na pasta do feedback e **fica fora do
  git** (regra LGPD, como as entrevistas; só os `.md` anonimizados versionam — conferir gitignore).

## Análise (sessão principal — SEM comitê; leve de propósito)

1. Carregar os artefatos de UX do projeto (personas, requisitos — via `projetos.md`) e o mapa de
   páginas do app (o protótipo/código).
2. Para cada ponto do usuário:
   - **Onde:** página → seção → subseção (ex.: Perfil → Data → seletor de meses);
   - **Tipo:** 👍 elogio · 👎 reclamação · 💡 sugestão;
   - **Leitura UX em meia-linha:** conceito + requisito relacionado (IDs do projeto) — sem aprofundar;
   - **Sugestão de execução em UMA linha** (o que fazer se Oscar aprovar).
3. **Não** escalar para trade-off/esforço/alternativas — isso é papel do `/jarbas-revisao` ou da
   execução. Aqui é triagem de fácil leitura.

## Relatório (`feedback.md`)

Salvar em `<pasta_feedbacks>\<AAAA-MM-DD>_feedback-NN\feedback.md` (NN = próximo número livre):

```markdown
# F-NN · <perfil curto anonimizado> — <data>
> Contexto: como testou (guiado/livre), duração, telas percorridas.

## 📄 <Página>
### <Seção → subseção>
- 👍 "citação curta" [ts]
- 👎 "citação curta" [ts] — <conceito UX; reqID>
  → **F-NN-3:** <sugestão de 1 linha>
- 💡 "citação curta" [ts]
  → **F-NN-4:** <sugestão de 1 linha>
```

- Cada sugestão ganha código **F-NN-k** (sequencial no feedback) — é o que Oscar usa p/ selecionar.
- Apresentar no chat de forma limpa e terminar SEMPRE com:
  **"Selecione os códigos que quer executar (ex.: F-03-2, F-03-5), 'todos', ou 'nenhum por ora'."**

## Acumulado (a memória entre feedbacks)

`<pasta_feedbacks>\acumulado.md` — atualizar **a cada feedback, antes de apresentar o relatório**:

- Estrutura por página/seção; cada linha = um **ponto agregado**:
  `| ponto | tipo | fontes | status |` → ex.: `| seletor de data confunde mês×ano | 👎 | F-01, F-03 | backlog |`
- **Dedupe semântico:** antes de criar linha nova, procurar ponto equivalente já registrado e só
  somar a fonte (senão a recorrência nunca aparece).
- **≥2 fontes = 🔥 recorrente** → refletir na seção **"🔥 Temas recorrentes"** no topo do arquivo.
- Status: `novo · selecionado · executado · backlog · ignorado`.
- **Elogios também acumulam** — o que NÃO mexer é informação de produto (e recorrência de elogio
  = ponto forte a proteger).
- Manter também o **índice de feedbacks** (código, data, perfil anonimizado, origem da gravação).

## Execução

1. Oscar seleciona códigos → executar as mudanças (commit só se pedir). Se ele pedir triagem
   por complexidade, usar o modelo do `/jarbas-revisao` §5: lote **LEVE** aprovável em bloco
   (cosmético/só-texto/fix pontual) + **ESTRUTURAIS** ordenados por criticidade 🔴🟠🟡🔵.
2. Mudança de interface que merece o ciclo completo (trade-off, alternativa, custo) → mandar pro
   backlog do `/jarbas-revisao` e anotar isso no acumulado.
3. Atualizar o `status` dos pontos no acumulado (`selecionado` → `executado`).

## Convenções

- Pasta de feedbacks do projeto: `projetos.md` § *Feedbacks de usuários*. Se o projeto não tiver a
  seção, perguntar UMA vez e criá-la (nunca inventar caminho).
- **LGPD/sensível:** áudio/vídeo e transcrições `.txt` de usuários reais **nunca** entram em repo
  (o gitignore da pasta do projeto cobre — conferir antes de qualquer commit). Só os `.md`
  anonimizados versionam. Gravações locais ficam em `RAIZ\gravacoes\` (fora de repo).
- Repo jarbas: este skill entra pela whitelist; `state/` e `gravacoes/` ficam fora pelo
  `.gitignore` local da pasta.
- Fim de sessão: rodar `_jarbas/retro.md`.
