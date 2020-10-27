from array import array
num = [0, 0]

for i in range(0,2):
    num[i] = int(input(f"Digite o numero [{i+1}]: "))

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
    for i in range(0, intervalo-1):
        print(inicioIntervalo+i, end=" ")
        
