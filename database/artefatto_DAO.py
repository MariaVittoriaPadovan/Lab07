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
    def get_artefatti_filtrati(museo:str, epoca:str):
        cnx = ConnessioneDB.get_connection()
        results = []

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT a.* 
                    FROM artefatto as a, museo as m 
                    WHERE m.nome= COALESCE(%s, m.nome) and a.epoca=%s and a.id_museo=m.id_museo"""

        '''
        COALESCE(%s, m.nome) valuta se l'attributo è nullo oppure no
        '''

        try:
            cursor.execute(query)
            for row in cursor:
                results.append(row["epoca"])
        except Exception as e:
            print("Errore durante la query artefatto epoca")
            result = None
        finally:  # fa quello che scrivo sia che vado nel try sia che vado nell'except
            cursor.close()
            cnx.close()

        return results

        if cnx is None:
            print("Connection failed")
            return [] #per non avere problemi quando itero per le opzioni della dropdown
        else:
            cursor = cnx.cursor(dictionary=True)
            #leggo tutte le righe e poi seleziono solo quelle che mi interessano con un if
            query = """
            SELECT 
                A.id AS artefatto_id,
                A.nome AS artefatto_nome,
                A.tipologia,
                A.epoca,
                A.id_museo,
                M.nome AS museo_nome
            FROM artefatto A
            JOIN museo M ON A.id_museo = M.id
            """

            if museo != "Nessun filtro" and epoca != "Nessun filtro":
                query += f" WHERE M.nome='{museo}' AND A.epoca='{epoca}'"
            elif museo != "Nessun filtro":
                query += f" WHERE M.nome ='{museo}'"
            elif epoca != "Nessun filtro":
                query += f" WHERE A.epoca ='{epoca}'"

            query += " ORDER BY A.nome"

            cursor.execute(query)

            for row in cursor:
                artefatto = Artefatto( #creo oggetti artefatto
                    row["artefatto_id"],
                    row["artefatto_nome"],
                    row["tipologia"],
                    row["epoca"],
                    row["id_museo"])

                artefatto.museo_nome = row["museo_nome"] #aggiungo il nome del museo

                results.append(artefatto)

            cursor.close()
            cnx.close()
            return results

    @staticmethod
    def get_epoche():
        cnx = ConnessioneDB.get_connection()
        results = []

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT epoca FROM artefatto """

        try:
            cursor.execute(query)
            for row in cursor:
                results.append(row["epoca"])
        except Exception as e:
            print("Errore durante la query artefatto epoca")
            result = None
        finally:  # fa quello che scrivo sia che vado nel try sia che vado nell'except
            cursor.close()
            cnx.close()

        return results
