# Playbook — Dependency Injection num componente que cria as próprias dependências

1. **Achar** onde o componente cria `client`/`conn`/etc. internamente.
2. **Promover a parâmetro** da função (com type hint).
3. **Subir a criação** para o composition root (geralmente o CLI / o entrypoint).
4. **Repassar pela cadeia** — cada nível recebe SÓ o que precisa (nem mais, nem menos).

**Conceito:** inversão/injeção de dependência (Tema C). Habilita testes (passar fakes) e troca
de implementação sem mexer na lógica.

*Exemplo real (casei):* um agente que criava `client` e `conn` internamente; o composition root
é o `apps/cli.py`. O normalizer **não** deveria receber `conn` (recebe só o que usa). Detalhes
no projeto.

## Refino
Ao terminar de usar este playbook, avalie se ele deve melhorar (passo, exemplo) e leve ao /retro.
