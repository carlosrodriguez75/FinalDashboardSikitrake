from config.dbconfig import pg_config
import psycopg2

class HashtagDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

        self.conn = psycopg2._connect(connection_url)

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "Select * From Hashtags;" #verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagsById(self,htid):
        cursor = self.conn.cursor()
        query = "Select * From Hashtags Where HTID = %s;" #verificar si corre bien
        cursor.execute(query, (htid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagsByMessageId(self,mid):
        cursor = self.conn.cursor()
        query = "Select htid, htext From Hashtags natural inner join HasHashtags where mid = %s;" #verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByHashtags(self,hashtags):
        cursor = self.conn.cursor()
        query = "Select * From Hashtags Where HText = %s;" #verificar si corre bien
        cursor.execute(query, (hashtags,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Phase III
    def insertHashtag(self, htext, mid):
        cursor = self.conn.cursor()
        query = "insert into hashtags (htext, mid) " \
                "values (%s,%s) " \
                "returning htid; "
        cursor.execute(query, (htext, mid, ))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result