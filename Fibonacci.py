n = int(input("Quantos termos serão listados ? "))
num = int(input("Qual o número deseja procurar ?"))

t1 = 0
t2 = 1
t4 = []

print("{} - {} - ".format(t1, t2), end="")

cont = 3

while cont <= n:
    t3 = t1 + t2
    print("{} - ".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
    t4.append(t3)

print("Fim da sequencia de Fibonacci")

i = 0
for n in t4:
    if (t4[i] == num):
        print("O número pertence")
    else:
        print("O múmero não pertence")

    i = i + 1

print(t4)


