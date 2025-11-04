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
    def read_musei(self):
        print("Executing read from database using SQL query")
        results = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            # Una sola query, con cui si leggono tutte le righe (si selezioneranno poi quelle che interessano es. con un if)
            query = """SELECT * 
                        FROM Museo"""
            cursor.execute(query)
            for row in cursor:
                # Posso creare oggetti di tipo Museo
                museo = Museo(row["id"], row["nome"], row["tipologia"])
                results.append(museo)

            cursor.close()
            cnx.close()
            return results