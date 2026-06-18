# Forja — criar e melhorar skills

Como o Jarbas se auto-melhora sem inchar. Não construímos um "motor de forja" — embrulhamos a
skill embutida **`anthropic-skills:skill-creator`** com as convenções abaixo.

## Portão anti-bloat (decidir ANTES de forjar)

Só vira skill se o procedimento for:
- **(a) repetível** — vai acontecer de novo;
- **(b) não-óbvio** — tem critério/ordem que se perde se não registrar;
- **(c) provável reuso > 1x** — em mais de um momento/projeto.

Se **não** passar nos três: registrar como **uma linha** em `aprendizado_oscar.md` (se for
aprendizado agnóstico) ou como um **playbook** na pasta do perfil/projeto. Skill é caro;
catálogo inchado dilui o auto-disparo.

## Roteamento — onde a coisa nasce

| O que é | Onde vai |
|---|---|
| Capacidade **agnóstica** reutilizável entre projetos (ex.: "construir persona") | skill top-level `forge-<capacidade>` (auto-dispara em qualquer lugar) |
| Procedimento **interno de um perfil** (ex.: "refatorar uma camada") | arquivo em `<perfil>\playbooks\` |
| Coisa **específica de um projeto** | pasta do projeto (`projetos.md`) |

Um playbook que provar reuso entre projetos **gradua** pra `forge-<capacidade>` — não nasce
skill antes de provar valor.

## Como criar

1. Rodar `anthropic-skills:skill-creator`.
2. Nome: `forge-<capacidade>` (kebab-case), descrição em estilo de gatilho (3ª pessoa,
   "Ative quando…").
3. **Rodapé obrigatório em TODA skill gerada:**

   ```
   ## Refino
   Ao terminar de usar esta skill, avalie se ela própria deve melhorar
   (passo, exemplo, gatilho) e leve isso ao /retro.
   ```

   Esse rodapé é o que faz o sistema **compor**: cada skill gerada carrega seu próprio gancho
   de melhoria, então o loop fecha — fazer → retro → virar playbook ou skill → na próxima já
   está disponível → um retro futuro a melhora.

## Gatilho C4 (delegação → captura)

No modo `executar`, depois que Oscar revisa o trabalho delegado, perguntar
*"este 'como fazer' vira capacidade reutilizável?"* e aplicar o portão acima. É o requisito
do Oscar: toda tarefa delegada e revisada é candidata a virar capacidade.
