
number = float(input("Digite um número em farenheight para ser convertido: ")) # pede um número em farenheight para o usuário
number_2 = float(input("Digite um número em celsius para ser convertido: "))  # pede um núemro em celcius para o usuário 

celsius= (number-32)/1.8 # transforma o primeiro número em celsius 
farenheight = (number_2*1.8) + 32 # transforma o segundo número em farenheight 


#imprime na tela os números:
print("A temperatura em celsius é: ",celsius )
print("A temperatura em Farenheight é: ",farenheight)




