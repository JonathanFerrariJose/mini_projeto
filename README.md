# Mini‑Projeto Avaliativo — Festa em Cena (versão com Pandas)

## Resumo
Este projeto analisa o arquivo `halloween_vendas.csv`, que contém pedidos fictícios de fantasias e acessórios de Halloween.  
O objetivo é limpar os dados, validar regras de negócio e gerar um relatório (`REPORT.md`) com contagens e descobertas.

## Arquivos principais
- `main_pandas.py` — script principal usando **pandas**.
- `halloween_vendas.csv` — base de dados (coloque na mesma pasta).
- `REPORT.md` — relatório gerado automaticamente pelo script.
- `video_script.txt` — roteiro sugerido para o vídeo de apresentação.

## Objetivo do programa
- Organizar e explorar a base.
- Identificar problemas de qualidade (categorias vazias, canais inconsistentes, quantidades inválidas, preços ausentes, datas inválidas).
- Padronizar categorias e canais.
- Validar números e datas.
- Testar a hipótese: todos os registros sem `data_entrega` têm `status_pedido == "Cancelado"`.
- Produzir relatório com contagens por canal e por período.

## Significado de uma linha e de quatro colunas
- **Linha**: representa um pedido de um produto.
- **pedido_id**: identificador único do pedido.
- **categoria**: tipo do produto (ex.: fantasia, acessório).
- **canal_venda**: canal onde o pedido foi registrado (Mercado, Loja física, Web).
- **data_venda**: data e hora da compra no formato `YYYY-MM-DD HH:MM:SS`.

## Regras adotadas
- **Categorias**: `.strip()`, `.lower()`, `re.sub(r"[^a-z\s]", "")`. Se vazio → `"sem categoria"`.
- **Canal**: padronizado para `Mercado`, `Loja física`, `Web`.
- **Quantidade**: inteiro > 0.
- **Preço**: número >= 0.
- **Data venda**: convertida com `pd.to_datetime(..., format="%Y-%m-%d %H:%M:%S")`. Datas inválidas são marcadas.
- **Data entrega vazia**: verificar se `status_pedido == "Cancelado"`. Contraexemplos listados.

## Como executar
1. Instale pandas:
   ```bash
   pip install pandas
