import sqlite3
from calendar import monthrange

class BD:

    def __init__(self):
        self.con = sqlite3.connect("agenda.db", check_same_thread=False)
        cursor = self.con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS crud(id INTEGER PRIMARY KEY, nomeEvento, diaTodo, dataDe, dataAte, descricao,repetir, lembre)')
        self.con.commit()
        cursor.close()

    def __del__(self):
        self.con.close()

    def inserir(self, nomeEvento, diaTodo, dataDe, dataAte, descricao, repetir, lembre):
        cursor = self.con.cursor()
        cursor.execute('INSERT INTO crud(nomeEvento, diaTodo, dataDe, dataAte, descricao, repetir, lembre) VALUES(?, ?, ?, ?, ?, ?, ?)', (nomeEvento, diaTodo, dataDe, dataAte, descricao, repetir, lembre))
        if (cursor.rowcount > 0):
            self.con.commit()
            id = cursor.lastrowid
        else:
            id = None
        cursor.close()
        return id
    
    def excluir(self, id):
        cursor = self.con.cursor()
        cursor.execute('DELETE FROM crud WHERE id = ?', (id,))
        dado = cursor.rowcount
        self.con.commit()
        cursor.close()
        return dado

    def buscarUm(self, id):
        cursor = self.con.cursor()
        cursor.execute('SELECT * FROM crud WHERE id = ?', (id,))
        dado = cursor.fetchone()
        cursor.close()
        return dado

    def alterarData(self,dataDe, dataAte, id):
        cursor = self.con.cursor()
        cursor.execute('UPDATE crud SET dataDe = ?, dataAte = ? WHERE id = ?', (dataDe, dataAte, id))
        self.con.commit()
        cursor.close()

    def buscarData(self, data):
        print("DATA RECEBIDA:", repr(data))

        data_convertida = data[6:10] + '-' + data[3:5] + '-' + data[0:2]

        print("DATA CONVERTIDA:", repr(data_convertida))

        comando = """
            SELECT *
            FROM crud
            WHERE substr(dataDe, 7, 4) || '-' ||
                substr(dataDe, 4, 2) || '-' ||
                substr(dataDe, 1, 2) <= ?
            AND
                substr(dataAte, 7, 4) || '-' ||
                substr(dataAte, 4, 2) || '-' ||
                substr(dataAte, 1, 2) >= ?
        """

        cursor = self.con.cursor()
        cursor.execute(comando, (data_convertida, data_convertida))
        dado = cursor.fetchall()

        print("RESULTADO:", dado)

        cursor.close()
        return dado

    def buscarMes(self, ano, mes):
        comando = """
                SELECT *
                FROM crud
                WHERE  substr(dataDe, 7, 4) || '-' ||
                       substr(dataDe, 4, 2) || '-' ||
                       substr(dataDe, 1, 2)
                       <= ?
                AND
                       substr(dataAte, 7, 4) || '-' ||
                       substr(dataAte, 4, 2) || '-' ||
                       substr(dataAte, 1, 2)
                       >= ?
        """
        ultimo_dia = monthrange(int(ano), int(mes))[1]

        inicio_mes = f'{ano}-{mes}-01'
        fim_mes = f'{ano}-{mes}-{ultimo_dia:02d}'
        
        cursor = self.con.cursor()
        cursor.execute(comando, (fim_mes, inicio_mes))
        dado = cursor.fetchall()
        cursor.close()
        return dado

    def buscarTodos(self):
        cursor = self.con.cursor()
        cursor.execute('SELECT * FROM crud')
        dado = cursor.fetchall()
        cursor.close()
        return dado

