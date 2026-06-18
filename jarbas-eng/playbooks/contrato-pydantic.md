# Playbook — introduzir um contrato Pydantic onde havia dict solto

1. **Mapear a forma real do dado HOJE** (rodar, inspecionar): campos que às vezes são None,
   às vezes str, etc. Modelar a realidade, não o ideal.
2. **Modelar o `BaseModel`** refletindo isso — incluindo opcionais e defaults.
3. **Validar contra dados reais existentes ANTES de plugar** — pode revelar inconsistências
   silenciosas que já existem.
4. **Plugar na fronteira:** quem produz passa a retornar o modelo; quem consome passa a recebê-lo.

**Conceito:** contratos (Tema B). Pydantic valida em runtime — o erro aparece na fronteira, não
três camadas adiante. Cuidado com campos polimórficos → discriminated unions.

*Exemplo real (casei):* o campo `alvo` do critério (polimórfico) é o caso clássico de
discriminated union. Detalhes no projeto.

## Refino
Ao terminar de usar este playbook, avalie se ele deve melhorar (passo, exemplo) e leve ao /retro.
