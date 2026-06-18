# Playbook — montar uma pasta de referências de UX

Objetivo: transformar links soltos + conceitos espalhados numa **biblioteca de referência
navegável** que orienta as decisões de UX/UI de um projeto. Método agnóstico; a saída vai pra
subpasta `ux\` do projeto ativo (caminho em `_jarbas/projetos.md`).

## Princípio

Uma boa pasta de referências não é um "favoritos". É **curada e anotada**: cada item entra com
um *porquê* (o que ensina, onde se aplica no projeto) e está **organizado por conceito**, não por
data de descoberta. Referência sem anotação envelhece e ninguém volta nela.

## Passos

1. **Definir os eixos** (com Oscar) — os conceitos/temas que o projeto precisa cobrir. Ex.:
   design system, padrões de navegação, onboarding, microinterações, acessibilidade,
   inspiração visual, concorrentes. Cada eixo vira uma seção.
2. **Para cada link, capturar 4 campos:**
   - **link** (URL)
   - **o que é** (1 linha)
   - **por que importa pro projeto** (o encaixe — a parte que mais agrega)
   - **tag/eixo** (a qual conceito pertence)
3. **Organizar conceitos junto dos links** — não só "onde achar", mas "o que é a ideia". Um
   conceito pode ter 0..N links. Conceito sem link ainda vale (é vocabulário a aprender).
4. **Marcar prioridade/estado** — `explorar agora` / `quando precisar` / `só referência`.
5. **Fechar com uma síntese** — "o que olhar primeiro" (3-5 itens), pra a pasta ter um ponto de
   entrada e não virar um depósito.

## Estrutura de saída sugerida (na pasta do projeto)

- `referencias.md` — os links curados, por eixo, com os 4 campos.
- `conceitos.md` — os conceitos organizados (vocabulário + ideia + ligação com os links).
- (opcional) subpastas por mídia se houver muitos prints/PDFs.

## Modo de condução com o Oscar

Ele aprende fazendo e gosta de **comparar/justificar**. Em vez de despejar uma lista pronta:
propor os eixos em 2-3 opções de recorte, deixá-lo escolher, e ir preenchendo junto —
ensinando o conceito de cada eixo enquanto cataloga. Mostrar a pasta tomando forma.

## Refino
Ao terminar de usar este playbook, avalie se ele deve melhorar (campo novo, eixo recorrente) e
leve ao /retro. Se a curadoria virar rotina entre projetos, graduar para uma skill `forge-`.
