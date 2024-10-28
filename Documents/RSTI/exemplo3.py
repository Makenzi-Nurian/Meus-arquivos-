def calcular_media_veiculos(carros):
    valores = [carro[3] for carro in carros]
    return sum(valores) /len(valores)

def encontrar_veiculo_mais_caro (carros):
    maior_valor = 0
    carro_mais_caro = None
    for carro in carros:
        if carro[3] > maior_valor:
           maior_valor = carro[3]
           carro_mais_caro = carro
def encontrar_veiculo_mais_barato (carros):
    menor_valor = 999
    carro_mais_barato = None
    for carro  in carros:
        if carro[3] < menor_valor:
            menor_valor = carro[3]
            carro_mais_barato = carro
    return carro_mais_barato    
def principal ():
    cadastro_carro = []
    while True:
        placa = int(input("Digite a placa: "))
        if placa == 0:
            break
        marca = str(input("Digite a marca do Veículo: "))
        modelo = str(input("Digite o modelo do veículo: "))
        valor = float(input("Digite o valor do veículo: "))
        ano = int(input("Digite o ano do veículo: "))
        cadastro_carro.append([placa ,marca, modelo, valor, ano])
    return cadastro_carro
