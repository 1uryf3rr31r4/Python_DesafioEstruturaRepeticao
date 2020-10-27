num = int(input("Digite o valor entre de zero a dez: "))

while num < 0 or num > 10:
    print("Inválido")
    num = int(input("Digite o valor entre de zero a dez: "))
else:
    print("Válido")
