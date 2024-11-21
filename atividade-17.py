import random 
# variáveis com valores para as senhas 
num = '0123456789'
maius = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
minus = 'abcdefghijklmnopqrstuvwxyz' 
simbolos = '!@#$%¨&*'

print("") #gera um espaço em branco 

#informa o usuário 
print("Se deseja a senha fraca digite um número menor ou igual a 5")
print("Se deseja a senha média digite um número menor ou igual a 9")
print('Se deseja a senha forte digite um número maior que 9')
print("") # gera um espaço em branco 

# pede ao usuário o comprimento que deseja para a senha 
quantidade = input('Digite um número para o tamanho da senha: ')

# transforma quantidade em um valor inteiro 
intquant = int(quantidade) 

dificil = num + maius + minus + simbolos #senhas difíceis tem todas os possiveis caracteres das variáveis juntas 
media = num + maius + minus # senhas médias não terão simbolos mas o restante das variáveis sim 
facil = minus + num # senhas fáceis terão apenas minusculas e numeros 

senha_forte = "".join(random.sample(dificil, intquant)) # a função join junta uma string, a random.sample() transforma em lista e embaralha os valores.
senha_media = "".join(random.sample(media, intquant))
senha_facil = "".join(random.sample(facil, intquant))

if intquant <= 5: # se o comprimento for menor ou igual a 5 a senha vai ser imprimida como fácil 
    print('Senha fraca: ' ,senha_facil) 
else: 
    if intquant <= 9: # se o comprimento for menor ou igual a 9 a senha vai ser imprimida como média 
        print('Senha média: ' ,senha_media) 

if intquant > 9: # se o comprimento for maior que 9 a senha vai ser imprimida como difícil 
    print('Senha forte: ',senha_forte)





    

    