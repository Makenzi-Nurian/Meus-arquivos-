while True:
    print ("*** CALCULADORA ***")
    print("1. Adição")
    print("2. Subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("0. Sair")
    
    opcao = int(input("Escolha a opção: "))
    if(opcao == 0):
        print("Sair do sistema")
        break
    
    elif(opcao == 1):
        valor1 = int(input("Digite o primeiro valor "))
        valor2 = int(input("Digite o segundo valor "))
        resultado = valor1 + valor2  
        print("O resultado é:" ,resultado) 
        
    elif (opcao == 2):
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        resultado = valor1 - valor2
        print("O resultado é" ,resultado) 
        
    elif(opcao == 3):
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        resultado = valor1*valor2
        print("O resultado é " ,resultado) 
    elif(opcao == 4):
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        if(valor2 ==0):
            print("Divisão por zero não é permitida !!!")
        else:
            resultado = valor1/valor2
            print("O Resultado é:" ,resultado)
    else:
        print("Operação não permitida !!! ")    
    
    