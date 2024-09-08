CONSTANTE_BONUS = 1000

# 1) Solicitar ao usuário que digite o seu nome

name_user = input("Digite o seu nome: ")

# 2) Solicite ao usuário que digite o valor do seu salário

wage_user = float(input("Digiste o seu salário: "))

# 3) Solicite ao usuário que digite o bônus

bonus_user = float(input("Digite o seu bonus: "))


# 4) Calcule o valor final do bônus

bonus_value = CONSTANTE_BONUS + wage_user * (bonus_user)

# 5) Imprime a mensagem personalizada incluindo nome do usuário, salário e bônus

print (f"{name_user}, o valor do seu bônus é de: {bonus_value}")

# Sempre que quiseremos contatenar variáveis com texto utilizamo o f string que são chamadas de 'strings literais formatadas'.
# Para utilizar o f string é necessário iniciar com a letra f e chaves para realizar a interpolação das expressões.