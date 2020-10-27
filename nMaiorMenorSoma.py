n = int(input("Digite a quantidade de lista de números: "))
print("")

lista = []
cont = 0
maior = 0
soma = 0


if n < 0 and n >1000:
    print("Operação Interrompida. Dados Inválidos")

else:
    while cont < n:
        lista.append(int(input(f"Digite o numero {cont+1} da lista: ")))
        cont += 1

    print("")

    menor = lista[0]

    for i in range(0, cont):

        if maior < lista[i]:
            maior = lista[i]

        if menor > lista[i]:
            menor = lista[i]

        soma += lista[i]

    print("")
    print(f"A lista informada: {lista}")
    print(f"O maior valor da lista: {maior}")
    print(f"O menor valor da lista: {menor}")
    print(f"O soma dos valores da lista: {soma}")
