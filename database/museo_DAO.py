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
    def read_musei(): #se metto @staticmethod non devo passare il self come parametro
        cnx = ConnessioneDB.get_connection()
        results = []

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM Museo"""

        try:
            cursor.execute(query)
            for row in cursor:
                museo = Museo(id=row["id"], nome=row["nome"], tipologia=row["tipologia"]) #creo oggetti museo
                results.append(museo)
        except Exception as e:
            print("Errore durante la query museo")
            result= None
        finally: #fa quello che scrivo sia che vado nel try sia che vado nell'except
            cursor.close()
            cnx.close()

        return results