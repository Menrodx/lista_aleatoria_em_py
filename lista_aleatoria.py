import random
qtde_nums = int(input("Informe a quantidade de números que você deseja criar: "))
lista_deNumeros=[]
i=0
while qtde_nums>i:    
    numero_aleatorio = random.randint(0,10)
    lista_deNumeros.append(numero_aleatorio)
    i+=1

print("A lista criada é: {}".format(lista_deNumeros))

