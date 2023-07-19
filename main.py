#VARIAVEIS
import json
#função que adciona um contato no dicionario
def adicionar_contato ():
    contatos={}
    resposta ="s"
    with open('Agenda telefonica.txt','a') as arquivopy:

       while (resposta.lower() == "s"):
         nome= str(input("Digite seu nome: "))
         telefone = int(input("Digite seu telefone: "))
         contatos[nome]= {
            "nome" :nome,
            "telefone" :telefone
         }
         for chaves, valor in contatos.items():
            print(chaves,valor)
           #for n in contatos.values():
          #arquivopy.write(str(n)+"\n")
       

         arquivopy.write(str(contatos)+"\n")
         #print("O contato de {} e seu numero: {}, foram adicionados a agenda!".format(contatos["nome"], contatos["telefone"]))
         resposta = str(input("Adicionar outro contato?[s/n]"))
        
         



#função que le as linhas de um arquivo
def ler_agenda():
    with open ("Agenda telefonica.txt", 'r') as arquivopy:
        linhas=arquivopy.readlines() #variavel linhas recebe funcao que le as linhas do arquivo
        for lines in linhas:
         print(lines)
    
#MENU e criação da agenda.txt
with open('Agenda telefonica.txt','r') as arquivopy:
    print("-------MENU------")
    print("1- Adicionar contato")
    print("2- Listar agenda")
    print("3 - Procurar contato por número")
    print("4 - Procurar contato por nome")
    print("5 - Alterar contato")
    print("6 - Excluir contato")
    print("7 - Apagar agenda")
    option =  (int(input("Digite a sua opção: ")))

    while(option !=8):
        match (option):
            case 1:
                adicionar_contato()
            case 2:
                ler_agenda()
            case 8:
                print("Agenda fechando...")
