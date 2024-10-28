from exemplo3 import calcular_media_veiculos, encontrar_veiculo_mais_caro, encontrar_veiculo_mais_barato, principal


    
veiculos = []


veiculos = principal()        

media = calcular_media_veiculos(veiculos) 
carro_mais_caro = encontrar_veiculo_mais_caro(veiculos)
carro_mais_barato = encontrar_veiculo_mais_barato(veiculos) 

for carros in veiculos:
    print("Placa: " ,carros[0])
    print("Marca:" ,carros[1])
    print("MOdelo: " ,carros[2])
    print("Valor: " ,carros[3])
    print("Ano" ,carros[4])
   
print(f"A média dos valores dos veículos é de: {media:.2f}")  # Formatação para 2 casas decimais
if carro_mais_caro:
    print(f"O carro mais caro é: Placa: {carro_mais_caro[0]}, Marca: {carro_mais_caro[1]}, Modelo: {carro_mais_caro[2]}, Valor: {carro_mais_caro[3]}, Ano: {carro_mais_caro[4]}")
if carro_mais_barato:
    print(f"O carro mais barato é: Placa: {carro_mais_barato[0]}, Marca: {carro_mais_barato[1]}, Modelo: {carro_mais_barato[2]}, Valor: {carro_mais_barato[3]}, Ano: {carro_mais_barato[4]}")
    
    