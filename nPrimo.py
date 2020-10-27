print("VERIFICADOR DE NÚMERO PRIMO")

print("~~"*10)

n = int(input("Digite o número: "))
print("~~"*10)
cont = 1
cont2 = 0

while cont <= n:

    if n % cont == 0:
        cont2 += 1

    cont += 1

if cont2 == 2:
    print(f"O número {n} é primo")
    print("~~"*10)
else:
    print(f"O número {n} não é primo")
    print("~~"*10)
