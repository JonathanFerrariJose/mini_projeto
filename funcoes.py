# funcoes.py
# Versão simples: funções pequenas e fáceis de entender.

import csv
import re
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def ler_csv(caminho):
    """Lê o CSV e retorna lista de dicionários (cada linha)."""
    with open(caminho, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        linhas = []
        for l in leitor:
            linhas.append(dict(l))
        return linhas

def limpar_categoria(texto):
    """Limpa categoria: tira espaços, deixa minúscula, remove pontuação.
       Se ficar vazio, retorna 'sem categoria'."""
    if texto is None:
        return "sem categoria"
    s = str(texto).strip().lower()
    # remove tudo que não for letra ou espaço
    s = re.sub(r"[^a-z\s]", "", s)
    s = " ".join(s.split())  # compacta espaços
    if s == "":
        return "sem categoria"
    return s

def padronizar_canal(texto):
    """Padroniza canal para Mercado / Loja física / Web. Retorna None se não reconhecer."""
    if texto is None:
        return None
    s = str(texto).strip().lower()
    if "mercado" in s:
        return "Mercado"
    if "loja" in s:
        return "Loja física"
    if "web" in s:
        return "Web"
    return None

def validar_quantidade(texto):
    """Tenta converter para int e verifica > 0. Retorna (ok, valor)."""
    try:
        v = int(str(texto).strip())
        return (v > 0, v)
    except:
        return (False, None)

def validar_preco(texto):
    """Tenta converter para float e verifica >= 0. Retorna (ok, valor)."""
    try:
        v = float(str(texto).strip())
        return (v >= 0, v)
    except:
        return (False, None)

def parse_data(texto):
    """Tenta converter data_venda para datetime. Retorna objeto datetime ou None."""
    if texto is None or str(texto).strip() == "":
        return None
    try:
        return datetime.strptime(str(texto).strip(), DATE_FORMAT)
    except:
        return None
