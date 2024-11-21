#jogo da forca 
import random 

lista = [
    "casa", "carro", "gato", "livro", "janela", 
    "cachorro", "mesa", "cadeira", "cidade", "computador", 
    "escola", "telefone", "porta", "flor", "rio", 
    "montanha", "estrada", "mercado", "praia", "ferramenta"
]
  
palavra = random.choice(lista) # escolhe uma palavra aleatória da lista 
chances = 10 # define o número de chances 
chutes= [] # lista de letras que já foram 

while True:
    chute = input("Digite sua letra: ") #tentativa do usuário de tentar adivinhar a palavra
    chutes.append(chute.lower())  # adiciona a tentativa garantindo que a letra seja minúscula 
    if chute not in palavra: # se a letra chutada nao estiver na palavra 
        chances-=1 # perde uma chance 
    for letter in palavra: # para cada letra da palavra 
        if letter.lower() in chutes: # se a letra minúscula estiver em chutes 
            print(letter, end=" ") # imprime a letra sem quebra de linhas 
        else:
            print('_', end=" ") # caso contrário imprime um '_' 
    print("") # cria um espaço em branco 
    print(f"Você tem {chances} chances.") #imprime as chances que o usuário tem 
    print(f"Letras que já foram: {chutes}") # imprime as letras que já foram 

    


    ganhou = True # ganhou é definido como True 
    for letter in palavra: # para cada letra na palavra 
        if letter not in chutes: # se a letra da palavra nao estiver em chutes do usuário
            ganhou=False # então usuário não ganhou, logo ganhou fica falso, porém caso contrário ganhou se mantém True 
    

    if chances == 0 or ganhou: # se acabar as chances ou o usuário acertar a palavra o loop para 
        break

if ganhou: 
    print(f"Parabéns, você ganhou! a palavra era {palavra}.") # caso ganhe imprime que ganhou 
else:
    print(f"Você perdeu! a palavra era {palavra}.")# caso perca imprime que perdeu 


    
    



    