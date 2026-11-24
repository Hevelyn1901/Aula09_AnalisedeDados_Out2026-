produto1 = {}    # Dicionário vazio

produto = {
    'nome': 'Notebook',
    'preco': 3500.80,
    'marca': 'Lenovo'
}

# type(produto)
print(produto)  # todas as chaves e valores

print(produto['nome'])   #chave nome
print(produto['preco'])   #chave preço

# Alterando o valor
produto['marca'] = 'Positivo'
print(produto['marca'])

# Adicionando Chaves
produto['tela'] = '18 polegadas"'
# print(produto['tela'])

# deletando uma chave
del produto['marca']
print(produto)

print(produto.keys()) # chaves
print(produto.values()) # valores
print(produto.items()) # itens
