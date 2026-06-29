---
description: Salvar e sincronizar — git pull, commit de tudo e push pro GitHub.
---

Você é o **Osmar**. Este comando salva o progresso pra trocar de dispositivo com segurança.

1. Rode `git pull` (na raiz do repo) pra integrar mudanças remotas.
2. Faça `git status` e mostre ao aprendiz o que mudou (staging cirúrgico — adicione os arquivos do
   `ai-onboarding/` e `.claude/`; **não** toque em `_jarbas/` nem `jarbas-*/`).
3. Faça commit com uma mensagem clara e descritiva do que mudou nesta sessão.
4. `git push -u origin <branch-atual>`. Se falhar por rede, tente de novo com backoff (2s, 4s, 8s, 16s).
5. Confirme ao aprendiz que está tudo salvo e sincronizado, e que ele pode continuar de qualquer
   janela/dispositivo.

Observação: este comando **não** escreve resumos nem notas de sessão — isso é o `/wrap`. Use
`/sync` pra salvar no meio do caminho.
