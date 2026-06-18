# Playbook — construção de personas (baseada em evidência)

Persona = retrato arquetípico de um usuário real, que alinha o time sobre "pra quem estamos
desenhando". O erro clássico é **inventar** a persona; o certo é **derivá-la de evidência**.

## Persona vs proto-persona

- **Proto-persona:** hipótese inicial, montada com o que já se sabe/assume — útil pra começar,
  **rotulada como hipótese**.
- **Persona (de verdade):** baseada em pesquisa (entrevistas, dados de uso, comportamento real).
  Substitui a proto-persona conforme a evidência chega.

## Anatomia (campos que importam)

1. **Nome + foto + 1 frase** que captura a pessoa (humaniza, evita "usuário 1").
2. **Contexto** — situação de vida/trabalho relevante ao produto.
3. **Objetivos (goals)** e **Jobs-to-be-done** — o que ela está tentando *conseguir* (o JTBD é
   mais robusto que "necessidade" porque é estável e independente da solução).
4. **Dores / frustrações** — o atrito atual.
5. **Comportamentos e contexto de uso** — quando/onde/com que dispositivo.
6. **Citação real** (se houver pesquisa) — ancora em evidência.

**Cortar o que não muda decisão de design** (renda fictícia, hobbies decorativos). Cada campo
deve poder influenciar uma escolha de produto, senão é enfeite.

## Passos

1. Reunir a evidência disponível (ou marcar explicitamente o que é hipótese).
2. Encontrar **padrões** → agrupar em 1-3 personas (mais que isso dilui o foco).
3. Preencher a anatomia; para cada campo, perguntar "isso muda uma decisão de design?".
4. Validar contra casos reais; revisar quando chegar evidência nova.

## Modo de condução com o Oscar

Distinguir explicitamente hipótese vs evidência (ele tem faro de dados e vai querer isso claro).
Usar o formato "duas opções pra comparar" nos cortes (ex.: 1 persona ampla vs 2 segmentadas).

## Refino
Ao terminar, avalie melhorias (campo, exemplo) e leve ao /retro. Se virar rotina entre projetos,
graduar para `forge-persona`.
