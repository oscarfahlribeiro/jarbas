# Playbook — condução de entrevista de descoberta (com o usuário)

Entrevista de descoberta serve pra **converter hipótese em evidência**: sai de proto-persona
(palpite) pra entender o usuário real. O erro clássico é tratar a entrevista como questionário
de opinião; o certo é **escavar comportamento real ao longo da jornada**.

> Status: nasce playbook (forja: capacidade praticada 1x). **Gatilho de graduação:** na 1ª vez
> que for usada em **outro projeto**, graduar pra skill top-level `forge-entrevista` (ver
> `_jarbas/forja.md`).

## Princípio-mãe — comportamento real, não opinião declarada
O que as pessoas *dizem que fazem* e o que *de fato fazem* quase nunca batem. Pergunta de
opinião ("o que é importante pra você?") gera resposta genérica e racionalizada. Pergunta
comportamental ("o que você fez da última vez?") fura essa casca e traz a dor verdadeira.

## O arco da entrevista (estrutura no tempo)
1. **Abertura — grand-tour:** peça a pessoa **narrar um evento real desde o começo**, sem opinar.
   ("Me leva pro começo: quando começou, qual foi a *primeira coisa* que você fez?") O comportamento
   bruto aparece sozinho — e as dores junto.
2. **Percorrer a jornada:** siga a **linha do tempo** que a pessoa abrir, fase a fase. **Este é o
   pilar:** a entrevista bem feita reconstrói a jornada do usuário no tempo. Em cada fase, capture:
   - **o que fez** (ação)   ·   **o que pensou** (raciocínio/critério)
   - **como se sentiu** (emoção)   ·   **onde doeu** (atrito/frustração)
   Isso é exatamente a matéria-prima de um **journey map** — entrevista → persona → jornada.
3. **Aprofundar incidentes:** dentro de uma fase, mergulhe nos momentos concretos (ver técnicas).
4. **Wind-down:** feche com uma pergunta de abertura ("se tivesse uma varinha mágica, o que
   mudaria?", "o que mais te surpreendeu?") — costuma revelar o desejo latente.

## Técnicas (o ofício)
- **História antes de opinião** — abra pela grand-tour, não por "o que você acha".
- **Comportamental, não hipotético** — "me conta da última vez que…", "o que você *fez* na
  prática?". Evite "o que você faria se…" (convida invenção).
- **Reflexo** — repita de volta em 1 linha o que captou; valida e deixa a pessoa corrigir.
- **Estacionar threads** — se aparecem 2 fios ricos, siga 1 e *anuncie* que volta no outro.
  Perguntar 2 coisas juntas faz a pessoa responder só a última.
- **Sondar o incidente crítico** — quando a pessoa nomeia uma emoção forte, mergulhe no
  **momento exato** (memória episódica guarda o detalhe que a opinião apaga). **Com ressalva** →
- **Vigiar o viés de confirmação DO ENTREVISTADOR** — o anti-padrão mais perigoso: cavar onde
  *você* está empolgado porque confirma sua tese, em vez de seguir pra onde *a pessoa* ia.
  Entrevistador bom **segue o entrevistado**; ansioso lidera pra própria hipótese.
- **Recuar quando a resposta encurta** — um "e aí, como foi?" + silêncio rende mais que uma
  pergunta nova. A 2ª resposta costuma ser mais verdadeira que a 1ª.
- **Laddering** — de uma funcionalidade citada, pergunte "por que isso importa?" repetidamente
  até chegar no **job emocional** por trás.

## Anti-padrões (erros a evitar)
- **Pergunta indutora** — plantar a resposta dentro da pergunta.
- **Pergunta fechada cedo demais** — "quantas abas você tinha?" mata a narrativa; abra primeiro.
- **Pergunta dupla** — duas perguntas numa só; a pessoa responde uma e a outra se perde.
- **Comprar a 1ª resposta** — "a gente comparava" pode esconder "na verdade não comparava, só
  buscava mais". Sempre cheque com o comportamental.
- **Fixar na própria tese** (viés de confirmação, acima) — o mais traiçoeiro.

## Roteiro pré-estabelecido (quando precisa de escala/consistência)
A entrevista exploratória pode ser fluida. Quando vira **plano** (vários respondentes, com
comparabilidade), monte um roteiro com perguntas fixas — mas:
- **Adaptativo (branching):** espinha fixa + **módulos que disparam pelo contexto** do respondente
  (ex.: estágio na jornada) + **sondas condicionais** (só pergunta o ramo relevante). Mantém leve —
  cada pessoa só vê o que lhe cabe.
- **Sempre pilotar:** rode **1 piloto** antes do plano — pega pergunta confusa, indutora ou longa
  demais antes de queimar respondentes reais.
- **Público em grupo (casal/time):** entrevistar **cada um individualmente, mesmo roteiro**, e
  comparar → a **divergência** vira achado sobre perfis.
- **Não dependa de anotação:** notetaker grátis que grava+transcreve (com consentimento) > memória.
- **Orçamento de tempo:** anote tempo-alvo por bloco; some o caminho mais longo do branching.

## Refino
Ao terminar de usar este playbook, avalie se ele próprio deve melhorar (passo, exemplo,
técnica, anti-padrão) e leve isso ao /retro. Se provar reuso em outro projeto, graduar pra
`forge-entrevista` via `_jarbas/forja.md`.
