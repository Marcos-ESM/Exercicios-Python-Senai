frase=input("Digite uma frase: ") # pede uma frase para o usuário 

count=0    # variável contador começando do zero 
vogais=" "  # variável com duas aspas, uma string vazia 


for i in frase.upper(): # para cada letra em 'frase.upper()'( serve para deixar todas as letras maiúsculas) :
    if i in 'AEIOU': # se tiver em 'AEIOU' 
        count+=1  # contador + 1 
        vogais+= i  # adiciona as vogais na variável vogais 
    else: 
        continue  # caso contrário ignora 

print("A quantidade de vogais existentes são: ", count) # imprime a quantidade de vogais na tela 
print("As vogais são: " , vogais)  # imprime quais vogais existem na frase
    
    
        

 
