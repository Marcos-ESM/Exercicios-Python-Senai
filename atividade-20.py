

file = open('arquivo.txt','r') # abre o arquivo de texto, 'r' é para somente ler 

soma = 0 
divisor= 0 

for l in file: # para cada caractere em file 
    l = l.replace(" ","") # remove os espaços em branco 
    l = list(l) # transforma l em uma lista 
    try:# em caso de quebras de linhas o comando nao vai conseguir transformar em número 
        for n in l: # para cada número na lista l 
            n = float(n) # transforma em número 
            soma += n # adiciona os números para nossa variável de soma, somando. 
            divisor += 1 # para cada número adiciona 1 ao divisor. 
    except:# se nao conseguir executar o comando, pula para o próximo caractere 
        continue 

try: # tenta fazer a divisão 
    media = soma / divisor # calcula a média 
    media = int(media) 
    print(media) # imprime a media na tela 
except: 
    print("") 
    print("Não há números na lista") # se não tiver média, imprime na tela que não há números na lista 

file.close() #fecha o arquivo 

