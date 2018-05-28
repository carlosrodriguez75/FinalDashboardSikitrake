from config.dbconfig import pg_config
import psycopg2

class GroupChatDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

        self.conn = psycopg2._connect(connection_url)

    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = "Select * from groupchats;"  # verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatsByName(self,name):
        cursor = self.conn.cursor()
        query = "Select * from groupchats where gname = %s;"  # verificar si corre bien
        cursor.execute(query,(name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatsById(self,gid):
        cursor = self.conn.cursor()
        query = "Select * from groupchats where gid = %s;"  # verificar si corre bien
        cursor.execute(query,(gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatsByUsername(self,name):
        cursor = self.conn.cursor()
        query = "Select GID, GName, GCDate, G.UID from (groupchats as G inner join participates as P using(gid)), Users as U where P.uid = U.uid AND UDispName = %s;"  # verificar si corre bien
        cursor.execute(query,(name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatNameById(self,gid):
        cursor = self.conn.cursor()
        query = "Select gname from groupchats where gid = %s;"  # verificar si corre bien
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatInfoByName(self,name):
        cursor = self.conn.cursor()
        query = "Select gid, gcdate, uid From groupchats where gname = %s;"  # verificar si corre bien
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    # Phase III
    def getGroupChatByUserID(self,uid):
        cursor = self.conn.cursor()
        query = "select p.uid, p.gid, g.gname " \
                "from participates as p, groupchats as g " \
                "where p.gid = g.gid and p.uid = %s; "
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertNewChatGroup(self, GName, GCDate, UID):
        cursor = self.conn.cursor()
        query = "insert into groupchats (gname, gcdate, uid) " \
                "values (%s,%s,%s) " \
                "returning gid; "
        cursor.execute(query, (GName, GCDate, UID, ))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result

    def insertParticipant(self, GID, UID):
        cursor = self.conn.cursor()
        query = "insert into participates (gid, uid) " \
                "values (%s,%s) " \
                "returning gid; "
        cursor.execute(query, (GID, UID, ))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result

    def validateContact(self, UID, CUID):
        cursor = self.conn.cursor()
        query = "select uid " \
                "from contacts " \
                "where uid = %s and cuid = %s; "
        cursor.execute(query, (UID, CUID, ))
        result = cursor.fetchone()
        return result


