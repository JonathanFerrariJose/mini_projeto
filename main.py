# main_pandas.py
# Versão com Pandas que lê o CSV, aplica regras e gera REPORT.md

import pandas as pd
import re
from datetime import datetime

CSV = "halloween_vendas.csv"
REPORT = "REPORT.md"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def limpar_categoria(s):
    if pd.isna(s) or str(s).strip() == "":
        return "sem categoria"
    t = str(s).strip().lower()
    t = re.sub(r"[^a-z\s]", "", t)
    t = " ".join(t.split())
    return t if t else "sem categoria"

def padronizar_canal(s):
    if pd.isna(s):
        return None
    t = str(s).strip().lower()
    if "mercado" in t:
        return "Mercado"
    if "loja" in t:
        return "Loja física"
    if "web" in t:
        return "Web"
    return None

def main():
    df = pd.read_csv(CSV, encoding="utf-8")

    # Limpeza de categoria
    df["categoria_limpa"] = df["categoria"].apply(limpar_categoria)

    # Canal
    df["canal_pad"] = df["canal_venda"].apply(padronizar_canal)

    # Quantidade e preço
    df["quantidade_num"] = pd.to_numeric(df["quantidade"], errors="coerce")
    df["quantidade_ok"] = df["quantidade_num"].apply(lambda x: not pd.isna(x) and x > 0)
    df["preco_num"] = pd.to_numeric(df["preco_unitario"], errors="coerce")
    df["preco_ok"] = df["preco_num"].apply(lambda x: not pd.isna(x) and x >= 0)

    # Datas
    df["data_venda_dt"] = pd.to_datetime(df["data_venda"], format=DATE_FORMAT, errors="coerce")
    df["periodo"] = df["data_venda_dt"].dt.strftime("%Y-%m")

    # Regras de negócio
    sem_entrega = df["data_entrega"].isna() | (df["data_entrega"].astype(str).str.strip() == "")
    cancelado = df["status_pedido"].astype(str).str.strip().str.lower() == "cancelado"
    df["cancelado_sem_entrega"] = sem_entrega & cancelado
    df["sem_entrega_outro"] = sem_entrega & (~cancelado)

    # Contagens
    problemas = {
        "categoria_vazia": int((df["categoria"].isna() | (df["categoria"].astype(str).str.strip() == "")).sum()),
        "quantidade_invalida": int((~df["quantidade_ok"]).sum()),
        "preco_invalido_ou_ausente": int((~df["preco_ok"]).sum()),
        "data_venda_invalida_ou_vazia": int(df["data_venda_dt"].isna().sum()),
        "sem_data_entrega": int(sem_entrega.sum())
    }

    # Exemplos contra a hipótese
    exemplos = df[df["sem_entrega_outro"]].head(3)

    # Descobertas
    canal_counts = df["canal_pad"].value_counts(dropna=True)
    periodo_counts = df["periodo"].value_counts(dropna=True).sort_index()

    # Geração do REPORT.md
    linhas = []
    linhas.append("# REPORT - Mini Projeto Festa em Cena (versão Pandas)\n\n")
    linhas.append(f"Total de linhas lidas: {len(df)}\n")
    linhas.append("## Problemas por campo\n")
    for k,v in problemas.items():
        linhas.append(f"- {k}: {v}\n")

    linhas.append("\n## Contagem por canal\n")
    for canal, cnt in canal_counts.items():
        linhas.append(f"- {canal}: {cnt}\n")

    linhas.append("\n## Contagem por período (ano-mês)\n")
    for periodo, cnt in periodo_counts.items():
        linhas.append(f"- {periodo}: {cnt}\n")

    linhas.append("\n## Hipótese sobre entregas\n")
    if exemplos.empty:
        linhas.append("Todos os registros sem data_entrega têm status Cancelado (hipótese verdadeira).\n")
    else:
        linhas.append("Existem registros sem data_entrega com status diferente de Cancelado (hipótese falsa). Exemplos:\n")
        for _, ex in exemplos.iterrows():
            linhas.append(f"- pedido_id={ex['pedido_id']}, status={ex['status_pedido']}, canal={ex['canal_venda']}, data_venda={ex['data_venda']}\n")

    linhas.append("\n## Duas descobertas\n")
    if not canal_counts.empty:
        maior_canal = canal_counts.idxmax()
        linhas.append(f"1) Canal com mais registros: {maior_canal} ({canal_counts.max()} pedidos). Limitação: não é receita.\n")
    if not periodo_counts.empty:
        maior_periodo = periodo_counts.idxmax()
        linhas.append(f"2) Período com mais registros: {maior_periodo} ({periodo_counts.max()} pedidos). Limitação: datas inválidas foram excluídas.\n")

    with open(REPORT, "w", encoding="utf-8") as f:
        f.writelines(linhas)

    print("REPORT.md gerado com sucesso.")

if __name__ == "__main__":
    main()

