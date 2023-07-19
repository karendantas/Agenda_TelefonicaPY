
#função que adciona um contato no dicionario
def adicionar_contato ():
    contatos={}
    resposta = "s"
    while (resposta != "n"):
        with open('Agenda telefonica.txt','a') as arquivopy:
        
            nome= str(input("Digite seu nome: "))
            telefone = int(input("Digite seu telefone: "))
            contatos["nome"]=nome
            contatos["telefone"]=telefone
                
            #for chaves, valor in contatos.items():
                #print(chaves,valor)

            for n in contatos.values():
                arquivopy.write(str(n)+"\n") #dessa forma o n pega os valores e os escreve na um embaixo do outro no arq
        resposta = str(input("Adicionar outro contato?[s/n]"))       
    return print("O contato de {} e seu numero: {}, foram adicionados a agenda!".format(contatos["nome"], contatos["telefone"]))
           
        
         



#função que le as linhas de um arquivo
def ler_agenda():
    with open ("Agenda telefonica.txt", 'r') as arquivopy:
        linhas=arquivopy.readlines() #variavel linhas recebe funcao que le as linhas do arquivo
        for lines in linhas:
         print(lines)
    

#função que pega as linhas do arquivo o transforma em um dicionario
def pegar_linhas(list):
    listanome=[]
    listtel=[]
    with open ("Agenda telefonica.txt", "r") as arquipy:
        linhas = arquipy.readlines()
        
        for i in range(1,100):
            if(i%2!=0):
                listanome =linhas
            elif(i%2==0):
                
                listtel = linhas
            
            
    
            
        print(listanome)
        print(listtel)
       


def procurar_numero():
    contatos={}
    pegar_linhas(contatos)
    procura = str(input("Digite seu nome: "))
    if procura in contatos.values():
        print("Contato de {}, foi encontrado!").format([procura])

#funcao que remove o arquivo
def apagar_agenda():
    
    resposta = str(input("Certeza que deseja apagar a agenda?[s/n]"))
    if(resposta == "s"):
        with open ("Agenda telefonica.txt", "r+") as arquivopy:
            arquivopy.truncate(0) #a função truncate "redimensiona" o arquivo, no caso para tamanho 0, que 
            #apaga os elementos existentes
    else:
        print ("Ação cancelada!")

#MENU e criação da agenda.txt
with open('Agenda telefonica.txt','r') as arquivopy:
    contatos={}
    pegar_linhas(contatos)
    option=0
    while(option !=8):
        print("-------MENU------")
        print("1 - Adicionar contato")
        print("2 - Listar agenda")
        print("3 - Procurar contato por número")
        print("4 - Procurar contato por nome")
        print("5 - Alterar contato")
        print("6 - Excluir contato")
        print("7 - Apagar agenda")
        print("8 - Sair")
        option =  (int(input("Digite a sua opção: ")))
        match (option):
            case 1:
                adicionar_contato()
            case 2:
                ler_agenda()
            case 3:
                procurar_numero()
            case 7:
                apagar_agenda()
            case 8:
                print("Agenda fechando...")
