import random # importa o módulo random 

resultados = [] # cria uma lista

while True:#inicia um loop 
    n = input("Caso deseje rolar o dado digite 'y', se não digite 'n': ") # pergunta ao usuário se ele deseja rodar o dado 
    if n == 'y': # se o usuário digitar y 
        l = random.randint(1,6) # escolhe um número entre 1 e 6 podendo ser 1 e 6 também 
        resultados.append(l)  # adiciona os números a nossa lista resultados 
        print("O número que caiu foi: ", l ) # imprime o número que caiu para o usuário 
    else:
        break # se o usuário nao digitar y o loop para 

    

print('Seus resultados foram: ', resultados ) # imprime os resultados de todas as jogadas do usuário



