
# criar função ordenar sem usar a função sort()

def ordenar(lista): # cria a função 
    for indice in range(1 , len(lista)): # indice vai ser gerado para cada número num intervalo de 1 até o cumprimento da lista
        numero = lista[indice]  # número vai ser = ao número que abriga no indice da lista 
        i = indice  # i = indice para facilitar o código 

        while i > 0 and numero < lista[i-1]: # cria um loop com os requisitos do indice ser maior que 0 e do número ser menor que o número anterior na lista 
            lista[i] = lista[i-1]   # no local do número atual, entra o número anterior a ele 
            i-=1  # indice menos um para poder alterar o valor do número anterior ao que estavamos 
            lista[i] = numero  # move o número para esse indice da lista ( no caso para o local do outro número maior que ele) 
            
# o loop só para quando i = 0 e quando o número anterior ao atual, não é maior que o número atual 
    print(lista)  # imprime a lista na tela 

 #     0  1 2 3 4 5 6 7 8 9 
lista=[10,8,9,7,6,5,4,3,2,8]
 
ordenar(lista) 




