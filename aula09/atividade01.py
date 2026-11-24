contatos = []

for i in range(3):
    print(f'\ncliente {i+1}')
    cliente = {}

    cliente['nome'] = input('Informe o nome completo: ')
    cliente['email'] = input('Informe o email: ')
    cliente['telefone'] = int(input('Informe o telefone: '))

    contatos.append(cliente)

for elemento in contatos:
    print(f'\nNome: {elemento['nome']}')
    print(f'Telefone: {elemento['telefone']}')
    print(f'Email: {elemento['email']}')





    