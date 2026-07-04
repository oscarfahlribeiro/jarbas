# Projetos — onde mora a memória de cada projeto

Registro único de caminhos. Os perfis alcançam dados de projeto **só** por aqui — assim o
caminho fica em um lugar só (se mudar, muda uma linha). **Nenhum perfil deve cravar um
caminho de projeto no próprio corpo.**

| Projeto | Artefatos do Jarbas (planos, pesquisas, aprendizados, ux, negócio) | Repo de código |
|---|---|---|
| **casei** | `C:\Users\Oscar\projects\casei\docs\jarbas\` (jarbas-eng/ux) · `C:\Users\Oscar\projects\casei\docs\negocio\` (jarbas-business) | `C:\Users\Oscar\projects\casei` (git, privado, GitHub) |

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

## O que tem em `casei\docs\negocio\` (fonte do jarbas-business)

Material de negócio que o `jarbas-business` lê **antes de opinar** (e onde grava os artefatos novos):

- `Casei_Plano_Negocio_Completo.md` — plano de negócio: problema/solução, monetização, cenários/receita, captação (pré-seed→série B, cap table), tese
- `plataformas-casamento-monetizacao.md` — análise de concorrência por modelo de receita + lições de modelo de negócio
- `comparacao-funcionalidades-fornecedores.md` — análise competitiva por funcionalidade + matriz comparativa
- `Casei_Plano_Jornadas.md` — jornadas/serviços (produto; alimenta posicionamento)

## Revisões de interface (jarbas-revisao)

Onde o ciclo de revisão falada guarda a APLICAÇÃO (transcrições, análises, propostas, backlog)
e como relançar a interface de cada projeto:

| Projeto | Pasta de revisões (inclui `glossario.md` e `backlog.md`) | Relançar a interface |
|---|---|---|
| **casei** (protótipo no DS novo) | `C:\Users\Oscar\projects\casei\docs\design\revisao frontend\` | `docs\design\prototipo\abrir.bat` (http.server 8123); server estático já serve arquivos editados → em geral basta recarregar o navegador |

Insumos que o comitê lê no casei — **UX:** `docs\jarbas\ux\requisitos_jornada.md` ·
`personas.md` · `comparativo_entrevistas.md` · `identidade_visual.md` · `requisitos_x_app.md`;
**Código da interface:** `docs\design\prototipo\` (des-bundle do DS + `perfil.js`).

## Notas da máquina (Oscar)

- Python de bootstrap para venvs (o `python`/`py` global é stub da Windows Store):
  `C:\Users\Oscar\projects\casei\.venv\Scripts\python.exe`

## As próprias skills do Jarbas

Versionadas no repo do Jarbas (`git init` em `~/.claude/skills`, espelho privado no GitHub para
compartilhar com o sócio). Ver o `README.md` dessa pasta.
