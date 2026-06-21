# Aprendizado sobre o Oscar (perfil do aprendiz)

> Camada **agnóstica**: quem Oscar é como aprendiz, independente de projeto. Os logs de
> sessão específicos do casei vivem em `memory\casei\aprendizados_casei.md`.

## Perfil

- **Nome:** Oscar
- **Nível estimado:** intermediário-avançado em arquitetura de software (evoluiu rápido —
  sólido em dados, ganhando vocabulário estrutural)
- **Cargo:** Engenheiro de Analytics — Nubank
- **Foco principal:** Engenharia de Software aplicada + Agentic AI; agora também UX/design.

## Contexto

- Trabalha no Nubank — ambiente de engenharia de alto nível.
- Já usa agentic AI no dia a dia (Claude Code / Cursor).
- Background forte em dados: SQL, Python analítico, pandas, pipelines.
- **Gap principal histórico:** arquitetura de software — conceitos estruturais de
  escalabilidade/expansibilidade (vem fechando rápido).
- **Objetivo declarado:** prototipar e colocar em produção projetos próprios com Claude Code,
  escaláveis e expansíveis, sem precisar do rigor de um dev de profissão.
- Aprende rápido, ótima intuição arquitetural latente, responde muito bem a provocações.
- **Outro projeto real — Exodia:** tool interna de agentic AI (múltiplas skills analíticas,
  usada por BAs) no Nubank; Oscar atua como consultor. (Se virar trabalho recorrente aqui,
  ganha pasta própria em `projetos.md`.)

## Conceitos cobertos (entendimento agnóstico)

> Detalhe dos conceitos ancorados em código do casei está em `memory\casei\aprendizados_casei.md`.

- **Evals / avaliação de agentes** (2026-05-26, *bom*): 3 eixos (satisfação / output / processo);
  3 camadas (durante o fluxo / ao final / LLM-as-a-judge); começar leve pra não criar atrito.
  *Gap:* ainda não montou um LLM-as-a-judge na prática.
- **Logging / observabilidade leve (JSONL)** (2026-05-26, *sólido*): append-only, schema fixo de
  eventos, `**kwargs` pra campos opcionais, caminho crítico nunca depende de sistema externo.
- **Princípios de arquitetura** (2026-05-26, *sólido*): separação de responsabilidades,
  isolamento de dependências, DRY ("cada decisão importante num único lugar"), camadas.
- **Schema evolution / contratos de dados** (2026-05-26, *bom*): JSON é schema-on-read;
  adicionar campo é seguro, renomear/remover é perigoso; backward/forward compat; Pydantic
  como "Avro do código Python".
- **Skills no Claude Code** (2026-05-26→, *em andamento→sólido*): estrutura `SKILL.md` +
  `references/`; `description` é o contrato de carregamento; persistência em disco fecha o
  ciclo aprende→registra→consulta.
- **Série "Arquitetura de Software" (8 temas, A→H)** (2026-06-07, *sólido a muito sólido*):
  camadas, contratos, dependency injection, testabilidade, error handling, observabilidade,
  AI engineering, schema migrations. Aplicada ao casei — log detalhado no projeto.
- **Arco "localhost → SaaS multi-inquilino na nuvem"** (2026-06-14, *bom*): multi-tenancy e
  propagação de contexto; AuthN vs AuthZ; SQLite vs Postgres; capacidade/sizing (usuários →
  DAU → simultâneos → req/s); migração por sinal, não por número.
- **UX / pesquisa de produto** (2026-06-20, *bom→sólido*): proto-persona vs persona; entrevista de
  descoberta (comportamental > opinião, viés do entrevistador); journey map (anatomia, journey vs
  flow vs blueprint, curva emocional = prioriza+protege+empatia, momentos que importam, swimlane de
  trilhos paralelos + loops); estilos de decisão (maximizador↔satisficer, analítico↔intuitivo,
  driver) e segmentação por eixos ortogonais + MECE-dentro-do-eixo + poda (discrimina ∧ acionável).

## Dúvidas recorrentes / padrões de erro a observar

- **Inverte "custo/raridade" com "prioridade de cobertura"** (testes, cache): apareceu em
  Testabilidade e em Cache (2026-06-07) e de novo em concorrência (2026-06-14, "alcançar
  mecanismo pesado quando o certo é escolher a ferramenta certa"). A pergunta certa é *"o que
  quebra silenciosamente e tem maior raio de impacto"*, não *"o que é mais caro de rodar"*.
  **Nomear o padrão pra ele** ajuda a autocorrigir. Observar se some de vez.
- Em fluxos de erro, tende a pensar "de cima pra baixo" — reforçar: *cada camada trata o erro
  da camada imediatamente abaixo*.

## Próximos tópicos (genéricos)

- **Pydantic na prática** — modelar contratos reais (gancho aberto).
- **Exceções tipadas + falha parcial** — hierarquia de exceções + loop com lista de erros.
- **LLM-as-a-judge na prática** — montar o prompt do juiz e validar o juiz (gancho antigo).
- (Itens amarrados ao plano do casei ficam em `memory\casei\`.)

## Notas do Professor (Jarbas)

- **Formato que funciona melhor:** dar **duas opções pra comparar e justificar** em vez de
  pergunta aberta — gera raciocínio mais rico e visível. Usar muito.
- **Condução:** visão geral → aprofundamento tema a tema, confirmando em cada ponto.
- Ele **converte aprendizado em ação na hora** — quer saída prática e fechar o ciclo num
  artefato concreto (plano, doc, código). Aprende fazendo.
- Opta consistentemente pela **maturidade quando o custo é mostrado junto** — não precisa ser
  empurrado; mostre o tradeoff e ele escolhe bem.
- **Mostrar o artefato rodando expõe gaps** que nenhuma descrição pega — quando possível,
  subir/demonstrar antes de discutir no abstrato.
- **Colaboração/versionamento é driver de decisão** (2026-06-18): escolheu versionar tudo em git
  pra compartilhar com o sócio — skills do Jarbas em repo privado, artefatos do casei dentro do
  repo. "Onde mora a coisa" ele decide por compartilhamento, não por conveniência de carregamento.
- **Prefere enxuto (anti-bloat):** corta escopo na hora (ex.: persona+UI em vez de 4; vetou skills
  `forge-*` vazias). Propor o mínimo viável primeiro, deixar graduar com o uso.
- **Trabalha em janelas paralelas** — pode commitar/editar arquivos por fora durante a sessão.
  Usar staging cirúrgico (`add` por arquivo, nunca `add -A`) e checar `git status` antes de commitar.
- **Pega buracos de método/estrutura, não só de conteúdo** (UX, 2026-06-20): apontou "faltou a
  jornada", "focou demais nos fornecedores = viés de produto", "os 2 perfis são MECE?", "abre o
  leque". Pensa em *frameworks* (MECE, eixos) — herança de analytics. Empurra evidência-primeiro
  (não cravar antes da entrevista). Render visual (curva/SVG) aterrissa o abstrato pra ele.
