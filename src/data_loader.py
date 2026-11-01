import pandas as pd

# 1. Carregamento dos dados em memória
# customers = pd.read_csv('customers.csv')
# products = pd.read_csv('products.csv')
# orders = pd.read_csv('orders.csv')
# order_items = pd.read_csv('order_items.csv')
# categories = pd.read_csv('categories.csv')

# 2. Tratamento rápido de nulos nas colunas críticas
# Ajuste 'preco' e 'estoque' para os nomes reais das colunas no seu CSV
products['preco'] = products['preco'].fillna(0) 
products['estoque'] = products['estoque'].fillna(0)

# 3. Conexões (Merges) baseadas nas chaves primárias
# Une os itens aos pedidos
df_pedidos = pd.merge(orders, order_items, on='order_id', how='inner')

# Adiciona os detalhes dos produtos e categorias
df_vendas = pd.merge(df_pedidos, products, on='product_id', how='left')
df_vendas = pd.merge(df_vendas, categories, on='category_id', how='left')

# Consolida com os dados dos clientes
df_completo = pd.merge(df_vendas, customers, on='customer_id', how='left')

print(df_completo.head())