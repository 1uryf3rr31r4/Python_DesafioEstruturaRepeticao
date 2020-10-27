qPao = 50
pPao = 0.18
cont = 1

print(f"Preço do pão: {pPao}")
print("Panificadora Pão de Ontem - Tabela de Preços")
while cont <= qPao:
    print(f"{cont} - R$ {cont*pPao}")
    cont += 1
