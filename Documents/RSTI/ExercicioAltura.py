menor_altura = 999
maior_altura = 0
contador = 0

while True :
    altura = float(input("Informa a altura: "))
    if altura <=0:
        print("Altura inválida, digite um número positivo: ")
    else:
         
        if(altura > maior_altura): 
          maior_altura = altura
        if(altura < menor_altura):
          menor_altura = altura
          
          contador +=1
        if contador == 5:
            
              print(f"A maior altura do grupo é: {maior_altura: .2f}")
              print(f"A menor altura do grupo é: {menor_altura: .2f}")
              break
     

    
        
    
            
