class AgendaService:

    def __init__(self, repository):

        self.repository = repository

    def criar_evento(
        self,
        nome,
        allday,
        dataDe,
        dataAte,
        descricao,
        repetir,
        lembretes
    ):

        evento = Evento(
            None,
            nome,
            allday,
            dataDe,
            dataAte,
            descricao,
            repetir,
            lembretes
        )

        return self.repository.criar(evento)

    def buscar_evento(self, id):

        return self.repository.buscar_por_id(id)

    def buscar_data(self, data):

        return self.repository.buscar_por_data(data)

    def buscar_mes(self, ano, mes):

        return self.repository.buscar_por_mes(ano, mes)

    def buscar_todos(self):

        return self.repository.buscar_todos()

    def alterar_data(self, id, dataDe, dataAte):

        return self.repository.atualizar_data(
            id,
            dataDe,
            dataAte
        )

    def excluir_evento(self, id):

        return self.repository.excluir(id)