# REPORT - Mini Projeto Festa em Cena

Total de linhas lidas: 1500
Pedidos com algum problema (IDs únicos): 172

## Problemas por campo
- categoria_vazia: 18
- data_venda_invalida_ou_vazia: 4
- preco_invalido_ou_ausente: 12
- quantidade_invalida: 7
- sem_data_entrega: 143

## Limpezas e validações
- Categorias vazias preenchidas: 18
- Categorias não vazias alteradas: 55
- Datas inválidas ou vazias: 4
- Cancelados sem data de entrega: 109
- Sem data de entrega com outros status: 34

## Exemplos (até 3) de pedidos sem data de entrega e status diferente de Cancelado
- pedido_id=1170, status=Concluído, canal='Web', data_venda='2025-08-19 22:20:19'
- pedido_id=990, status=Concluído, canal=' web ', data_venda='2025-10-13 20:00:16'
- pedido_id=740, status=Concluído, canal='Web', data_venda='data_invalida'

## Pedidos por canal (registros com canal reconhecido)
- Loja física: 551
- Mercado: 283
- Web: 666

## Pedidos por período (ano-mês) — apenas datas válidas
- 2024-08: 77
- 2024-09: 104
- 2024-10: 393
- 2024-11: 174
- 2025-08: 62
- 2025-09: 94
- 2025-10: 410
- 2025-11: 182

## Duas descobertas simples
1) Canal com mais registros: Web (666 pedidos). Interpretação: maior volume de registros. Limitação: não é receita.
2) Período com mais registros: 2025-10 (410 pedidos). Interpretação: possível pico sazonal. Limitação: datas inválidas excluídas.
