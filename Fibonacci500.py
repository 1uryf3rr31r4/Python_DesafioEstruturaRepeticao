n = int(input("Quantos termos serão listados ? "))

t1 = 1
t2 = 1

print("{} - {} - ".format(t1, t2), end="")

cont = 3

while cont <= n:

    t3 = t1 + t2
    
    if t3 < 700: 
        print("{} - ".format(t3), end="")
        t1 = t2
        t2 = t3
        cont += 1

print("Fim da sequencia de Fibonacci")


