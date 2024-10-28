numero_notas = 3
soma = 0

for i in range (numero_notas):
    nota = float(input(f"Digite a {i+1}ª  nota: "))
    soma += nota 
    
media = soma / numero_notas
print(f"A média do aluno é: {media: .2f}")