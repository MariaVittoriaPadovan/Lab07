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
                    WHERE m.nome= COALESCE(%s, m.nome) and a.epoca=COALESCE(%s, a.epoca) and a.id_museo=m.id_museo"""

        '''
        COALESCE(%s, m.nome) serve perché nel caso in cui %s sia nullo lui lo pone uguale a m.nome che gli sto passando
        '''

        try:
            cursor.execute(query, (museo,epoca,)) #è importante l'ordine per museo e epoca
            for row in cursor:
                artefatto = Artefatto(  # creo oggetti artefatto
                    id= row["artefatto_id"],
                    nome= row["artefatto_nome"],
                    tipologia= row["tipologia"],
                    epoca= row["epoca"],
                    id_museo= row["id_museo"])
                results.append(artefatto)

        except Exception as e:
            print("Errore durante la query artefatto filtrato")
            result = None
        finally:  # fa quello che scrivo sia che vado nel try sia che vado nell'except
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
