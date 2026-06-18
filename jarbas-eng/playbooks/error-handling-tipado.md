# Playbook — error handling tipado + falha parcial

1. **Identificar onde erros são engolidos:** `try/except` mudo, `or {}` que mascara exceção, etc.
2. **Criar/usar a hierarquia** de exceções por domínio (uma raiz → subclasses).
3. **Cada camada traduz** erro de infra em erro de domínio; re-lança com contexto. **Cada camada
   trata o erro da camada imediatamente abaixo dela** (não de cima pra baixo).
4. **A borda (CLI/API) captura** o erro de domínio → mensagem amigável; deixa `Exception` crua
   subir (é bug, vira log).

**Conceito:** error handling (Tema E). **Falha parcial em lote:** registra o erro do item,
continua, reporta ao final — um item ruim não derruba o batch.

*Exemplo real (casei):* hierarquia em `casei/core/exceptions.py` (`CaseiError` → subclasses).
Detalhes no projeto.

## Refino
Ao terminar de usar este playbook, avalie se ele deve melhorar (passo, exemplo) e leve ao /retro.
