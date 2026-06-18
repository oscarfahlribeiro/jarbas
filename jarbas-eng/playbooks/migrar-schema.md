# Playbook — migrar schema ou dados (risco máximo)

**Pré-requisito inegociável:** contratos (B) → testabilidade (D) → migração. Nessa ordem. Você
precisa do formato-ALVO definido pra escrever o teste de comparação.

1. **Declarar o formato alvo** como contrato (Pydantic).
2. **Escrever o teste de comparação antes/depois:** "os N registros que tinham X têm o
   equivalente em Y após migrar". (Characterization/TDD invertido: o teste do bug nasce
   VERMELHO no código velho, prova que a rede pega, refatora até VERDE.)
3. **Migração em passos:** cria estrutura nova → migra dados existentes (**preserva!**) → só
   então torna obrigatório / remove o antigo. `INSERT OR IGNORE` para reconciliar o que já existe.
4. **Dry-run / backup** antes do real.

**Conceito:** schema migrations (Tema H). O passo que mais falha é a **preservação de dados
existentes**. DROP idempotente seguindo o padrão dos DROPs já existentes.

*Exemplo real (casei):* `criterios_casal` + `criterios_casal_historico` (versionamento), e a
aposentadoria da tabela legada `avaliacoes`. Detalhes no projeto.

## Refino
Ao terminar de usar este playbook, avalie se ele deve melhorar (passo, exemplo) e leve ao /retro.
