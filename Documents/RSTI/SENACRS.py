def calcular_media_notas(alunos):
    notas = [aluno[2] for aluno in alunos]
    return sum(notas) / len(notas)

def encontrar_aluno_mais_velho(alunos):
    maior_idade = 0
    aluno_mais_velho = None
    for aluno in alunos:
        if aluno[0] > maior_idade:
            maior_idade = aluno[0]
            aluno_mais_velho = aluno
    return aluno_mais_velho

def encontrar_aluno_mais_novo(alunos):
    menor_idade = 999
    aluno_mais_novo = None
    for aluno in alunos:
        if aluno[0] < menor_idade:
            menor_idade = aluno[0]
            aluno_mais_novo = aluno
    return aluno_mais_novo

def principal():    
    dados_alunos = []
    while True:
        idade = int(input("Digite a idade do aluno (ou 0 para sair): "))
        if idade == 0:
            break        
        sexo = input("Digite o sexo do aluno (M/F): ")
        nota = float(input("Digite a nota do aluno: "))
        dados_alunos.append([idade, sexo, nota])
    return dados_alunos

alunos = principal()
media = calcular_media_notas(alunos)
aluno_mais_velho = encontrar_aluno_mais_velho(alunos)
aluno_mais_novo = encontrar_aluno_mais_novo(alunos)

# Imprimir dados dos capirotos
for aluno in alunos:
    print("-" * 20)
    print("Idade:", aluno[0])
    print("Sexo:",  aluno[1])
    print("Nota:",  aluno[2])
    print("-" * 20)

print("A média das notas dos alunos é:", media)
print("O aluno mais velho tem", aluno_mais_velho[0], "anos.")
print("O aluno mais novo tem", aluno_mais_novo[0], "anos.")