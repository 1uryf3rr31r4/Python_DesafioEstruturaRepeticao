num = int(input("Digite o valor para gerar a média aritmética: "))

soma = 0

for i in range(1,num+1):
    soma += i

mediaA = soma / num

print(mediaA)
