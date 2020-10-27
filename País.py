paisA = 80000
paisB = 200000

txA = 0.03
txB = 0.015

ano = 0

while paisA < paisB:

    paisA = paisA * (1 + txA)
    paisB = paisB * (1 + txB)
    ano += 1
    
print("O país A levará {} anos para superar o país B".format(ano))
