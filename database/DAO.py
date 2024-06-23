from database.DB_connect import DBConnect
from model.states import State

class DAO():
    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(s.datetime) as anno
                    from sighting s
                      order by anno"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['anno'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getShape():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct shape
                    from sighting s
                     order by shape"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['shape'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStati():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select *
                       from state s
                        order by id"""
        cursor.execute(query)
        for row in cursor:
            if row['Neighbors'] is not None:
                neighbors = row['Neighbors'].split(' ')
            else:
                neighbors = []
            result.append(State(row['id'], row['Name'], row['Capital'], row['Lat'], row['Lng'], row['Area'], row['Population'], neighbors))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(anno,forma,id1, id2):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as peso
                    from sighting s 
                    where year (`datetime`)= %s and shape =%s and (state=%s   or state =%s)"""
        cursor.execute(query,(anno,forma,id1,id2,))
        for row in cursor:
            result.append((row['peso']))
        cursor.close()
        conn.close()
        if len(result) == 0:
            return 0
        else:
            return result[0]