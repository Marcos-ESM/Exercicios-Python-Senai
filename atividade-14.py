frase = input("Digite uma frase: ") # pede ao usuário uma frase 

if frase == frase[::-1]: # se a frase for igual a ela ao contrário 
    print(f"A frase {frase} é um palíndromo.") # é um palíndromo 
else:
    print(f"A frase {frase} não é um palíndromo.") # caso contrário, não é um palíndromo 