from exercicios import *


while True:
    n_exercicio = int(input("Informe o numero do exercício: "))

    if n_exercicio == 1 :
        ex1()
    elif n_exercicio == 2 :
        ex2()
    elif n_exercicio == 3 :
        ex3()
    elif n_exercicio == 4 :
        ex4()
    elif n_exercicio == 5 :
        ex5()
    else:
        print("Exercício não existe")
        break

    
    