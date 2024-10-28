salarioBruto = float(input("Entre com o salário bruto: "))
filhosMenores = float(input("Número de filhos menores de 14 anos: "))

if(salarioBruto <= 2259.20):
    irrf = 0
    
elif(salarioBruto >=2259.21 and salarioBruto <= 2826.65):
    irrf = salarioBruto * 0.075 - 169.44

elif(salarioBruto >=2826.66 and salarioBruto <= 3751.05):
    irrf = salarioBruto * 0.15 -381.44
    
elif(salarioBruto >= 3751.06 and salarioBruto <= 4664.68):
    irrf = salarioBruto * 0.225-662.77
    
else:
    irrf =    
    
print("***** FOLHA DE PAGAMENTO *****")
print("Salario Bruto: " ,salarioBruto)
print("IRRF" ,irrf)