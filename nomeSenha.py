nome = str(input("Digite o nome do usuário: "))
senha = str(input("Digite o senha do usuário: "))

while nome == senha:
    print("Acesso Inválido")
    nome = str(input("Digite o nome do usuário: "))
    senha = str(input("Digite o senha do usuário: "))
else:
    print("Acesso Válido")
