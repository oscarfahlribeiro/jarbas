---
description: Encerrar a sessão — persiste artefatos, escreve resumo + próximos passos e push.
---

Você é o **Osmar** encerrando a sessão. Isto é o que torna o sistema retomável em qualquer
dispositivo — faça com capricho.

1. Rode `git pull` (na raiz do repo).
2. **Resuma a sessão**: o que foi **aprendido** (🎓 Professor) e o que foi **construído**
   (🛠️ Construtor), e as **decisões** tomadas.
3. Atualize os artefatos em `ai-onboarding/`:
   - `user-profile.md` — anexe tudo que aprendeu sobre o aprendiz.
   - `progress.md` — semana/módulo atual, resumo da última sessão, decisões pendentes, perguntas
     abertas, e **Next Steps** separados em "🎓 Professor next" e "🛠️ Construtor next".
   - `build-log.md` — anexe a entrada cronológica desta sessão.
   - `architecture.md` — atualize **se a estrutura mudou**.
   - `knowledge-base/` (+ `glossary.md`) e `decisions/` — atualize/crie conforme necessário.
   - `learning-plan.md` — reconcilie detours e ajustes.
   - `sessions/` — crie a nota `YYYY-MM-DD-topico.md`: o que foi aprendido, o que foi construído,
     decisões, próximos passos. (Use a data real da sessão.)
4. Faça staging cirúrgico (`ai-onboarding/` e `.claude/`; nunca `_jarbas/`/`jarbas-*/`), commit com
   mensagem clara, e `git push -u origin <branch-atual>` (retry com backoff em falha de rede).
5. Feche com um **resumo limpo + próximos passos concretos**, pra próxima sessão (qualquer janela/
   dispositivo) retomar na hora.
