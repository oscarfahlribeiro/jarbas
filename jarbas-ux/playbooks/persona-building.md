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

## Segmentação: eixos, MECE e poda

- **Proto-persona pode nascer da experiência vivida do próprio time** (n=1, primeira mão) — não só
  de pesquisa externa. Rotular como hipótese; vale ouro pra não inventar do zero.
- **Perfis vivem em EIXOS ortogonais** (ex.: *papel* no grupo × *estilo de decisão*). Não jogar
  eixos diferentes numa lista só: **MECE só vale DENTRO de um eixo**, nunca cruzando eixos. "Persona
  A maximizadora" é um *ponto numa grade*, não um item de lista.
- **Abrir o leque largo pra descoberta, depois PODAR pros 2–3 eixos que importam.** Critério de poda
  (ambos obrigatórios): (1) **discrimina** — as pessoas de fato variam nesse eixo; (2) **acionável**
  — saber onde a pessoa cai *muda uma decisão de produto*. Senão é **trivia inerte** (ex.: "signo do
  casal" discrimina mas não é acionável). A pesquisa é o filtro que separa acionável de inerte.
- **Estilos de decisão** úteis como ponto de partida (adaptar ao domínio): maximizador↔satisficer;
  analítico↔intuitivo; *driver* (orçamento/experiência/esforço/status/valores); controle↔delegação;
  averso↔tolerante a risco; motor emocional (medo↔desejo).
- **Quando os perfis diferem, escolher o artefato certo** (mapa separado vs curva sobreposta vs raia
  por ator) — ver `jornada-usuario.md`.

## Modo de condução com o Oscar

Distinguir explicitamente hipótese vs evidência (ele tem faro de dados e vai querer isso claro).
Usar o formato "duas opções pra comparar" nos cortes (ex.: 1 persona ampla vs 2 segmentadas).

## Refino
Ao terminar, avalie melhorias (campo, exemplo) e leve ao /retro. Se virar rotina entre projetos,
graduar para `forge-persona`.
