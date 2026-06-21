# Playbook — mapeamento de jornada (journey map)

Journey map = retrato da **experiência do usuário ao longo do tempo** (fases, ações, pensamentos,
**emoções**, dores, oportunidades). Serve pra **alinhar um time sobre onde dói e onde agir** — o
entregável não é o diagrama bonito, é o *entendimento compartilhado + as oportunidades priorizadas*.
Se não muda uma decisão de produto, virou enfeite.

## Não confundir (o trio clássico)
- **User flow** — tela a tela, clique a clique. Micro, design de interface.
- **Journey map** — a *vivência* no tempo, **emoção no centro**. Macro. ← é este playbook.
- **Service blueprint** — journey map **+ bastidores** (o que a operação faz por trás). Vem depois.

## Anatomia (os blocos)
1. **Ator / persona** — de quem é a jornada.
2. **Cenário + escopo** — qual fatia do tempo (início → fim).
3. **Fases** — as colunas do tempo.
4. **Raias (swimlanes)** — quando há frentes *paralelas* (trilhos), uma raia por trilho.
5. **Camadas por fase** — ações · pensamentos/dúvidas · **emoções** · pontos de contato/canais ·
   dores · oportunidades.

## A curva emocional é a alma
É o que separa journey map de fluxograma. Desenhe a curva de emoção pelas fases (picos e vales).
Ela faz três coisas que as outras camadas, sozinhas, não fazem:
- **Prioriza** — diz *quanto* cada dor importa pro humano (o vale mais fundo é onde se perde o usuário),
  não só *onde* há atrito.
- **Protege os picos** — marca o que encanta e não pode quebrar.
- **Gera empatia** — alinha o time no *sentimento*, não só na lista de tarefas.
Os pontos de emoção extrema (pra cima ou pra baixo) são os **"momentos que importam"** — onde focar.

## Estrutura real: nem sempre é linha reta
- **Trilhos paralelos (swimlane)** — várias frentes que o usuário equilibra ao mesmo tempo; a
  sobrecarga costuma vir do *malabarismo entre trilhos*, não de um trilho só.
- **Loops repetíveis** — um mesmo mini-ciclo que se repete por item (ex.: "selecionar X" repetido
  por categoria), às vezes ancorado por um item que vem primeiro e condiciona os demais.

## Multi-perfil: 3 padrões (não faça mapa novo à toa)
- **Mapa separado** — só quando o *caminho* diverge estruturalmente (fases/ações diferentes).
- **Curva sobreposta** — mesmo caminho, *sentido diferente*; várias curvas no mesmo mapa.
- **Raia por ator** — mesmo journey, atores *interagindo* (um entra em fases específicas).
Personas vivem em **eixos ortogonais** (papel × estilo de decisão…) — ver `persona-building.md`.

## Passos de construção
1. **Aterrissar na evidência** (entrevista, uso). Sem isso → rotular **proto-jornada** (hipótese).
2. Mapear **ações** na linha do tempo.
3. Sobrepor **pensamentos e emoções** (aqui ganha vida).
4. Marcar **dores** nos vales.
5. **Derivar oportunidades** de cada dor (a ponte jornada → produto).
6. Achar os **momentos que importam** e priorizar (pela profundidade do vale).
7. **Validar** com pesquisa; a proto vira jornada de verdade.

## Modo de condução com o Oscar
Etiquetar **evidência vs hipótese** por célula (ele tem faro de dados). **Renderizar a curva**
(canvas/SVG) ajuda muito — ele pensa melhor reagindo a artefato visual. Usar "duas opções pra
comparar" nas bifurcações (ex.: jornada por unidade vs por ator).

## Refino
Ao terminar, avalie melhorias (passo, exemplo) e leve ao /retro. Se provar reuso entre projetos,
graduar pra `forge-jornada` via `_jarbas/forja.md`.
