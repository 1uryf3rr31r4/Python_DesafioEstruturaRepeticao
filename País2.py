paisA = int(input("Digite o número da população do País A: "))
paisB = int(input("Digite o número da população do País B: "))
txA = float(input("Digite a taxa de crescimento populacional do País A: "))
txB = float(input("Digite a taxa de crescimento populacional do País B: "))

ano = 0
if paisA <= 0 or paisB <= 0 or txA <= 0 or txB <= 0:
    print("Informações Inválidas")
    paisA = int(input("Digite o número da população do País A: "))
    paisB = int(input("Digite o número da população do País B: "))
    txA = float(input("Digite a taxa de crescimento populacional do País A: "))
    txB = float(input("Digite a taxa de crescimento populacional do País B: "))
else:
    while paisA < paisB:
        paisA = paisA * (1 + txA/100)
        paisB = paisB * (1 + txB/100)
        ano += 1
    
print("O país A levará {} anos para superar o país B".format(ano))
