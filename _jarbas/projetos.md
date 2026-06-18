# Projetos — onde mora a memória de cada projeto

Registro único de caminhos. Os perfis alcançam dados de projeto **só** por aqui — assim o
caminho fica em um lugar só (se mudar, muda uma linha). **Nenhum perfil deve cravar um
caminho de projeto no próprio corpo.**

| Projeto | Artefatos do Jarbas (planos, pesquisas, aprendizados, ux) | Repo de código |
|---|---|---|
| **casei** | `C:\Users\Oscar\projects\casei\docs\jarbas\` | `C:\Users\Oscar\projects\casei` (git, privado, GitHub) |

## Por que os artefatos do casei vivem DENTRO do repo

Decisão do Oscar (2026-06-18): os artefatos do casei moram no **repo do casei** (em
`docs/jarbas/`) para serem **versionados e compartilhados com o sócio** via git. O
`jarbas-eng`/`jarbas-ux` os lê **sob demanda** por este caminho absoluto — funciona mesmo
rodando da home (é um Read direto, não depende da recall automática da memória do harness).
Oscar commita e dá push quando quiser; o sócio puxa.

## O que tem em `casei\docs\jarbas\`

- `plano_estudos.md`, `plano_evolucao.md`, `plano_mvp_full.md` — planos
- `pesquisas.md` — pesquisas externas filtradas pro casei
- `aprendizados_casei.md` — logs de sessão do casei
- `ux\` — artefatos de UX do casei (`referencias.md`, `conceitos.md`, e futuras personas/jornadas)

## As próprias skills do Jarbas

Versionadas no repo do Jarbas (`git init` em `~/.claude/skills`, espelho privado no GitHub para
compartilhar com o sócio). Ver o `README.md` dessa pasta.
