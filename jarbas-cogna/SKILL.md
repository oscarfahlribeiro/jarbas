---
name: jarbas-cogna
description: Ative quando Oscar mencionar "jarbas cogna", "torre de comando", "atualizar a torre", "regenerar a torre", "cockpit", "rotina do dia", "o que fazer hoje", ou quiser (re)construir a visão navegável do projeto — o cockpit diário (café do dia: onde estamos no plano, frentes abertas, backlog de ações priorizado por tipo/complexidade com prompt pronto de sessão), arquitetura de dados (tabelas, colunas, linhagem), arquitetura de software (superfícies, módulos, chamadas), glossário categorizado, biblioteca de documentos, diário de bordo e gaps docs×commits. É o perfil de COGNIÇÃO da família Jarbas — a ponte entre tudo que acontece no projeto (vibecoding em N sessões) e o consumo humano do Oscar. Mantém artefatos intermediários em JSON dentro do repo e gera uma torre HTML navegável a partir deles. Dois modos: `/jarbas-cogna hoje` re-sintetiza o cockpit (plano.json) cruzando gaps+diário+plano MVP+git; `/jarbas-cogna` faz a ATUALIZAÇÃO INCREMENTAL dos artefatos factuais via git diff contra o commit do manifest — re-extrai SÓ o que mudou, nunca varre o repo inteiro à toa.
---

# Jarbas — cogna (torre de comando do projeto)

Perfil de cognição da família Jarbas: transforma o estado real do projeto em uma **torre
HTML navegável** para consumo humano. Caminhos do projeto ativo: consultar
`_jarbas/projetos.md` § *Cogna*. Voz e postura: `_jarbas/persona.md` (aqui o modo default
é **executor com relatório** — extrai, atualiza, gera, e conta o que mudou; só pergunta em
bifurcação real).

## O que este perfil mantém (por projeto)

Em `<repo>/docs/cogna/`:

| Peça | Papel |
|---|---|
| `fonte/*.json` | Artefatos canônicos: `tabelas` · `usos` · `linhagem` · `modulos` · `superficies` · `servicos` · `glossario` · `docs` · `diario` · `gaps` · **`plano`** (o cockpit diário — aba ☕ Hoje) · **`amostras`** (10 linhas anonimizadas por tabela) · **`areas`** (governança por área — gerado por script varrendo `docs/areas/` a cada geração, NÃO é extraído por LLM; alimenta a aba Áreas e o runtime `/area`). **Contratos de forma: `LEIAME.md` do próprio diretório.** |
| `cogna.config.json` | Mapa artefato → arquivos-fonte (globs) + granularidade de atualização |
| `manifest.json` | Commit/data da última geração — a âncora do incremental |
| `gerar_torre.py` | Montador determinístico (stdlib, $0): JSONs + .md do repo → `torre.html`. Flags: `--consolidar` (funde parciais) · `--amostras` (lê `casei.db` local e reescreve `amostras.json`) |
| `torre_template.html` | O app (abas, busca, glossário clicável, grafo de linhagem, leitor de .md) |
| `torre.html` | **GERADO — nunca editar à mão** |

Divisão de trabalho fixa: **LLM só extrai e resume** (escreve nos JSONs de `fonte/`);
**a montagem é sempre `gerar_torre.py`** (determinística). Nunca editar `torre.html`.

## Fluxo — HOJE (cockpit diário, o mais frequente)

Disparado por `/jarbas-cogna hoje` (ou "cockpit", "rotina", "plano do dia"). Diferente dos
outros: `plano.json` é **síntese analítica**, regerada por inteiro (não é diff de arquivo).

1. **Ler o estado**: `fonte/gaps.json` + `fonte/diario.json` (já extraídos — não re-varrer código),
   `fonte/areas.json` + `docs/areas/*/kpis.json` (governança por área: **roadblock vencido,
   retro armada — ≥3 dores novas ou 30 dias — e KPI fora da meta entram nos alertas do café**),
   `docs/jarbas/plano_mvp_full.md` (roadmap D1–D24) e `plano_evolucao.md`, e o git REAL
   (`git status --porcelain`, `git branch` + último commit por branch, `git log --all -30`).
2. **Ler o `plano.json` anterior** (se existir): preservar ações ainda abertas; as que os
   commits novos resolveram, remover ou rebaixar; manter a numeração estável quando der.
3. **Sintetizar** seguindo o contrato do `LEIAME.md` (§ plano.json v2 — a página Hoje responde
   TRÊS perguntas): `cafe_do_dia` + `marcos` (**Onde estamos?** — a rota D1–D24);
   `acontecendo` (**O que está acontecendo?** — `frentes` SÓ ativas/pausadas/não-integradas
   + encerradas DESDE O ÚLTIMO cockpit, as antigas caem — o diário conta a história; e
   `alertas_areas` de `areas.json`+`kpis.json`: roadblock vencido, KPI fora da meta, retro
   armada, artefato órfão); `acoes` (**O que fazer agora?** — derivadas dos backlogs "Agora"
   das ÁREAS, cada ação com campo `area` OBRIGATÓRIO + tipo 9-MECE, complexidade, prioridade,
   `prompt_sessao` pronto; ação órfã = gap de governança, não categoria). Nomear a TENSÃO
   quando houver. **Gap novo nasce com campo `area`** (dono = gestor; sem dona → Governo).
4. **Pendências do Oscar** (se o projeto tiver o artefato — casei: `fonte/pendencias_oscar.json`,
   contrato no LEIAME do cogna): re-varrer as fontes (backlogs/roadblocks das áreas, ADRs
   propostos, trackers, gaps com dono) e reescrever o JSON — baixar como `"resolvida"` o que
   os commits/decisões fecharam. A seção da aba Hoje envelhece sem isso (criada 2026-07-16).
5. **Gerar**: `python docs/cogna/gerar_torre.py` (a torre lê `plano.json` na aba Hoje).
6. **Relatório a Oscar**: as 3–5 ações recomendadas do dia (id + título), o que mudou desde o
   último cockpit (ações fechadas, frentes que avançaram), e a tensão/foco. Oferecer abrir a torre.

Regras próprias: prioridade ancorada no **plano de trabalho corrente** (hoje = MVP; o que destrava
o próximo marco = alta). Toda ação com lastro (gap/marco/frente/git) — sem inventar trabalho.
`prompt_sessao` autossuficiente (o agente executor lê o CLAUDE.md/mapa, não esta análise).
**PT-BR com acentuação correta** (é leitura diária do Oscar — "próximo/código/árvore", nunca ASCII pelado).
Verificar premissas no código antes de afirmar status (ex.: confirmar se um marco "existe" no repo,
não confiar só no diário) — é o princípio de verificação empírica do Oscar.

## Fluxo padrão — ATUALIZAR (incremental)

1. **Delta**: no repo do projeto —
   `C0 = manifest.json .commit` · `C1 = git rev-parse HEAD` ·
   `git diff --name-only C0..C1` + `git status --porcelain` (não commitado conta como
   mudança, marcado "não commitado" nos resumos). Se `C0 == C1` e status limpo: só
   reportar "torre em dia" e parar.
2. **Roteamento**: cruzar os caminhos alterados com `cogna.config.json → artefatos[*].depende_de`
   (respeitando `excluir_sempre`). Artefato sem arquivo-fonte alterado **não é tocado** —
   esse é o contrato de eficiência do perfil.
3. **Re-extração cirúrgica**, seguindo a `granularidade` de cada artefato afetado:
   - `modulos.json` / `usos.json`: reler SÓ os `.py` alterados; substituir as entradas
     daquele caminho; arquivo novo → entrada nova; deletado → remover entrada.
   - `tabelas.json`: só se `schema.py` mudou — diff de tabelas/colunas, preservando
     resumos de tabelas intactas.
   - `docs.json`: só docs alterados/novos/removidos (resumo_1l + atualizado_em).
   - `diario.json`: **sempre aditivo** — `git log --all --date=short` desde a última data
     registrada; 1 entrada nova por dia com commit; cruzar com `aprendizados_casei.md`;
     nunca reescrever dias antigos.
   - `gaps.json`: revisão leve — commits novos fecham itens? (marcar `"status": "resolvido"`
     com evidência, não deletar) · pendência nova declarada em doc alterado → item novo.
   - `linhagem.json`: só se mudaram módulos que escrevem em tabela ou o próprio schema.
     A aba Dados renderiza cada aresta como **transformação em texto** (via+tipo+resumo) na
     ficha da tabela — o `resumo` de aresta é a explicação interpretada, mantê-lo legível.
   - `tabelas.json` → campo `sensivel`: derivado do domínio (casal/ambar/jade/contas = true);
     ao adicionar tabela nova, marcar antes de gerar amostra.
   - `amostras.json`: **não é diff de arquivo** — regerar com `gerar_torre.py --amostras`
     quando o `schema.py` mudou (colunas novas) ou quando quiser o snapshot de dados atual.
     Lê o `casei.db` local (gitignored); anonimiza conforme `sensivel` (ver LEIAME § amostras).
   - `glossario.json` / `servicos.json`: só se as fontes canônicas deles mudaram. Cada termo
     carrega campos de PROFUNDIDADE (`como_funciona` · `exemplo` · `caracteristicas` p/ persona)
     e `doc_origem` (caminho de um doc de docs.json → a torre mostra "📄 Ler a fonte"). Ao criar
     termo novo, preencher esses campos com lastro no código/doc (fidelidade), não deixar raso.
   Muitos arquivos afetados (>~15)? Paralelizar com subagentes, um por artefato.
4. **Gerar**: `python docs/cogna/gerar_torre.py` (SEM `--consolidar` — consolidar
   sobrescreveria os canônicos com parciais velhos).
5. **Manifest**: atualizar `commit`/`gerado_em`.
6. **Relatório a Oscar**: o que mudou na torre (n itens por artefato), o que foi PULADO por
   não ter mudança (mostrar a economia), destaques dos dias novos do diário, gaps
   abertos/fechados. Oferecer abrir: `start docs/cogna/torre.html` (Windows).

## Fluxo — RECONSTRUIR (extração total)

Só quando Oscar pedir ("reconstruir a torre", "extração total") ou quando o manifest não
existir. Roda os extratores (contratos e escopos em `LEIAME.md` § Contratos) gravando em
`fonte/parciais/`, depois `python docs/cogna/gerar_torre.py --consolidar`. Extração total
usa subagentes paralelos (1 por artefato; módulos divididos por pacote) + 2 verificadores
adversariais (cobertura: toda tabela do schema? todo .py? todo doc? · ligações: referências
cruzadas resolvem?).

## Fluxo — ABRIR / CONSULTAR

"abrir a torre" → `start <repo>/docs/cogna/torre.html`. Pergunta pontual sobre o projeto
("quem escreve na tabela X?") → responder direto dos JSONs de `fonte/` (mais barato que
varrer código; se o manifest estiver velho, avisar e oferecer atualização).

## Regras duras

- **Idioma e altitude**: tudo que vai para os JSONs em PT-BR simples, nível técnico
  intermediário — o leitor é o Oscar, não outra sessão do Claude.
- **Fidelidade**: resumo sem evidência no código/doc/commit não entra. Gap sem evidência
  não entra. Na dúvida, campo `avisos` no manifest, não invenção.
- **Git**: a skill NUNCA commita — gera os arquivos e lista o que mudou; Oscar decide
  (staging cirúrgico, regra do CLAUDE.md do projeto).
- **LGPD**: a torre embute só .md versionados no repo; mídia/transcrição bruta jamais. A
  **amostra de linhas** (`amostras.json`) segue a política de anonimização do LEIAME —
  contato/identidade mascarados em toda tabela, texto livre mascarado nas `sensivel`, scrubber
  de email/telefone a nível de valor. O JSON é commitável; o `casei.db` de origem, NUNCA.
- **Gate de arquitetura do projeto**: cogna documenta, não muda topologia. Se a extração
  revelar violação de princípio (P1–P10) ou drift do mapa do sistema, registrar em
  `gaps.json` e avisar Oscar — quem muda mapa/ADR é o `/jarbas-arquiteto`.
- **Paridade com o mapa vivo**: `mapa_sistema.md` (arquiteto) é a visão de GOVERNANÇA;
  a torre é a visão de CONSUMO. Divergência entre os dois = gap a reportar, nunca
  "corrigir" o mapa por conta própria.
