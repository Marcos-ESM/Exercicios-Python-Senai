
number=[] 
for num in range(1,101): # para cada número de 1 a 100 
    number.append(num) # o número é adicionado à lista 


for num in number: # para cada número da lista 'number'
    if num == 2: # se o número for 2, imprime na tela que é primo 
        print("2 é primo") 
    if num == 1:# se o número for 1, imprime na tela que é primo 
        print('1 é primo')
    if num > 1: # se o número for maior que 1
        for i in range(2, num): # para cada número de 2 até o número que tá no loop da lista 
            if num % i == 0: # se o número tiver restante 0 com a divisão por 2 
                print(num, 'não é primo')# então ele não é primo 
                break# para o loop 
            else:
                print(num, 'é primo')#caso ele nao tenha resto 0, então ele é primo 
                break #para o loop 
    print("")#espaço em branco 
