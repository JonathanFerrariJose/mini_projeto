# REPORT - Mini Projeto Festa em Cena (versão Pandas)

Total de linhas lidas: 1500
## Problemas por campo
- categoria_vazia: 18
- quantidade_invalida: 7
- preco_invalido_ou_ausente: 12
- data_venda_invalida_ou_vazia: 4
- sem_data_entrega: 143

## Contagem por canal
- Web: 666
- Loja física: 551
- Mercado: 283

## Contagem por período (ano-mês)
- 2024-08: 77
- 2024-09: 104
- 2024-10: 393
- 2024-11: 174
- 2025-08: 62
- 2025-09: 94
- 2025-10: 410
- 2025-11: 182

## Hipótese sobre entregas
Existem registros sem data_entrega com status diferente de Cancelado (hipótese falsa). Exemplos:
- pedido_id=1170, status=Concluído, canal=Web, data_venda=2025-08-19 22:20:19
- pedido_id=990, status=Concluído, canal= web , data_venda=2025-10-13 20:00:16
- pedido_id=740, status=Concluído, canal=Web, data_venda=data_invalida

## Duas descobertas
1) Canal com mais registros: Web (666 pedidos). Limitação: não é receita.
2) Período com mais registros: 2025-10 (410 pedidos). Limitação: datas inválidas foram excluídas.
