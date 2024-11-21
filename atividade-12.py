
lista = [] 

while True: #começa um loop 
    numeros = input('Digite seus número e insira "."para parar: ') #pedindo ao usuário os números.
    if '.' in numeros: # se caso o usuário digitar '.' o loop para. 
        break
    lista.append(numeros) # adiciona os números do usuário à lista.

resultado = [] # uma nova lista para inserir os números sem duplicatas

for n in lista: # para cada número da lista 
    if n not in resultado: # caso o número nao esteja na lista 'resultado' adicione à ela 
        resultado.append(n) 
    else:
        continue # caso esteja, ignore.  

print(resultado) #imprimir o resultado na tela 

