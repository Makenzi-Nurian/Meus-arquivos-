def somar_dois_numeros(a,b):
    resultado = a + b
    return resultado

def calcular_triplo(valor):
    return valor * 3

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

soma = somar_dois_numeros (a,b)
print("Soma: " ,soma)

triplo = calcular_triplo (soma)

print("O triplo da soma é: " ,triplo)