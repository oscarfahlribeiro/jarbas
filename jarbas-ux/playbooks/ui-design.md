# Playbook — design e crítica de interface (UI)

UI não é "deixar bonito" — é tornar a hierarquia e as ações **óbvias**. Toda crítica/decisão
deve apontar pra um princípio, não pra gosto.

## Os princípios de trabalho

- **Hierarquia visual:** o olho deve achar o mais importante primeiro. Tamanho, peso, cor e
  espaço criam ordem. Se tudo grita, nada é ouvido.
- **Espaçamento e agrupamento (Gestalt):** proximidade agrupa; espaço separa. Espaço em branco
  é estrutura, não desperdício.
- **Tipografia:** poucas famílias, escala consistente, contraste de tamanho/peso para nível.
- **Cor com função:** uma cor de marca + uma de ação + neutros + estados (sucesso/erro/aviso).
  Cor nunca é o único portador de significado (acessibilidade).
- **Componentes e estados:** desenhar todos os estados (default, hover, foco, ativo,
  desabilitado, carregando, vazio, erro) — o "estado vazio" e o "erro" são onde a maioria falha.
- **Consistência:** mesmo padrão para o mesmo problema; reduz carga cognitiva.

## Lente de avaliação — heurísticas de Nielsen (as 10)

Visibilidade do estado · correspondência com o mundo real · controle e liberdade do usuário ·
consistência e padrões · prevenção de erro · reconhecer > lembrar · flexibilidade/eficiência ·
estético e minimalista · ajudar a reconhecer/recuperar de erros · ajuda e documentação.
Use como checklist ao criticar uma tela.

## Como criticar uma tela (método)

1. Qual é a **ação principal** desta tela? Ela é a coisa mais óbvia? (hierarquia)
2. Passar as 10 heurísticas como checklist — anotar violações.
3. Para cada violação: princípio ferido + correção concreta (não "melhorar", e sim o quê).
4. Verificar os **estados** (vazio/erro/carregando).

## Modo de condução com o Oscar

Ancorar na direção visual que o projeto já decidiu (ex.: no casei é tema dark/tech, Inter,
linguagem de círculos — ver a memória de frontend do projeto). Crítica com princípio nomeado,
pra ele aprender a lente, não só receber o ajuste.

## Refino
Ao terminar, avalie melhorias e leve ao /retro. Se virar rotina entre projetos, graduar para
uma skill `forge-` (ex.: `forge-ui-critique`).
