votoAda = 0
votoLinus = 0
votoFeio = 0
votoNulo = 0
votoBrancos = 0
while True :
    print("*** Candidatos da computação ***")
    print("1. Candidata Ada Lovelace")
    print("2. Candidato Linus Tovalds")
    print("3. Candidato Patinho feio")
    print("4. Nulo ")
    print("5. Branco")
    print("6. Relatório Eleição")
    
    votos=int(input("Número do candidato(a)"))
    if (votos == 0):
     print("Sair do sistema !")
     break
 
    elif(votos ==1):
        votoAda+=votos 
    elif(votos ==2):
        votoLinus +=1
    elif(votos==3):
        votoFeio+=1
    elif(votos ==4):
        votoNulo+=1
    elif(votos==5):
        votoBrancos+=1
     
   
        soma=votoAda+votoLinus+votoFeio+votoBrancos+votoNulo
        porcentagemNulo=votoNulo*100/soma
        porcentagemBranco = votoBrancos*100/soma
    else:
        print("***Relatório leição***")
        print("***********") 
       
        print("*******") 
        print(f"Candidata Ada Lovelace {votoAda} votos")
        print(f"Candidato Linus Torvalds {votoLinus} votos")
        print(f"Candidato Patinho Feio {votoFeio} votos")
        print(f"Votos nulos {votoNulo} votos nulos ")
        print(f"Votos em Branco {votoBrancos} votos brancos")       
        print(f"Total de votos : {soma}")
        print("")
        print(f"Total de votos nulos : {porcentagemNulo: .2f} %")
        print(f"Total de votos Brancos: {porcentagemBranco: .2f} %")
        print("")
        if(votoAda > votoLinus and votoAda >votoFeio):
                print(f"Candidato vencedor Ada Lovelace")
        elif(votoLinus >votoAda and votoLinus>votoFeio):
                print(f"Candidato vencedor Linus Tovalds")
        else:
            (f"Candidato vencedor Patinho Feio")
        break    
  