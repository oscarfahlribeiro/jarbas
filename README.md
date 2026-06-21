# Jarbas — sistema de mentores (Claude Code skills)

Família de mentores especialistas que **ensinam enquanto fazem**: analisam criticamente a ideia
(não concordam por concordar), explicam o raciocínio, e executam com disciplina. Cada perfil é
uma especialidade; todos compartilham um cérebro comum.

## Estrutura

```
_jarbas/        cérebro compartilhado (NÃO é skill — pasta com _ na frente)
  persona.md    identidade, voz, postura "não concorda por concordar"
  metodo.md     como ensina (Explica → Questiona → Valida)
  modos.md      3 modos: aprofundar / obra / executar (+ default professor-executor)
  retro.md      refino de fim de sessão (o loop que faz o sistema melhorar)
  forja.md      quando/como criar ou melhorar uma skill (com portão anti-bloat)
  projetos.md   onde mora a memória de cada projeto
  aprendizado_oscar.md   perfil do aprendiz
jarbas-eng/     perfil de Engenharia de Software / Agentic AI / Claude Code (+ playbooks/)
jarbas-ux/      perfil de User Experience (+ playbooks/)
jarbas-business/ perfil de Estratégia, Modelo de Negócio, Precificação e Finanças
```

## Como usar

- Diga **"Jarbas"** → ativa `jarbas-eng`. **"Jarbas UX"** → ativa `jarbas-ux`.
  **"Jarbas business"** → ativa `jarbas-business`.
- Modos por frase: *"modo aprofundar"* (socrático), *"mão na massa/modo obra"* (execução com
  rede), *"executa e eu reviso"* (delegação). Sem sinal = professor-executor (analisa + ensina).
- Fim de sessão: *"retro"* → roda o refino.

## Instalar (para o sócio)

Estas skills carregam de `~/.claude/skills/`. Para usar:

1. `git clone <url-do-repo>` numa pasta de sua escolha.
2. Copie (ou faça uma junction de) `_jarbas/`, `jarbas-eng/`, `jarbas-ux/`, `jarbas-business/` para `~/.claude/skills/`.
   *Alternativa:* se sua `~/.claude/skills/` estiver vazia, dá pra clonar direto nela.
3. Reinicie o Claude Code e diga **"Jarbas"**.

Para atualizar: `git pull` e repita o passo 2 (ou, se usou junction/clonou direto, só `git pull`).

## Fronteira importante

Artefatos **específicos de projeto** (ex.: planos e personas do casei) **não** ficam aqui — eles
vivem no repo do próprio projeto. Ver `_jarbas/projetos.md`. Este repo é só o sistema agnóstico.
