#/////////////////////##/////////////////////##/////////////////////#
chegada = input("Horario da chegada: 'Horas e minutos': ").split()
saida = input("Horario da saida: 'Horas e minutos': ").split()
hora_chegada, min_chegada = list(map(int, chegada))
hora_saida, min_saida = list(map(int, saida))
#/////////////////////##/////////////////////##/////////////////////#
#Calculo das horas
hora = hora_chegada - hora_saida
hora_pos = abs(hora)
min = min_chegada - min_saida
min_pos = abs(min)
#/////////////////////##/////////////////////##/////////////////////#
#variaveis fixas#
valor = 5
multa = 1
total = 0
#/////////////////////##/////////////////////##/////////////////////#
#descobrindo a hora exata e convertendo para minutos
if hora > 0:
    hora_f = 24 - hora
elif hora < 0:
    hora_f = abs(hora)
else:
    hora_f = 0
aux_min = hora_f * 60
#/////////////////////##/////////////////////##/////////////////////#
#descobrindo os minutos exatas e somando com os minutos das horas
if min < 0:
    min_f = abs(min) + aux_min
elif min > 0:
    min_f = min + aux_min
else:
    min_f = 0 + aux_min
#/////////////////////##/////////////////////##/////////////////////#
#calculando o total
if min_f <= 60 and min_f > 0:
    total = valor
elif min_f <= 120 and min_f > 60:
    total = valor * 2
elif min_f > 120:
    aux = min_f/60
    aux_2 = min_f%60
    if aux > 2:
        if aux_2 > 0:
            aux = int(aux)
            aux = aux + 1
            total = (aux * valor) + (multa * (aux - 2))
        else:
            aux = int(aux)
            total = (aux * valor) + (multa * (aux - 2))
#/////////////////////##/////////////////////##/////////////////////#
#resposta
print("o carro ficou estacionado por {} horas e {} minutos, vai pagar o total de {:.2f} R$".format(hora_pos, min_pos, total))