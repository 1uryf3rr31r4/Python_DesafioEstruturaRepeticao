print("Gerador de Tabuadade 1 a 10")

num = int(input("Digite o número: "))

if num > 0 and num < 11:
    print("Tabuada de {}".format(num))

    for i in range(0, 10):
        print(num," x ", i+1," = ",num * ((i+1)))
else:
    print("Números fora da tabuada")

