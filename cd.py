qCd = int(input("Digite a quantidade de CD's comprados: "))
print("~~"*24)

cont = 0
sCd = 0

while cont < qCd:
    vCd = int(input("Digite a valor de cada CD comprado: "))
    cont += 1
    sCd += vCd

mCd = sCd / qCd

print("~~"*24)

print(f"O valor total investido pelo colecionador foi {sCd}")
print(f"O valor médio gasto por CD foi {mCd}")
