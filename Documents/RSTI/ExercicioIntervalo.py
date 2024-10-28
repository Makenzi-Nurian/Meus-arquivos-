"""
Programa que receba 10 números e mostre o que esta dentro do intervalo e fora do intervalo

"""
y = 0
x = 0 
for i in range(1, 6 ):
    numero = int(input("Digite valor: "))
    if numero >= 10 and numero <= 20:
        x+=1
    
    else:
        y+=1
        
print( f"{x} Dentro do intervalo")
print(f"{y} Fora do intervalo")    