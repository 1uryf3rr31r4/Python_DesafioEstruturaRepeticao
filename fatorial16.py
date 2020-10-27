from time import sleep
print("CALCULAR FATORIAL")
print("~~"*10)

n = int(input("Digite número para calcular seu fatorial: "))
opcao = 0
print("~~"*10)
if n < 16:
    
    while opcao != 3:

        print("[1] Calcular Fatorial")
        print("[2] Novos valores")
        print("[3] Sair do programa")
        opcao = int(input("Qual é a opção: "))
        print("~~"*10)
        cont = n
        f = 1

        if opcao == 1:
            
            print(f"{n}!=", end="")

            while cont > 0:
                print(f"{cont}", end="")
                print("." if cont > 1 else "=", end="")
                f *= cont
                cont-=1

            print(f"{f}")
            print("~~"*10)
            
        elif opcao == 2:

            print("Informe os valores novamente")
            n = int(input("Digite número para calcular seu fatorial: "))
            print("~~"*10)

        elif opcao == 3:
            print("Finalizando...")
            
        else:
            print("Opção Inválida. Tente Novamente")

else:
    print("Operação Interrompida. O número não pode ser maior que 16 e menor que 0")

sleep(1)
print("~~"*10)
print("Fim do programa")

