quartos_vagos = [101, 102, 103, 104, 105]
quartos_reservados = []
nome = []
dia = []
mes = []
def home():
    while True:
        print("\t\t\t\t\t\t BEM VINDO AO HOTEL HOTEL")
        print("1.Reservar Quarto\n2.Cancelar Reserva\n3.Fechar Reserva\n4.Cadastrar Quarto\n0.Sair\n")
        quartos_vagos.sort()
        esc = int(input())
        if esc == 1:
            print(" ")
            reservar()
        elif esc == 2:
            print(" ")
            cancelar_reserva()
        elif esc == 3:
            print(" ")
            fechar_reserva()
        elif esc == 4:
            print(" ")
            criar_quarto()
        else:
            if esc == 0:
                print("")
                break


def reservar():
    print("\t\t\t\t\t\t CRIAR UMA RESERVA\n")
    print("Quartos vagos ",quartos_vagos)
    print("Quartos_reservados ",quartos_reservados)
    print(" ")
    while True:
        nomeh = str(input("Digite o Nome: "))
        mesh = int(input("Digite o mês: "))
        diah = int(input("Digite o dia: "))
        quartoh = int(input("Digite o numero do quarto: "))
        if quartoh in quartos_vagos:
            nome.append(nomeh)
            mes.append(mesh)
            dia.append(diah)
            quartos_reservados.append(quartoh)
            quartos_vagos.remove(quartoh)
            break
            home()

def criar_quarto():
    while True:
        quarto_novo = int(input("Digite o Numero do quarto"))
        if quarto_novo in quartos_vagos or quarto_novo in quartos_vagos:
            print("Quarto já existente")
        else:
            quartos_vagos.append(quarto_novo)
            posicao = quartos_vagos.index(quarto_novo)
            print(posicao)
            break
            home()
def cancelar_reserva():
    while True:
        print("\t\t\t\t\t\t BEM VINDO AO HOTEL HOTEL\n")
        print("hospedes dos quartos", nome)
        print("Quartos reservados",quartos_reservados)
        quarto = int(input())
        indice = quartos_reservados.index(quarto)
        nomex = nome[indice]
        diax = dia[indice]
        mesx = mes[indice]
        if quarto in quartos_reservados:
            nome.remove(nomex)
            dia.remove(diax)
            mes.remove(mesx)
            quartos_vagos.append(quarto)
            quartos_reservados.remove(quarto)
            break
            home()
def fechar_reserva():
    while True:
        print("\t\t\t\t\t\t FECHAR UMA RESERVA\n")
        print(nome)
        print(quartos_reservados)
        quarto = int(input("número do quarto: "))
        if quarto in quartos_reservados :
            pos = quartos_reservados.index(quarto)
            nomex = nome[pos]
            diax = dia[pos]
            mesx = mes[pos]
            print("Mês de entrada {}".format(mesx))
            mes_de_saida = int(input("mês de saida: "))
            print("Dia de entrada {}".format(diax))
            dia_de_saida = int(input("dia de saida: "))
            meses = mes_de_saida - mesx
            if meses > 0:
                dias_total = (365 - (meses * 30)) + (dia_de_saida - diax)
                total = dias_total * 50
                print("O hospede'{}' ficou hospedado por {}".format(nomex, dias_total))
                print("O valor da estadia é de {:.2f}R$".format(total))
                aux = int(input("digite 1 para voltar ao menu\n"))
                nome.remove(nomex)
                dia.remove(diax)
                mes.remove(mesx)
                quartos_vagos.append(quarto)
                quartos_reservados.remove(quarto)
                break
                home()
            else:
                meses = abs(meses)
                dias_total = (meses * 30) + (dia_de_saida - diax)
                total = dias_total * 50
                print("O hospede'{}' ficou hospedado por {}".format(nomex,dias_total))
                print("O valor da estadia é de {:.2f}R$".format(total))
                aux = int(input("digite 1 para voltar ao menu\n"))
                nome.remove(nomex)
                dia.remove(diax)
                mes.remove(mesx)
                quartos_vagos.append(quarto)
                quartos_reservados.remove(quarto)
                break
                home()

        else:
            print("não há quartos reservados")
            break
            home()

home()