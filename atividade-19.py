


clientes={} # cria um dicionário 


def adicionar(): #função para adicionar clientes 
    idcliente = input('Digite o id do cliente que deseja adicionar: ') # pede ao usuário um número para ser o id do cliente 

    if idcliente in clientes: # caso o id já esteja na biblioteca 
        print("Este cliente já está cadastrado.") # imprime na tela que já tá cadastrado o cliente 

    
    nome = input('Digite o nome do cliente que deseja adiocionar: ') # pede o nome do cliente para adicionar 
    email = input('Digite o email do cliente que deseja adicionar: ') # pede o email do cliente para adicionar 

    clientes[idcliente] ={'Nome':nome, 'Email': email} # clientes[idcliente] vai ser onde vai entrar as informações, no caso o nome e email 

def visualizar(): # função para visualizar os clientes cadastrados 
    if not clientes: # caso não tenha clientes 
        print("") # espaço em branco
        print('Nenhum cliente foi cadastrado.') # imprime que o cliente já está cadastrado 
    
    for chave,valor in clientes.items(): # para chave, valor em clientes.items()( função que exibe os pares chave - valor do dicionário )
        idcliente = chave # define idcliente como chave 
        nome = valor['Nome'] # define nome como o valor Nome especificado 
        email = valor['Email'] # define email como o valor Email especificado 

        print('ID: ', idcliente, 'Nome:', nome, 'Email:', email)  # imprime as informações de cada chave, valor que tiver no dicionário clientes 

def remover(): #função que remove clientes 
    idcliente = input("Digite o id do cliente que deseja remover: ") #pede ao usuário para que digite o id do cliente que deseja remover 

    if idcliente not in clientes: # se o id do cliente nao estiver em clientes 
        print("Esse usário não existe.") # imprime isso na tela 
    else:
        del clientes[idcliente] # caso esteja, remove o cliente do dicionário 

def tela_inicial():# função que cria um menu para deixar mais específico o que o usuário deseja 
    while True:# cria um loop 
        print("") #espaço em branco
        #imprime essas informações na tela 
        print("TELA INICIAL") 
        print("Digite 1 se deseja visualizar os clientes existentes.")
        print("Digite 2 se deseja adicionar um cliente.") 
        print("Digite 3 se deseja remover um cliente.")
        print("Digite 4 se deseja sair.") 
        print("") 

        n = input("digite um número: ") # pede o número que o usuário quiser para realizar as ações

        if n == '1':# se o número for 1, chama a função visualizar 
            visualizar() 
        if n == '2':
            adicionar()# se o número for 2, chama a função adicionar
        if n == '3':
            remover() #se o número for 3, chama a função remover 
        if n == '4':
            break # se o número for 4, sai do loop. 


tela_inicial() 