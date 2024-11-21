lista = [ ] # criação de lista 

while True: # inicia um loop 
    number = input('Digite seus números e digite n para parar:  ') # pede um número ao usuário
    if number == 'n': # se o usuário digitar 'n' o loop para 
        break
    else:
        lista.append(number) # caso contrário, adiciona o número para a lista 
    

print("sua lista é: " , lista) # imprime a lista do usuário 

soma = 0 # variável para somar os números 

nums =(int(s) for s in lista)  # transforma os números da lista em inteiros 

for i in nums: # para cada número em 'nums' (variável que abrigou números da lista inteiros) 
    soma += i  # vai somando os números na variável soma 

print("A soma dos números é: ",soma) #imprime na tela a soma dos números da lista do usuário 

