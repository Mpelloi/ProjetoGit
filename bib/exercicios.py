def ex1():
    metros = float(input("Informe o valor em metros: "))
    
    def centimetros(m):
        return metros * 100

    centmt = centimetros(metros)
    print(f"Valor em centimetros é: {centmt:.0f} cm")

def ex2():
    valorhora = float(input("Informe o valor da sua hora de trabalho: "))
    horastrabalho = int(input("Informe suas horas trabalhadas no mês: "))

    ganhomensal = valorhora * horastrabalho

    print(f"Seu ganho mensal foi de: R$ {ganhomensal:,.2f}")

def ex3():
    fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
    
    def f_para_c(fahrenheit):
        cels = 5 * ((fahrenheit - 32) / 9)
        return cels
    celsius = f_para_c(fahrenheit)

    print(f"Valor convertido em Celsius é: {celsius:.0f}ºC")

def ex4():
    peso = int(input("Informe o seu peso: "))
    altura = float(input("Informe a sua altura: "))

    print(f"Seu IMC é de {peso/(altura**2):.2f}")

def ex5():
    kilopescado = float(input("Informe a quantidade pescada em Kg: "))
    excesso = kilopescado - 30
    multa = excesso * 3

    if excesso>0: print(f"""Peso excedido em: {excesso} Kg 
    Multa a pagar R$: {multa:.2f}""")
    else: print(f"-- Valor dentro do peso permitido --")
