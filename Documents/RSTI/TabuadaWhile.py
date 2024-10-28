numero = int(input("Escreva um número: "))

v1 = 1
v2= 10
for i in range(v1, v2+1):
    resultado = numero * i
    print(f" { numero } x {i} = {resultado}")