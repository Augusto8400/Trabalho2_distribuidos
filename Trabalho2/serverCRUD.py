import banco
import Pyro5.server
import Pyro5.core
import Pyro5.api

from agenda_service import AgendaService 
from E_Repositorio import Evento_Repository
from evento import *



@Pyro5.server.expose
class AgendaServer:

    def __init__(self):

        self.banco = banco.BD()

        repository = Evento_Repository(self.banco)

        self.service = AgendaService(repository)

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

        return self.service.criar_evento(
            nome,
            allday,
            dataDe,
            dataAte,
            descricao,
            repetir,
            lembretes
        )

    def buscar_evento(self, id):

        return self.service.buscar_evento(id)

    def buscar_data(self, data):

        return self.service.buscar_data(data)

    def buscar_mes(self, ano, mes):

        return self.service.buscar_mes(ano, mes)

    def buscar_todos(self):

        return self.service.buscar_todos()

    def alterar_data(self, id, dataDe, dataAte):

        return self.service.alterar_data(
            id,
            dataDe,
            dataAte
        )

    def excluir_evento(self, id):

        return self.service.excluir_evento(id)


def main():
    c = AgendaServer()
    
    daemon = Pyro5.api.Daemon()

    Pyro5.api.register_class_to_dict(Evento,converter)
    Pyro5.api.register_dict_to_class("evento.Evento",desconverter)

    
    URI = daemon.register(c)

    print("Servidor iniciado.")
    print(URI)
    ns = Pyro5.core.locate_ns()
    ns.register("agenda",URI)

    daemon.requestLoop()


if __name__ == "__main__":
    main()