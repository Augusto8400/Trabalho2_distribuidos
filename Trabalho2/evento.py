class Evento: # definimos a estrutura de como os dados estão armazenadas 
    # facilitar a ideia de Orientados a Objetos 

    def __init__(
        self,
        id,
        nome,
        allday,
        dataDe,
        dataAte,
        descricao,
        repetir,
        lembretes
    ):
        self.id = id
        self.nome = nome
        self.allday = allday
        self.dataDe = dataDe
        self.dataAte = dataAte
        self.descricao = descricao
        self.repetir = repetir
        self.lembretes = lembretes
       
def converter(evento):
    return {
        "id": evento.id,
        "nome": evento.nome,
        "allday": evento.allday,
        "dataDe": evento.dataDe,
        "dataAte": evento.dataAte,
        "descricao": evento.descricao,
        "repetir": evento.repetir,
        "lembretes": evento.lembretes
    }
    
def desconverter(classname, dados):
    return Evento(
        dados["nome"],
        dados["allday"],
        dados["dataDe"],
        dados["dataAte"],
        dados["descricao"],
        dados["repetir"],
        dados["lembretes"],
        dados["id"]
    )