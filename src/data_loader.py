import pandas as pd
import os
import PyPDF2

caminho_atual = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(caminho_atual, '..', 'data')

# 1. Declara a variável produtos_df
caminho_produtos = os.path.join(base_dir, 'desafio_tecnico_ai_eng - products.csv')
produtos_df = pd.read_csv(caminho_produtos)

if 'preco' in produtos_df.columns and 'estoque' in produtos_df.columns:
    produtos_df['preco'] = produtos_df['preco'].fillna(0)
    produtos_df['estoque'] = produtos_df['estoque'].fillna(0)
elif 'price' in produtos_df.columns and 'stock' in produtos_df.columns:
    produtos_df['price'] = produtos_df['price'].fillna(0)
    produtos_df['stock'] = produtos_df['stock'].fillna(0)

# 2. Declara a variável texto_politicas
def carregar_politicas():
    caminho_pdf = os.path.join(base_dir, 'políticas_da_loja.pdf')
    texto = ""
    try:
        with open(caminho_pdf, "rb") as f:
            leitor = PyPDF2.PdfReader(f)
            for pagina in leitor.pages:
                texto += pagina.extract_text()
        return texto
    except Exception:
        return "Políticas não encontradas."

texto_politicas = carregar_politicas()