from array import array
num = []
inter = []
soma = 0

for i in range(0,2):
    num.append(int(input(f"Digite um valor para posição {i}: ")))

for i in range(0, 2):
    fim = num[i]

inicio = num[0]

intervalo = fim - inicio

inicioIntervalo = num[0]+1

if intervalo == 0: 
    print("Sem intervalos. Números iguais")

elif intervalo == 1:
    print("Não há intervalos entre eles")

elif intervalo > 1:

    inter = []
    
    for i in range(0, intervalo-1):
        soma += intervalo
        inter.append(int(inicioIntervalo+i))

print("=-="*15)
print(f"O intervalo entre os números: {inter}")
print("Primeiro número do intervalo: {} ".format(inicio))
print("Ultimo número do intervalo: {}".format(fim))
print("Total da soma dos números entre os intervalos: {}".format(soma))

