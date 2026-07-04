---
name: jarbas-revisao
description: Ative com /jarbas-revisao (toggle gravar→parar), com /jarbas-revisao <arquivo(s)> para submeter gravações/transcrições prontas, ou quando Oscar disser "gravar revisão", "revisar a interface falando", "parar gravação", "analisar esses áudios/vídeos como revisão", "feedback de vibecoding". É o ciclo de revisão falada da família Jarbas para interfaces vibecoded — grava o microfone enquanto Oscar testa (ou recebe arquivos prontos), transcreve local (Whisper, $0), normaliza a fala (glossário + falantes) e convoca o COMITÊ (jarbas-ux + jarbas-eng em paralelo + consolidação) que transforma a crítica em proposta numerada R1..Rn com prós/contras e recomendação; Oscar aprova por número, as mudanças aprovadas são executadas e a interface é relançada para o próximo ciclo. Argumentos - caminhos de arquivo/pasta (fluxo ARQUIVOS), rapido (sem comitê), status, cancelar.
---

# Jarbas — revisão falada de interface (o ciclo de vibecoding)

Orquestrador da família Jarbas: transforma o que Oscar **fala enquanto testa** uma interface
em **requisitos analisados e mudanças aprovadas**. A sessão principal carrega antes:
`_jarbas/persona.md` (voz, "não concorda por concordar") e `_jarbas/projetos.md` (caminhos
do projeto ativo — seção *Revisões de interface*). Os perfis especialistas (jarbas-ux,
jarbas-eng) são carregados **pelos subagentes do comitê**, não pela sessão principal.

## O ciclo

```
/jarbas-revisao ────────────► 🔴 grava enquanto Oscar testa e fala
/jarbas-revisao ────────────► ⏹ para → transcreve (Whisper local)
/jarbas-revisao <arquivos> ─► 📁 sem gravar: transcreve arquivos prontos (áudio/vídeo/txt)
                    │
                    ▼ normaliza (glossário + falantes)
                    ├─► 🎨 jarbas-ux   requisito de experiência, sem meia-solução, refs reais
                    ├─► 🔧 jarbas-eng  código afetado, trade-offs, alternativas, esforço/risco/custo
                    └─► 📋 consolida  → proposta R1..Rn → Oscar aprova por número
                         → executa aprovados → relança a interface → próximo ciclo
```

## Caminhos

- **RAIZ** do skill: `~\.claude\skills\jarbas-revisao\` (nesta máquina: `C:\Users\Oscar\.claude\skills\jarbas-revisao\`)
- Python: `RAIZ\.venv\Scripts\python.exe` — se não existir, § Setup.
- Estado: `RAIZ\state\gravacao.json` (lock da gravação ativa) · `RAIZ\state\PARAR` (sinal de parada)
- Áudios: `RAIZ\gravacoes\` — **nunca** em repo de projeto (pesado; o repo recebe só `.txt`/`.md`).
- Pasta de revisões, artefatos, código e **glossário do projeto**: `_jarbas/projetos.md`
  § *Revisões de interface*. **Se o projeto ainda não tem a seção lá:** perguntar os caminhos a
  Oscar UMA vez (código da interface, artefatos de UX, pasta de revisões), criar a seção e seguir.
  **Nunca** preencher um placeholder com caminho não verificado.

## 0 · Toggle — decidir o fluxo

1. **Arquivos na chamada?** (caminhos/@-menções de áudio, vídeo, transcrição ou pasta) →
   fluxo **ARQUIVOS** (§1b) — não mexe no lock nem na gravação.
2. Argumentos: `rapido` (§7) · `status` (há gravação ativa? de qual projeto? desde quando?) ·
   `cancelar` (criar `state\PARAR`, apagar o lock, **não** transcrever; perguntar se apaga o áudio).
3. Se `state\gravacao.json` **não existe** → fluxo **GRAVAR** (§1).
4. Se **existe** → ler o lock e triar:
   - **Dono morto?** `Get-Process -Id <pid>` falha, ou `inicio` mais velho que o teto de horas
     → fluxo **RECUPERAR** (§2b), não PARAR.
   - **Outro projeto/janela?** Se o `projeto` do lock não bate com o contexto atual, perguntar
     antes de agir: "há gravação ativa de *<projeto>* desde *<hora>* — paro ela, ou foi engano?"
     (Oscar trabalha em janelas paralelas; não parar a gravação de outra janela sem confirmar.)
   - Senão → fluxo **PARAR** (§2).

## 1 · GRAVAR

1. Se `.venv` não existe → § Setup primeiro (avisar que a 1ª vez demora).
2. **Criar o lock ANTES de tudo, atomicamente** (fecha a corrida entre janelas paralelas):
   `New-Item -ItemType File RAIZ\state\gravacao.json` — se **falhar porque já existe**, outra
   janela ganhou: voltar à triagem do §0. Em seguida preencher com o **Write tool** (UTF-8;
   `Set-Content` do PS 5.1 gravaria UTF-16): `{"arquivo": "<flac>", "inicio": "<ISO>", "projeto": "<nome>"}`.
3. Saída: `RAIZ\gravacoes\<AAAA-MM-DD_HHMMSS>.flac` (16 kHz mono; **segundos no nome** — nunca
   reutilizar caminho).
4. Iniciar em background (PowerShell, `run_in_background: true`):
   `& "RAIZ\.venv\Scripts\python.exe" "RAIZ\gravar.py" "<saida.flac>" "RAIZ\state\PARAR"`
5. Após ~2s, ler o output da task. **Health-check:** exigir `[pid] N` **e** `[gravando] dispositivo: …`
   — este último só é impresso **depois** de o stream abrir de verdade. Se não vieram: a gravação
   NÃO está rodando → apagar o lock, reportar o erro do output. Se vieram: completar o lock
   (Write tool) com `"pid"` e `"task_id"`.
6. *(Opcional, se o protótipo estiver com preview/server ativo)*: capturar um screenshot da tela
   inicial como contexto visual da sessão.
7. Responder **curto**: "🔴 Gravando — teste à vontade e fale. `/jarbas-revisao` de novo para parar."

## 1b · ARQUIVOS — submeter gravações/transcrições prontas (sem gravar)

Para revisões já gravadas por fora (Meet, gravador do celular/Windows, vídeos) ou já transcritas.

1. **Aceitar:** um ou mais caminhos de **mídia** (`.m4a .mp4 .mp3 .wav .flac .ogg .webm .mkv`),
   de **transcrição pronta** (`.txt`, `.docx` — extrair o texto), ou uma **pasta** (pegar as
   mídias de dentro). Resolver o projeto como no GRAVAR (via `projetos.md`; perguntar se ambíguo).
2. **Transcrever o que for mídia** (background, com o vocabulário do glossário do projeto):
   `& "…python.exe" "RAIZ\transcrever.py" "<arquivo>" --prompt "<vocabulário>"`
   — o Whisper lê áudio E vídeo direto (PyAV). Vários arquivos: **até 2 em paralelo** (lição da
   máquina; mais que isso, avisar que vai em levas). Se já existe `.txt` ao lado da mídia, usar
   e **não** retranscrever (a menos que Oscar peça).
3. **Normalizar cada fonte** (§3), rotulando `[A]`, `[B]`… quando houver mais de uma; salvar na
   pasta da sessão como `transcricao-A.txt`, `transcricao-B.txt` (ou `transcricao.txt` se única).
4. Seguir para o **comitê** (§4) com as fontes concatenadas, separadas por
   `=== FONTE A: <nome do arquivo> ===` — as duas análises tratam as fontes como UMA revisão
   (críticas repetidas entre fontes = sinal forte, apontar).
5. **Mídia pesada fica onde está** (não copiar pra dentro de repo); se já estiver dentro de um
   repo, conferir que o `.gitignore` a cobre antes de qualquer commit.

## 2 · PARAR → transcrever

1. Criar `state\PARAR` (arquivo vazio). Aguardar `<arquivo>.flac.done` (poll ~0,5s, até 30s).
   Se não aparecer → fluxo **RECUPERAR** (§2b).
2. Montar o **prompt de vocabulário** com os termos do **glossário do projeto** (caminho na seção
   *Revisões de interface* do `projetos.md`; o `RAIZ\glossario.md` explica só o método).
   Transcrever em background:
   `& "…python.exe" "RAIZ\transcrever.py" "<arquivo>.flac" --prompt "<vocabulário>"`
3. Apagar `state\gravacao.json`. **Enquanto transcreve**, pré-ler os artefatos do projeto
   (requisitos, backlog de revisões, código do protótipo) — adianta o comitê.
4. Na notificação da task: ler o `.txt` gerado (fica ao lado do `.flac`).

## 2b · RECUPERAR (gravação morta ou lock órfão)

Sinais: PID do lock não existe mais · `.done` não apareceu em 30s · lock mais velho que o teto.
1. **Limpar o estado**: apagar `state\gravacao.json` **e** `state\PARAR` (senão todo toggle
   futuro cai aqui de novo).
2. O `.flac` parcial **sobrevive** (flush a cada 30s): oferecer transcrever o parcial.
3. Reportar a causa provável (ex.: Modern Standby matando processos de fundo — padrão conhecido
   desta máquina; sessão que caiu; mic tomado por outro app).

## 3 · NORMALIZAR (sessão principal, sem subagente)

Produzir a **transcrição normalizada**:
- corrigir termos pela tabela do **glossário do projeto** — e **adicionar lá** os erros novos
  que notar (o glossário melhora a cada sessão; erros/vocabulário de projeto ficam NO projeto);
- inferir e rotular **falantes** pelo contexto (heurística no `RAIZ\glossario.md`); na dúvida, `[?]`;
- anotar **a que tela/seção** cada trecho se refere;
- manter timestamps.
Salvar em `<pasta_revisoes>\<AAAA-MM-DD>_sessao-NN\transcricao.txt` (NN = próximo número livre).

## 4 · COMITÊ — dois subagentes em paralelo (uma mensagem, duas chamadas Agent)

Preencher `{…}` com os caminhos do `projetos.md` e a transcrição normalizada.

**Subagente UX** (`subagent_type: general-purpose`):

```
Você é o perfil jarbas-ux analisando uma REVISÃO FALADA da interface de {PROJETO}.

PREPARO (leia nesta ordem, antes de opinar):
1. C:\Users\Oscar\.claude\skills\jarbas-ux\SKILL.md e C:\Users\Oscar\.claude\skills\_jarbas\persona.md
   — seu jeito: não concordar por concordar.
2. Artefatos do projeto: {ARTEFATOS_UX} (personas, requisitos da jornada, identidade visual,
   design system) e o backlog de revisões: {BACKLOG}.

TAREFA — a transcrição normalizada está abaixo. Para CADA crítica/pedido (e elogio):
- **Citação** curta do que foi dito (com timestamp e falante).
- **Princípio de UX em jogo** (nomeie: hierarquia, affordance, feedback, consistência, carga
  cognitiva, prevenção de erro, reconhecimento>memorização…).
- **Ligação com o projeto**: a que persona/modo e a que requisito existente se conecta (use os
  IDs do projeto, se houver); pedido de FLUXO/PRODUTO (não de tela) → marque `[PRODUTO]`.
- **O que precisa mudar — específico e ambicioso.** Não aceite meia-solução: se pediram
  interatividade, proponha a melhor experiência possível e cite REFERÊNCIAS REAIS (produtos e
  padrões conhecidos, e onde vê-los funcionando). Sua régua é SÓ a experiência; custo técnico é
  problema do eng — não rebaixe a ambição por ele. Quando sua proposta FOR ALÉM do pedido
  original, marque o item com `[AMPLIADO]` (o eng vai custear a ampliação depois).
- **Severidade**: bloqueia / incomoda / polimento.
- **Recorrente?** — confira o backlog; crítica repetida = sinalizar (regressão ou não-resolvido).
Elogios também são dado: registre o que NÃO deve ser mexido.

RETORNO: markdown estruturado (vira analise_ux.md), itens numerados UX-1..UX-n.
=== TRANSCRIÇÃO NORMALIZADA ===
{TRANSCRICAO}
```

**Subagente Eng** (`subagent_type: general-purpose`):

```
Você é o perfil jarbas-eng analisando TECNICAMENTE os pedidos de uma revisão falada da
interface de {PROJETO}.

PREPARO (leia antes):
1. C:\Users\Oscar\.claude\skills\jarbas-eng\SKILL.md e C:\Users\Oscar\.claude\skills\_jarbas\persona.md.
2. O CÓDIGO da interface: {CODIGO} — e os princípios/arquitetura do projeto em {DOCS_TECNICOS}.

TAREFA — para cada pedido da transcrição abaixo:
- **Onde vive no código** (arquivo:linha) e o que exatamente seria alterado.
- **Bate com os princípios/arquitetura do projeto?** (apontar conflito, se houver)
- **Trade-offs explícitos** (ex.: animação rica × peso/latência; lib nova × dependência;
  efeito visual × acessibilidade) e **ALTERNATIVAS mais leves com efeito similar** — se o pedido
  for inviável como pedido, desenhe o caminho viável mais próximo; nunca só "não dá".
- **Esforço** (P/M/G + horas aproximadas), **riscos** (o que pode quebrar) e **custos**
  (processamento, financeiro — APIs, assets pesados, build).
RETORNO: markdown estruturado (vira analise_eng.md), itens ENG-1..ENG-n, referenciando os
mesmos trechos da transcrição.
=== TRANSCRIÇÃO NORMALIZADA ===
{TRANSCRICAO}
```

Salvar os retornos em `analise_ux.md` e `analise_eng.md` na pasta da sessão.

**Custeio honesto (2ª rodada quando preciso):** o eng analisou o *pedido bruto*; itens que o UX
marcou `[AMPLIADO]` têm proposta que o eng **não custeou**. Antes de fechar a proposta, disparar
um follow-up curto do subagente eng **só sobre esses itens ampliados**. Se pular o follow-up por
algum motivo, o campo esforço/risco/custo desses R deve dizer explicitamente
*"estimativa do consolidador — não passou pelo eng"*.

## 5 · CONSOLIDAÇÃO (a sessão principal é o "jarbas consolidador")

Fundir as duas análises numa **proposta numerada** — agrupando pedidos que são a mesma mudança:

```
## R1 · <título curto>
- **Pedido:** "<citação>" [timestamp] (falante)
- **UX:** <essência da leitura UX> (UX-i)
- **Eng:** <essência técnica + trade-off> (ENG-j)
- **Recomendação:** SEGUIR · ADAPTAR (como) · NÃO SEGUIR (por quê)
- **Prós × contras:** …
- **Esforço/risco/custo:** …
```

Regras: conflito UX×Eng → expor os dois lados e recomendar (não esconder a tensão); itens
`[PRODUTO]` vão para a seção separada **"Requisitos de produto (fora da tela)"** com destino
(ex.: o doc de requisitos da jornada do projeto). Salvar como `proposta.md` na pasta da sessão.
Apresentar no chat e terminar SEMPRE com:
**"Aprove por número (ex.: 'R1, R3-R5'), 'todos', ou ajuste o que quiser."**

## 6 · EXECUTAR + RELANÇAR

1. Aplicar **só os aprovados** (edições normais; commit só se Oscar pedir).
2. **Relançar a interface**: comando por projeto no `projetos.md` (server estático já serve os
   arquivos editados → muitas vezes basta recarregar o navegador; iniciar se não estiver rodando).
3. Atualizar `<pasta_revisoes>\backlog.md`: cada R vira uma linha com status —
   `✅ feito · 👍 aprovado-pendente · ❌ rejeitado · ⏸ adiado · 🔁 recorrente` — e a sessão de origem.
4. Convidar: "quando quiser, `/jarbas-revisao` pro próximo ciclo."

## 7 · Modo rápido (`/jarbas-revisao rapido`)

Pular §4–5: entregar a transcrição normalizada + lista de pontos em bullets (sem comitê).
Salvar `transcricao.txt` do mesmo jeito; oferecer rodar o comitê depois sobre ela.
Combina com o fluxo ARQUIVOS: `/jarbas-revisao rapido <arquivos>`.

## 8 · Setup (1ª vez / máquina nova)

1. `python -m venv RAIZ\.venv` — atenção: o `python` global pode ser stub da Windows Store;
   usar um Python real ≥3.10 (o caminho de bootstrap desta máquina está em
   `_jarbas/projetos.md` § *Notas da máquina*).
2. `RAIZ\.venv\Scripts\python.exe -m pip install -r RAIZ\requirements.txt` (~2–4 min).
3. O modelo Whisper `small` baixa ~460 MB no 1º uso (cache HuggingFace, compartilhado entre venvs).

## 9 · Convenções

- **Repo jarbas** (whitelist em `~/.claude/skills/.gitignore`) rastreia este skill; `.venv/`,
  `state/` e `gravacoes/` ficam fora pelo `.gitignore` local da pasta.
- **Saída dupla / anti-contaminação**: o MÉTODO é este skill (agnóstico — nenhum nome ou caminho
  de projeto no corpo); a APLICAÇÃO (transcrições, análises, propostas, backlog, **glossário do
  projeto**) vive na pasta de revisões do projeto, alcançada **só** via `projetos.md`.
- Privacidade: gravação e transcrição são locais ($0, nada sai da máquina); áudio com terceiros
  segue a regra das entrevistas (não versionar).
- Fim de sessão: rodar `_jarbas/retro.md`.
