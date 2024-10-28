matriz = []
numlinha = 3
numcoluna = 3

for linha in range(numlinha):
    inserir = []
    for coluna in range(numcoluna):
      valor = int(input(f"Digite o valor para a posição {linha} {coluna}: "))
      inserir.append(valor)
    matriz.append(inserir)
print("Matriz criada:")
for imprimir in matriz:
        print(imprimir) 
        
with open ('Relatorio.txt' , 'w') as arquivo:
    for linha in matriz:
        linha_str = ' ' .join(map(str, linha))
        arquivo.write(linha_str + '\n')
print("DIAGONAL PRINCIPAL: ")
dp = len(matriz)
teste = []
for igualLinhaColuna in range(dp):
    teste.append(matriz[igualLinhaColuna][igualLinhaColuna])
print(teste)   

print("SOMA DA DIAGONAL PRINCIPAL ")
dp = len(matriz)
teste = []
soma = 0  # Variável para armazenar a soma da diagonal

for igualLinhaColuna in range(dp):
    valor_diagonal = matriz[igualLinhaColuna][igualLinhaColuna]
    teste.append(valor_diagonal)
    soma += valor_diagonal  # Somando os valores da diagonal
print("A soma da diagonal principal é :" ,soma)    


