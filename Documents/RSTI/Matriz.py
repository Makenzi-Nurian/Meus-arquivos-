matriz = []
numeroLinhas = 3
numeroColunas = 3
for linha in range(numeroLinhas):
    inserir = []
    for coluna in range(numeroColunas):
      valor = int(input(f"Digite o valor para a oposição [ {linha}, {coluna}]:"))
      inserir.append(valor)
    matriz.append(inserir)
print("matriz criada:")
for imprimir in matriz:
    print(imprimir)
    
print("SOMA DOS VALORES DA MATRIZ")
soma = 0 
for linha in matriz:
 for valor in linha:
    soma+=valor
    print("A soma dos VALORES da matriz é:",soma)
        
print("O MENOR VALOR DA MATRIZ")
menor = matriz[0][0]
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna]< menor:
            menor= matriz[linha][coluna]
            print("O menor valor da matriz é: ", menor)                         
        
print("DIAGONAL PRINCIPAL")
diagonalPrincipal = len(matriz)
for dp in range(diagonalPrincipal):
    print(matriz [dp] [dp])
    
print ("DIAGONAL SECUNDÁRIA")
ds = len(matriz)
for linha in range(ds):
    print(matriz[linha][ds-linha -1])
    
    with open ('Rlatorio.txt','w') as arquivo:
        for linha in matriz :
            linha_str = ' '.join(map(str, linha))
            arquivo.write(linha_str + '\n')
            arquivo.write(f"A diagonal principal da matriz é {diagonalPrincipal}")   
        
