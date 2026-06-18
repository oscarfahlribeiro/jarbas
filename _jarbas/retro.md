# Retro — refino de fim de sessão

O loop que faz o sistema **melhorar com o uso**. Herdado por todos os perfis.

## Quando rodar

- Oscar sinaliza fim: **"fecha a sessão"**, **"retro"**, "vamos encerrar"; OU
- ao concluir um **bloco grande** de trabalho (mesmo sem Oscar pedir, oferecer rodar).

## Regra de ouro

**Apresentar o que vai gravar e esperar aprovação antes de escrever** (CLAUDE.md do Oscar:
confirmar nas decisões). O retro propõe; Oscar aprova.

## Antes de gravar qualquer coisa — classificar (invariante anti-contaminação)

Para cada coisa a registrar, decidir o escopo (a localização encoda o escopo):

- **AGNÓSTICO** (sobre Oscar-aprendiz, sobre Jarbas, "como fazer" genérico)
  → camada global (`_jarbas/…` ou uma skill).
- **PROJETO** (sobre casei ou outro projeto específico)
  → pasta do projeto (ver `projetos.md`).

## Os 4 passos

1. **O que Oscar aprendeu/praticou?**
   → agnóstico: `_jarbas/aprendizado_oscar.md` · projeto: `memory\<projeto>\aprendizados_<projeto>.md`.
   Registrar conceito, nível de entendimento, gaps, e o que se aprendeu sobre o Oscar.

2. **Surgiu artefato ou decisão de projeto?**
   → escrever no arquivo certo da pasta do projeto (plano, pesquisas, ux, …).

3. **Repetimos um procedimento que vale virar reutilizável?**
   → decidir **criar / melhorar / pular** uma skill, aplicando o **portão anti-bloat** da
   `forja.md` (só forja se: repetível + não-óbvio + provável reuso >1x).

4. **A persona, um perfil ou um modo se mostrou mal-calibrado?**
   → propor edição em `persona.md` / `modos.md` / no `SKILL.md` do perfil. Mostrar a Oscar,
   aplicar com aprovação. **É assim que os perfis se afinam com o tempo.**

## Fronteira entre as duas memórias de projeto

Existem duas camadas de memória do casei e elas **não se sobrescrevem**:
- **Memória do harness** (`memory\*.md` na raiz, indexada no `MEMORY.md`) = fatos
  operacionais/de produto que o harness curta.
- **`memory\casei\…`** (artefatos do Jarbas) = planos, pesquisas e aprendizados pedagógicos
  que o mentor produz.
O retro pode **promover** um fato durável de uma pra outra — explicitamente, nunca silenciosamente.
