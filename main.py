#função que adciona um contato no dicionario
def adicionar_contato ():
    contatos={}
    with open('Agenda telefonica.txt','a') as arquivopy:
            
        nome= str(input("Digite seu nome: "))
        telefone = int(input("Digite seu telefone: "))
        contatos[nome]=telefone
          
        for nome,telefone in contatos.items():
            arquivopy.write(str(nome)+"\n"+str(telefone)+"\n") #dessa forma pega os valores e os escreve na um embaixo do outro no arq       
        print("O contato de {} e seu numero: {}, foram adicionados a agenda!".format(nome, telefone))
           
            
           
#função que le as linhas de um arquivo
def ler_agenda():
    with open ("Agenda telefonica.txt", 'r') as arquivopy:
        linhas=arquivopy.readlines() #variavel linhas recebe funcao que le as linhas do arquivo
        for lines in linhas:
         print(lines)



#função que pega as linhas do arquivo o transforma em um dicionario
def pegar_linhas():
    listanome=[]
    listtel=[]
    with open ("Agenda telefonica.txt", "r") as arquipy:
        linhas = arquipy.readlines()
        
        #aqui estou pegando cada linha do arquivo, e se a linha é par, o elemento que esta nela
        #cai na lista dos nome, se for impar cai na lista dos numeros.
        for i in range (len(linhas)):
            if(i%2==0):
                listanome.append(linhas[i].strip())
                #a funcao strip retira espaços em branco e enter "\n"
                #append é a maneira de adiconar itens dentro de listas no python
            elif(i%2!=0):
                listtel.append(linhas[i].strip())
               
        #agora junto as duas listas em um dicionario
    unirlistas = zip(listanome, listtel)
    global contatos #transformando em uma variavel global para poder usar em outras funções
    contatos= dict(unirlistas) 
       
    print(contatos)#esse print é so pra eu ver se deu certo dps apago(lembrete para karen do futuro)



#funcao que mostra o tamanho da agenda (pelo tamanho do dicionario)   
def tamanho_agenda ():
    print ("O número de contatos que a agenda possui no momento é de: ", len(contatos))
    #a funçao len le o tamanho do dicionario (assim como poder ler o tamanho de uma lista também)


#função que procura pelo nome
def procurar_nome():
    
    procura = str(input("Digite seu nome: "))
    if procura in contatos.keys():
        print ("O contato de '{}' e seu número '{}', foi encontrado na agenda!" .format(procura, contatos[procura]))
    else:
        print ("Contato não encontrado")
    
  


#função que procura pelo numero
def procurar_numero():
    procuranumero = str(input("Digite seu número:"))
    if procuranumero in contatos.values():
        print ("O número '{}', foi encontrado na agenda!" .format(procuranumero))
    else:
        print("Número não foi encontrado.")


#funcao para alterar um contato()
def alterar_contato():
    procurar_cont = str(input("Digite seu nome: "))
    if procurar_cont in contatos:
        del contatos[procurar_cont]
        #del é uma keyword que deleta o elemento nas chaves

        novo_nome=str(input("Digite o novo nome: "))
        novo_tel = input("Digite o novo número")
        contatos[novo_nome]=novo_tel

        with open ("Agenda telefonica.txt", 'a') as arquivopy:
            arquivopy.truncate(0) #apago a agenda para inserir o novo dicionario com o contato alterado
            for nome, telefone in contatos.items():
                arquivopy.write(str(nome)+"\n"+str(telefone)+"\n")

        print("O contato foi alterado!")
    else:
        print("Desculpe, contato não encontrado!")



#funcao para deletar um contato(essa não difere tanto da de alterar, os passos seguem praticamente os mesmos)
def excluir_contato():
    procurar_cont = str(input("Digite o nome do contato que deseja excluir: "))
    if procurar_cont in contatos:
        del contatos[procurar_cont]
  
        with open ("Agenda telefonica.txt", 'a') as arquivopy:
            arquivopy.truncate(0)
            for nome, telefone in contatos.items():
                arquivopy.write(str(nome)+"\n"+str(telefone)+"\n")

        print("O contato foi apagado da agenda!")
    else:
        print("Desculpe, contato não encontrado!")



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
    
    pegar_linhas()
    option=0
    while(option !=9):
        print("-------MENU------")
        print("1 - Adicionar contato")
        print("2 - Listar agenda")
        print("3 - Quantidade de contatos")
        print("4 - Procurar contato por número")
        print("5 - Procurar contato por nome")
        print("6 - Alterar contato")
        print("7 - Excluir contato")
        print("8 - Apagar agenda")
        print("9 - Sair")
        option =  (int(input("Digite a sua opção: ")))
        match (option):
            case 1:
                adicionar_contato()
            case 2:
                ler_agenda()
            case 3:
                tamanho_agenda()
            case 4:
                procurar_numero()
            case 5:
                procurar_nome()
            case 6:
                alterar_contato()
            case 7:
                excluir_contato()
            case 8:
                apagar_agenda()
            case 9:
                print("Agenda fechando...")
