nome = str(input("Digite o nome do usuário: "))
idade = int(input("Digite a idade do usuário: "))
salario = float(input("Digite o salario do usuário: "))
sexo = str(input("Digite o sexo do usuário: "))
estadoCivil = str(input("Digite o estado civil do usuário: "))

while len(nome) < 3 or idade < 0 or idade > 150 or salario < 0 or sexo != "M" and sexo != "F" and estadoCivil != "S" and estadoCivil != "C" and estadoCivil != "V" and estadoCivil != "D":
    print("Informações Inválidas")
    nome = str(input("Digite o nome do usuário: "))
    idade = int(input("Digite a idade do usuário: "))
    salario = float(input("Digite o salario do usuário: "))
    sexo = str(input("Digite o sexo do usuário: "))
    estadoCivil = str(input("Digite o estado civil do usuário: "))

else:
    print("Informações Válidas")
