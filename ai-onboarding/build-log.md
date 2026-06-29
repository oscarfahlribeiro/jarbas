# build-log.md — Registro cronológico do que construímos

> Uma entrada por sessão de construção. O blueprint estruturado está em `architecture.md`.

## 2026-06-29 — Kickoff / andaime do projeto
- Criada a estrutura do AI Onboarding em `ai-onboarding/` (isolada do sistema Jarbas).
- `.gitignore` ajustado pra rastrear `ai-onboarding/` e `.claude/`.
- Criados os 7 slash commands em `.claude/commands/` (`/osmar`, `/teacher`, `/builder`,
  `/status`, `/plan`, `/sync`, `/wrap`).
- Seedados: `CLAUDE.md`, `user-profile.md`, `learning-plan.md` (rascunho), `progress.md`,
  `architecture.md` (stub), `knowledge-base/glossary.md` + `_TEMPLATE.md`, ADR `0001`.
- _Nenhum artefato técnico construído ainda — o primeiro virá no primeiro `/builder` (setup do
  assistente de IA)._
