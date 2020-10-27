nPessoa = int(input("Digite o número de pessoa para verificar a média aritmética de idade da turma: "))
totIdade = 0

if nPessoa <= 0:
    print("Atividade Interropida. Número de pessoas inválido")

elif nPessoa >=1:
    
    for i in range(1,nPessoa+1):
        idade = int(input(f"Digite a idade da pessoa {i}: "))
        totIdade += idade 

    mediaIdade = totIdade / nPessoa

    if mediaIdade > 0 and mediaIdade < 25:
        print(f"A média de idade da turma é {mediaIdade}, ela é considerada jovem")

    elif mediaIdade > 26 and mediaIdade < 60:
        print(f"A média de idade da turma é {mediaIdade}, ela é considerada adulta")

    elif mediaIdade > 60:
        print(f"A média de idade da turma é {mediaIdade}, ela é considerada idosa")

else:
    print("Dados Inválidos")
    
