item = 0
cesta = []
compra = 1
soma = 0
rep = 1

while rep > 0:
    while compra != 0:
        compra = float(input(f"Item {item+1}: "))

        if compra != 0:
            cesta.append(compra)
            item += 1
            soma += compra

    print(f"Total da compra: R$ {soma}")
    pag = float(input("Valor pago em dinheiro: R$ "))

    troco = pag - soma

    print("~~"*20)

    print("Loja Tabajara")

    for i in range(0, item):
        print(f"Produto {i+1}: R$ {cesta[i]}")

    print(f"Total: R$ {soma}")
    print(f"Dinheiro: R$ {pag}")
    print(f"Troco: R$ {troco}")
    
    compra += 1
    item = 0
    
    print("~~"*20)
