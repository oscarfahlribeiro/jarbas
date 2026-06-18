# Playbook — refatorar uma camada

Caso típico: um componente que **bypassa** a camada de dados (ex.: um agente que chama o
banco direto em vez de passar pelo repository).

1. **Caracterizar:** rodar o fluxo atual e salvar o resultado como baseline (characterization
   test). É a rede de segurança.
2. **Localizar o vazamento:** o ponto exato onde a regra de dependência é violada (chamada
   direta que deveria passar por outra camada).
3. **Mover a query** para a camada certa (ou usar a função que já existe lá).
4. **Trocar a chamada** no componente para usar a camada certa.
5. **Rodar o characterization test** — resultado idêntico = refatoração segura.

**Conceito:** regra de dependência única (Tema A). Ganho concreto: quando a infra trocar
(ex.: SQLite → Postgres), só a camada de dados muda.

*Exemplo real (casei):* `ranker.py` chamando `db.py` direto em vez do `repository`. Detalhes do
caso no projeto (ver `_jarbas/projetos.md`).

## Refino
Ao terminar de usar este playbook, avalie se ele deve melhorar (passo, exemplo) e leve ao /retro.
