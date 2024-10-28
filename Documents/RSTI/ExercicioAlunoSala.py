"""
Escreva um programa que pergunte ao usuário quantos alunos tem na sala dele.
Em seguida, através de um laço for, pede ao usuário para que entre com as notas de todos os alunos da sala, um por vez.

"""
qtdeAlunos = int(input("Número de alunos: "))
for i in range(qtdeAlunos):
    nota = float(input(f"Nota aluno {i+1}:"))
    print(f"{i+1} - {nota}")
    