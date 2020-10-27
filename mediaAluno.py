qTurma = int(input("Digite a quantidade de turmas na escola: "))
cont = 0
sAluno = 0
while cont < qTurma:
    qAluno = int(input("Digite a quantidade de aluno por turma na escola: "))
    cont += 1

    if qAluno < 40:
        sAluno += qAluno
    else:
        print("Turmas não podem ter mais de 40 aluno")

mAluno = sAluno / qTurma


print(mAluno)
