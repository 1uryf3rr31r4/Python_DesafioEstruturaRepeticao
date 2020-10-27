temp = []
descisao = "S"
maior = 0
menor = 0
cont = 0
media = 0
while descisao != "N":
    temp.append(float(input("Digite a temperatura a ser medida: ")))
    descisao = input("Deseja continuar [S]im ou [N]ão: ")
    if cont == 0:
        maior = menor = temp[cont]
    else:
        if temp[cont] > maior:
            maior = temp[cont]
        if temp[cont] < menor:
            menor = temp[cont]
    media = media + temp[cont]
    print("--" * 10)
    cont = cont + 1


print(f"As temperaturas digitadas foram {temp}")
print(f"A maior temperatura é {maior}")
print(f"A menor temperatura é {menor}")
print(f"A temperatura média é {media/cont}")