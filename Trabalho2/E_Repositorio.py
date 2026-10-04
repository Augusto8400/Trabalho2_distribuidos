class Evento_Repository: # o que conversa com o Banco de dados

    def __init__(self, banco):
        self.banco = banco

    def criar(self, evento):

        return self.banco.inserir(
            evento.nome,
            evento.allday,
            evento.dataDe,
            evento.dataAte,
            evento.descricao,
            evento.repetir,
            evento.lembretes
        )

    def buscar_por_id(self, id):

        return self.banco.buscarUm(id)

    def buscar_por_data(self, data):

        return self.banco.buscarData(data)

    def buscar_por_mes(self, ano, mes):

        return self.banco.buscarMes(ano, mes)

    def buscar_todos(self):

        return self.banco.buscarTodos()

    def atualizar_data(self, id, dataDe, dataAte):

        return self.banco.alterarData(
            dataDe,
            dataAte,
            id
        )

    def excluir(self, id):

        return self.banco.excluir(id)