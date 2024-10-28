numero = int(input("Digite o número que se refere a tabuada da sua preferencia: "))

v1 = int(input("Valor inicial: "))
v2 = int(input("Valor final: "))
for i in range(v1, v2+1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado} ")