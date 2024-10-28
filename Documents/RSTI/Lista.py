
alunos = []
numeroAlunos = 5
for i in range(numeroAlunos):
    nome = input("Digite o nome do aluno {}: ".format(i+1))
    idade = int(input("Digite a idade {}:" .format(nome)))
    alunos.append({'nome': nome, 'idade':idade})
    
    somaIdades = 0
    for aluno in alunos:
        somaIdades += aluno['idade']
        mediaIdades = somaIdades/len(alunos)
        
        print("\nAlunos acima da média:")
        for aluno in alunos:
            if aluno ['idade'] > mediaIdades:
                print(aluno['nome'])
                print(aluno['idade'])
                 
                