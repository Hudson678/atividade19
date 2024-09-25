# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

num = int(input("insira um numero para exibir seu fatorial: "))

if num == 0:
    print ("o fatorial desse numero é 1")
else: 
    fatorial = 1 
    for n in range (1, num + 1):
        fatorial *= n
    print (f"o fatorial de {num} é {fatorial}")






