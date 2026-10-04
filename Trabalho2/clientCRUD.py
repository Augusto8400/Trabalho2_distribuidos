import Pyro5.core
import Pyro5.api

from evento import *


menu_principal = """
=================
     Agenda
=================

Digite:

    1 - para criar evento;
    2 - para editar evento;
    3 - para excluir evento;
    4 - para mostrar eventos do dia;
    5 - para mostrar eventos do mês;
    6 - para mostrar todos os eventos;
    0 - para sair

-> Escolha: """

menu_allday = """Evento dia todo?

    0 - Não;
    1 - Sim.

-> Escolha: """

menu_ciclo = """
Repetir o evento?

    01 - Evento unico;        04 - Semanalmente
    02 - Diariamente;         05 - Mensalmente
    03 - Dias uteis;          06 - Anualmente

-> Escolha: """

menu_lembretes = """
Adicionar lembretes?

    01 - Nenhum lembrete;     06 - 1 hora antes;
    02 - Antes do evento;     07 - 4 horas antes;
    03 - 5 minutos antes;     08 - 1 dia antes;
    04 - 15 minutos antes;    09 - 2 dias antes
    05 - 30 minutos antes;    10 - 1 semana antes.

-> Escolha: """

str_not_found = 'Nenhum evento encontrado'
str_quant = 'Quantidade de evento(s) encontrado(s):'


def mostrar_eventos(eventos):

    if eventos:

        print('\n')
        print('-' * (len(str_quant) + 8))
        print('| ', str_quant, len(eventos), ' |')
        print('-' * (len(str_quant) + 8))

        for evento in eventos:

            print('     ID:', evento.id)
            print('     Evento:', evento.nome)
            print('     De:', evento.dataDe)
            print('     Ate:', evento.dataAte)
            print('     Descricao:', evento.descricao)

            print('-' * (len(str_quant) + 8))

        return True

    else:

        print('-' * (len(str_not_found) + 8))
        print('|  ', str_not_found, '  |')
        print('-' * (len(str_not_found) + 8))

        return None


def main():

    ns = Pyro5.core.locate_ns()

    uri = ns.lookup("agenda")

    agenda = Pyro5.api.Proxy(uri)

    print("Conectado ao servidor.\n")

    op = None

    while op != 0:

        op = int(input(menu_principal))

        if op == 1:

            nomeE = input('Digite o nome do evento: ')

            allday = int(input(menu_allday))

            while allday not in (0, 1):

                print('ERRO. Escolha entre as opcoes validas\n')
                allday = int(input(menu_allday))

            if allday == 1:

                data_de = input('De [DD/MM/AAAA]: ')
                data_ate = input('As [DD/MM/AAAA]: ')

            else:

                data_de = input('De [DD/MM/AAAA HH:MM]: ')
                data_ate = input('As [DD/MM/AAAA HH:MM]: ')

            descricao = input('Descricao do evento: ')

            ciclo = int(input(menu_ciclo))

            while ciclo not in range(1, 7):

                print('ERRO. Escolha entre as opcoes validas\n')
                ciclo = int(input(menu_ciclo))

            lembretes = int(input(menu_lembretes))

            while lembretes not in range(1, 11):

                print('ERRO. Escolha entre as opcoes validas')
                lembretes = int(input(menu_lembretes))

            evento = agenda.criar_evento(
                nomeE,
                allday,
                data_de,
                data_ate,
                descricao,
                ciclo,
                lembretes
            )

            if evento:

                print('\n')
                print('-' * (len('Evento cadastrado com sucesso') + 8))
                print('|   Evento cadastrado com sucesso   |')
                print('-' * (len('Evento cadastrado com sucesso') + 8))

                print("ID:", evento.id)

            else:

                print('\n')
                print('-' * (len('Erro no cadastro do evento') + 8))
                print('|   Erro no cadastro do evento   |')
                print('-' * (len('Erro no cadastro do evento') + 8))

        elif op == 2:

            escolhaID = int(
                input('Digite o ID do evento a ser alterado: ')
            )

            evento = agenda.buscar_evento(escolhaID)

            if evento is None:

                mostrar_eventos([])

                continue

            print('\n')
            print('-' * (len('Evento selecionado:') + 8))
            print('|   Evento selecionado:   |')
            print('-' * (len('Evento selecionado:') + 8))

            print('     ID:', evento.id)
            print('     Evento:', evento.nome)
            print('     De:', evento.dataDe)
            print('     Ate:', evento.dataAte)
            print('     Descricao:', evento.descricao)

            print('-' * (len('Evento selecionado:') + 10))

            dataNovaDe = input(
                '(Novo) De [DD/MM/AAAA HH:MM]: '
            )

            dataNovaAte = input(
                '(Novo) Ate [DD/MM/AAAA HH:MM]: '
            )

            resultado = agenda.alterar_data(
                escolhaID,
                dataNovaDe,
                dataNovaAte
            )

            if resultado:

                print('\n')
                print(
                    '-' * (len('ID 00 alterado com sucesso') + 8)
                )

                print(
                    "| ID",
                    escolhaID,
                    "alterado com sucesso |"
                )

                print(
                    '-' * (len('ID 00 alterado com sucesso') + 8)
                )

        elif op == 3:

            escolhaID = int(
                input('Digite o ID a ser excluido: ')
            )

            resultado = agenda.excluir_evento(escolhaID)

            if resultado:

                print(
                    '-' * (len("Evento excluido com sucesso") + 8)
                )

                print(
                    '|  Evento excluido com sucesso  |'
                )

                print(
                    '-' * (len("Evento excluido com sucesso") + 8)
                )

            else:

                mostrar_eventos([])

        elif op == 4:

            dataAlvo = input(
                'Data [DD/MM/AAAA]: '
            )

            # Chamada remota
            eventos = agenda.buscar_data(dataAlvo)

            mostrar_eventos(eventos)

        elif op == 5:

            mesAlvo = input(
                'Mes [MM/AAAA]: '
            )

            # Separa MM/AAAA
            mes = mesAlvo[0:2]
            ano = mesAlvo[3:7]

            # Chamada remota
            eventos = agenda.buscar_mes(
                ano,
                mes
            )

            mostrar_eventos(eventos)

        elif op == 6:

            # Chamada remota
            eventos = agenda.buscar_todos()

            mostrar_eventos(eventos)

        elif op != 0:

            print("Opcao invalida.")

    print("Encerrando agenda.")


if __name__ == "__main__":
    main()