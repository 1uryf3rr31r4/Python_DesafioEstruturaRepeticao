n = int(input("Digite número para calcular seu fatorial: "))

cont = n
f = 1
print("~~"*20)
print(f"Fatorial de: {n}")

print(f"{n}! = ", end="")


while cont > 0:
    print(f"{cont}", end="")
    print(" . " if cont > 1 else " = ", end="")
    f *= cont
    cont-=1

print(f"{f}")
