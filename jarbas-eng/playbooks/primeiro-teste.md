# Playbook — escrever o primeiro teste de um módulo existente

1. **Escolher por risco × facilidade:** funções **puras** de alto impacto primeiro (rápidas de
   testar, sem mocks).
2. **Definir os golden cases** — para resultado não-óbvio (ex.: score contínuo), Oscar precisa
   decidir "qual é o resultado correto". Não é binário como um booleano.
3. **Cobrir os extremos:** caso ideal, caso incoerente, eliminatório, entrada ausente (None).
4. (Quando o teste toca o banco) usar **fixture isolada** (arquivo temp + monkeypatch do path) —
   nunca o arquivo/registro de produção. `:memory:` costuma NÃO servir se cada conexão abre uma
   conexão nova (estado não compartilha).

**Conceito:** testabilidade (Tema D). O valor do teste é proporcional a quão **lento/indireto**
seria achar o bug sem ele.

**Disciplina (lição cara, registrada):** testes de **escrita** nunca tocam produção. Começar a
sessão de escrita já com `casal_id` de teste ou DB temp — não "corrigir depois".

*Exemplo real (casei):* avaliadores de `core/criterios.py` (funções puras) foram o primeiro
teste do projeto. Detalhes no projeto.

## Refino
Ao terminar de usar este playbook, avalie se ele deve melhorar (passo, exemplo) e leve ao /retro.
