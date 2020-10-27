num = []

qPar = 0
qImpar = 0

for i in range(0,10):
    
    num.append(int(input(f"Digite o número {i+1}: ")))


for i in range(0, 10):

    if (num[i] % 2) == 0:
        qPar += 1

    else:
        qImpar += 1
        
print(f"A lista de números digitados é essa : {num}")
print(f"A quantidade de números pares é : {qPar}")
print(f"A quantidade de números ímpares é : {qImpar}")
