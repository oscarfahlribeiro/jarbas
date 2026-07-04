# Glossário — como funciona (método, agnóstico)

O vocabulário e os erros de transcrição são **por projeto** — vivem no **glossário do projeto**,
na pasta de revisões dele (caminho na seção *Revisões de interface* do `_jarbas/projetos.md`).
Este arquivo explica só o método. *(Anti-contaminação: nenhum termo de projeto aqui.)*

## As duas funções do glossário do projeto

1. A seção **Vocabulário** vira o `--prompt` do `transcrever.py` (initial_prompt do Whisper —
   corrige nomes próprios **na fonte**).
2. A tabela de **erros conhecidos** guia a normalização pós-transcrição (§3 do SKILL).
   Ao notar um erro novo, **adicionar à tabela do projeto** — o glossário melhora a cada sessão.

## Formato esperado (no glossário do projeto)

```markdown
## Vocabulário
<termos separados por vírgula: nomes próprios, jargão do produto, telas>

## Erros conhecidos → correção
| Whisper transcreveu | Era |
|---|---|
| ... | ... |
```

## Falantes (heurística, sem diarização)

Inferir pelo contexto: quem **opera** a interface costuma explicar o que está na tela e
perguntar ("o que você achou?"); o(a) **convidado(a)** responde com a crítica. Rotular pelos
nomes quando o contexto deixa claro; na dúvida, `[?]` — não inventar certeza.
