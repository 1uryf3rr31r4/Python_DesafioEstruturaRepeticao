nEleitor = int(input("Digite o números de eleitores: "))
print("~~~"*22)

candidatoA = 13
candidatoB = 17
candidatoC = 50
cont = 0

urnaA = 0
urnaB = 0
urnaC = 0

print("Canditado A - 13")
print("Canditado B - 17")
print("Canditado C - 50")
print("~~~"*22)

while cont < nEleitor:

    Voto = int(input("Digite o número do seu candidato que receberá o seu voto: "))

    if Voto == 13:
        urnaA += 1
        
    elif Voto == 17:
        urnaB += 1

    elif Voto == 50:
        urnaC += 1

    else:
        print("Número de canditado inválido")

    cont += 1

if urnaA > urnaB and urnaA > urnaC:
    print("O candito A é o eleito")

elif urnaB > urnaA and urnaB > urnaC:
    print("O candito B é o eleito")

else:
    print("O candito C é o eleito")
