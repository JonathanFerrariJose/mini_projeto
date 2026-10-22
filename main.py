# main_pandas.py
# Versão alternativa com pandas (opcional). Requer pandas instalado.
import re
import pandas as pd
from datetime import datetime

CSV = "halloween_vendas.csv"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def limpar_categoria_pd(s):
    if pd.isna(s) or str(s).strip() == "":
        return "sem categoria"
    t = str(s).strip().lower()
    t = re.sub(r"[^a-z\s]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t if t else "sem categoria"

def padronizar_canal_pd(s):
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
    df["categoria_limpa"] = df["categoria"].apply(limpar_categoria_pd)
    df["canal_padronizado"] = df["canal_venda"].apply(padronizar_canal_pd)
    df["quantidade_num"] = pd.to_numeric(df["quantidade"], errors="coerce")
    df["quantidade_ok"] = df["quantidade_num"].apply(lambda x: (not pd.isna(x)) and (int(x) > 0))
    df["preco_unitario_num"] = pd.to_numeric(df["preco_unitario"], errors="coerce")
    df["preco_ok"] = df["preco_unitario_num"].apply(lambda x: (not pd.isna(x)) and (x >= 0))
    df["data_venda_dt"] = pd.to_datetime(df["data_venda"], format=DATE_FORMAT, errors="coerce")
    df["periodo"] = df["data_venda_dt"].dt.strftime("%Y-%m")
    sem_entrega = df["data_entrega"].isna() | (df["data_entrega"].astype(str).str.strip() == "")
    cancelado = df["status_pedido"].astype(str).str.strip().str.lower() == "cancelado"
    df["cancelado_sem_entrega"] = sem_entrega & cancelado
    df["sem_entrega_outro_status"] = sem_entrega & (~cancelado)

    print("Total linhas:", len(df))
    print("Problemas por campo:")
    print(" - categoria_vazia:", int((df["categoria"].isna() | (df["categoria"].astype(str).str.strip() == "")).sum()))
    print(" - quantidade_invalida:", int((~df["quantidade_ok"]).sum()))
    print(" - preco_invalido_ou_ausente:", int((~df["preco_ok"]).sum()))
    print(" - data_venda_invalida_ou_vazia:", int(df["data_venda_dt"].isna().sum()))
    print(" - sem_data_entrega:", int(sem_entrega.sum()))
    print("\nPedidos por canal (reconhecidos):")
    print(df["canal_padronizado"].value_counts(dropna=True))
    print("\nPedidos por periodo (ano-mes):")
    print(df["periodo"].value_counts(dropna=True).sort_index())

    exemplos = df[df["sem_entrega_outro_status"]].head(3)
    if not exemplos.empty:
        print("\nExemplos de pedidos sem data de entrega e status diferente de Cancelado:")
        print(exemplos[["pedido_id", "status_pedido", "canal_venda", "data_venda"]].to_string(index=False))

if __name__ == "__main__":
    main()
