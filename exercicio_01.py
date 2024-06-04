# Exercício 1
# Crie um programa que o usuário digita o seu nome e retorna o número de caracteres
# Exemplo:
    # Digite o seu nome: Luciano
    # 7
# A função input tem o objetivo de solicitar via teclado, informações do usuário, sendo o retorno padrão em String
# É utilizada a função *len* de python, é um função embutida que tem o objetivo de retornar o número de itens em um objeto.
# Desta forma, uma da função len consegue contar o número de caracteres em uma String, que é o retorno padrão da função input

nome = input("Digite o seu nome: ")
print("O número de caracteres no seu nome é:",len(nome))


