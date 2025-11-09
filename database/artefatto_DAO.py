from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def read_artefatti(museo:str, epoca:str):
        print("Executing read from database using SQL query")
        results = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Connection failed")
            return [] #per non avere problemi quando itero per le opzioni della dropdown
        else:
            cursor = cnx.cursor(dictionary=True)
            # Una sola query, con cui si leggono tutte le righe (si selezioneranno poi quelle che interessano es. con un if)
            query = """SELECT * FROM artefatto A JOIN museo M ON A.id_museo = M.id"""

            if museo != "Nessun filtro" and epoca != "Nessun filtro":
                query += f" WHERE M.nome='{museo}' AND A.epoca='{epoca}'"
            elif museo != "Nessun filtro":
                query += f" WHERE M.nome ='{museo}'"
            elif epoca != "Nessun filtro":
                query += f" WHERE A.epoca ='{epoca}'"

            query += " ORDER BY A.nome"

            cursor.execute(query)

            for row in cursor:
                # Posso creare oggetti di tipo Artefatto
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatto)

            cursor.close()
            cnx.close()
            return results

    @staticmethod
    def read_epoche():
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("""SELECT DISTINCT epoca 
                          FROM artefatto 
                          ORDER BY epoca;""")
        epoche = [row["epoca"] for row in cursor]
        cursor.close()
        cnx.close()
        return epoche