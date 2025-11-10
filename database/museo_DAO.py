from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO

    @staticmethod
    def read_musei():
        print("Executing read from database using SQL query")
        results = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Connection failed")
            return [] #per non avere problemi quando itero per le opzioni della dropdown
        else:
            cursor = cnx.cursor(dictionary=True)
            #leggo tutte le righe e seleziono quelle che mi interessano con un if
            query = """SELECT * 
                        FROM Museo
                        ORDER BY nome"""

            cursor.execute(query)

            for row in cursor:
                museo = Museo(row["id"], row["nome"], row["tipologia"]) #creo oggetti museo
                results.append(museo)

            cursor.close()
            cnx.close()
            return results