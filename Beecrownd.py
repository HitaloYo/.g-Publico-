def b1007():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    diferenca = a * b - c * d
    print("DIFERENCA =".format(diferenca))
def b1008():
    a = int(input())
    b = int(input())
    c = float(input())
    salary = b * c
    print("NUMBER = {}".format(a))
    print("SALARY = U$ {:.2f}".format(salary))
def b1009():
    a = str(input())
    b = float(input())
    c = float(input())
    print(f'TOTAL = R$ {b + ((c * 15) / 100):.2f}')
def b1010():
    linha1 = input().split()
    linha2 = input().split()
    x_1, y_1, z_1 = list(map(int, linha1))
    x_2, y_2, z_2 = linha2(map(int, linha2))
    resultado = (x_1 * y_1) + (x_2 * y_2)
    print("VALOR A PAGAR: R$ {:.2f}".format(resultado))
def b1011():
    N = int(input())
    area = (4 / 3) * 3.14159 * (N ** 3)
    print("VOLUME = {:.3f}".format(area))
def b1012():
    linha = input().split()
    a, b, c = list(map(int, linha))
    triangulo = (a * c) / 2
    circulo = (c * c) * 3.14159
    trapezio = ((a * c) / 2) + ((b * c) / 2)
    quadrado = b * b
    retangulo = a * b
    print("Resultados abaixo")
    print("TRIANGULO: {0:.3f}".format(triangulo))
    print("CIRCULO: {0:.3f}".format(circulo))
    print("TRAPEZIO: {0:.3f}".format(trapezio))
    print("QUADRADO: {0:.3f}".format(quadrado))
    print("RETANGULO: {0:.3f}".format(retangulo))
def b1013():
    linha = input().split()
    a, b, c = list(map(int, linha))
    maiorABC = (((a + b + abs(a - b))/2) + c + abs(((a + b + abs(a - b))/2) - c))/2
    print("{} eh o maior".format(int(maiorABC)))
def b1014():
    x = int(input())
    y = float(input())
    gasto = x/y
    print("{:.3f} km/l".format(gasto))
def b1015():
    linha = input().split()
    linha2 = input().split()
    x1, y1 = list(map(float, linha))
    x2, y2 = list(map(float, linha2))
    distancia = (((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))) ** 0.5
    print("{0:.4f}".format(distancia))
def b1016():
    y = int(input())
    y = y * 2
    print("{} minutos".format(y))
def b1017():
    tempo = int(input())
    velocidade = int(input())

    consumo = (tempo * velocidade) / 12

    print("{0:.3f}".format(consumo))
def b1018():
    n = int(input())
    notas = [100, 50, 20, 10, 5, 2, 1]
    print(n)
    for i in range(len(notas)):
        if (n >= notas[i]):
            print("%d nota(s) de R$ %d,00" % (n // notas[i], notas[i]))
            n = n % notas[i]
        else:
            print("0 nota(s) de R$ %d,00" % (notas[i]))
def b1019():
    N = int(input())
    horas = 0
    minutos = 0
    if N < 60:
        segundos = N
    elif N >= 60:
        segundos = int(N % 60)
        minutos = int(N / 60)
    if minutos >=60:
        horas = int(minutos / 60)
        minutos = int(minutos % 60)
    print("{}:{}:{}".format(horas, minutos, segundos))
def b1020():
    N = int(input())
    ano = N / 365
    ano = int(ano)
    resto_ano =  N % 365
    mes = resto_ano / 30
    mes = int(mes)
    dia = resto_ano % 30
    print("{} ano(s)".format(ano))
    print("{} mes(es)".format(mes))
    print("{} dia(s)".format(dia))
def b1021():
    n = float(input())
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01];

    print('NOTAS:')
    for i in range(len(notas)):
        qt = 0
        while n-notas[i] >= 0:
            qt += 1
            n -= notas[i]
        print("%d nota(s) de R$ %.2f" % (qt, notas[i]))

    print('MOEDAS:')

    for i in range(len(moedas)):
        qt = 0
        while n-moedas[i] >= 0:
            qt += 1
            n = float(format(round(n - moedas[i],2)))

        print("%d moeda(s) de R$ %.2f" % (qt, moedas[i]))
def b1035():
    linha = input().split()
    a, b, c, d = list(map(int, linha))
    if (b > c and d > a and (a + b) > (c + d) and c >= 0 and d >= 0 and a % 2 == 0):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")
def b1036():
    linha = input().split()
    a, b, c = list(map(float, linha))
    delta = (b*b)-4 * a * c
    raizdelta = delta ** 0.5
    if(a == 0.0 or delta < 0.0):
        print("Impossivel calcular")
    else:
        r1 =((-b) + raizdelta)/(2*a)
        r2 =((-b) - raizdelta)/(2*a)
        print("R1 = {:.5f}".format(r1))
        print("R2 = {:.5f}".format(r2))
    n = float(input())
    if n >= 0 and n <= 25:
        print("Intervalo (0,25]")
    elif n >= 25 and n <= 50:
        print("Intervalo (25,50]")
    elif n >= 50 and n <= 75:
        print("Intervalo (50,75]")
    elif n >= 75 and n <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")
def b1037():
    x = float(input())
    if 0 <= x <= 25:
        print('Intervalo [0,25]')
    if 25 < x <= 50:
        print('Intervalo (25,50]')
    if 50 < x <= 75:
        print('Intervalo (50,75]')
    if 75 < x <= 100:
        print('Intervalo (75,100]')
    if x > 100 or x < 0:
        print('Fora de intervalo')
def b1038():
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x == 1:
        precox = y * 4.00
    elif x == 2:
        precox = y * 4.50
    elif x == 3:
        precox = y * 5.00
    elif x == 4:
        precox = y * 2.00
    elif x == 5:
        precox = y * 1.50
    print("Total: R$ {:.2f}".format(precox))
def b1040():
    n1, n2, n3, n4 = input().split()
    n1= float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1))/10
    if media >= 7:#aprovado
        print("Media: {:.1f}".format(media))
        print("Aluno aprovado.")

    elif media < 7 and media >= 5: #em exame
        exame = float(input())
        exame_media = (media + exame)/2
        if exame_media >= 5:
            print("Media: {:.1f}".format(media))
            print("Aluno em exame.")
            print("Nota do exame: {:.1f}".format(exame))
            print("Aluno aprovado.")
            print("Media final: {:.1f}".format(exame_media))
        else:
            print("Media: {:.1f}".format(media))
            print("Aluno em exame.")
            print("Nota do exame: {:.1f}".format(exame))
            print("Aluno reprovado.")
            print("Media final: {:.1f}".format(exame_media))

    elif media < 5:  #reprovado
        print("Media: {:.1f}".format(media))
        print("Aluno reprovado.")









