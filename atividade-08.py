import random 

while True: #inicia um loop 
    number= random.randint(0,10) #número aleatório de 0 a 10, incluindo 0 e 10 
    number_u = int(input("Digite um número de 0 a 10: " )) # número do usuário de 0 a 10 
    if number_u != number:
        print("O número não é esse. Tente novamente!") # se o número for diferente do número aleatório pertencente à variável 'number'
    else:
        print("O número", number_u, "é o número correto") # se o número for igual ao número aleatório pertencente à variável 'number' 
        break # para o loop e o jogo de adivinhação termina 



