
frase = input("Digite uma frase: ") # pede ao usuário uma frase 

lista=[] 
for l in frase: # para cada letra na frase 
    lista.insert(0,l) # insere no início da lista porém, cada letra empurra a outra para a direita, logo a primeira letra será empurrada pela segunda e assim vai 

frase_final= '' #cria uma variável com uma string vazia 

for n in lista: # para cada letra da lista 
    frase_final += n  # adiciona para a variável 'frase_final' 

print(frase_final) 
