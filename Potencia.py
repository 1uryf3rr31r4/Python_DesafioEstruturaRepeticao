base = int(input("Digite a primeiro número: "))
expo = int(input("Digite o segundo número: "))


if expo == 0:

    print("O resultado do primeiro número {} elevado ao segundo número {} é 1".format(base, expo))
    
elif expo == 1:

    print("O resultado do primeiro número {} elevado ao segundo número {} é {}".format(base, expo, base))

elif base == 0:
    print("O resultado do primeiro número {} elevado ao segundo número {} é 0".format(base, expo))


elif expo < 0:

    calc = 1/base
    expo = expo * -1
    
    for i in range(1, expo):
        calc *= base

    print("O resultado do primeiro número {} elevado ao segundo número {} é {}".format(base, expo, calc))
          
elif expo > 1:

    calc = base
    for i in range(1, expo):
        calc *= base

    print("O resultado do primeiro número {} elevado ao segundo número {} é {}".format(base, expo, calc))


