# 0001 — Estrutura e local do projeto AI Onboarding

## Contexto
O prompt de kickoff pedia `git init`, criar `.gitignore` e perguntar a URL do repo. Mas o ambiente
já é um repo configurado (`oscarfahlribeiro/jarbas`) que hospeda o sistema de mentores "Jarbas".
Dois problemas surgiram:
1. O `.gitignore` existente ignora **tudo** na raiz exceto `_jarbas/` e `jarbas-*/` — então
   arquivos do Osbar criados na raiz **nunca seriam commitados/sincronizados**, quebrando a
   promessa de retomabilidade.
2. O README do repo diz explicitamente que artefatos específicos de projeto **não** moram aqui.

## Opções consideradas
- **A. Subpasta `ai-onboarding/`** (+ ajustar `.gitignore` pra rastreá-la e `.claude/commands/`).
  Prós: isola do sistema Jarbas; versionado e sincronizável; não polui o repo agnóstico.
  Contras: os slash commands precisam morar em `.claude/commands/` na raiz (exigência do Claude Code).
- **B. Na raiz do repo** (prompt ao pé da letra). Prós: literal. Contras: exige reescrever o
  `.gitignore` protetor; mistura Osmar com o sistema Jarbas.
- **C. Repo novo dedicado.** Prós: mais limpo. Contras: outro repo pra gerir; fora do escopo da sessão.

## Decisão
**Opção A.** Projeto em `ai-onboarding/`; `.gitignore` ajustado com `!/ai-onboarding/` e
`!/.claude/`. Slash commands em `.claude/commands/` (única opção pra o Claude Code achá-los).
Decisão do aprendiz em 2026-06-29.

Adicionalmente: **persona = a do prompt** (profissional de Private Banking no Brasil, começando do
zero), independente do perfil "Oscar" já existente no sistema Jarbas.

## Consequências
- O Osmar vive isolado; o sistema Jarbas (`_jarbas/`, `jarbas-*/`) não é tocado.
- Todo estado do Osmar é versionado e sincronizável → retomável em qualquer dispositivo.
- Os comandos na raiz `.claude/commands/` são aditivos e claramente namespeados ao Osmar.
