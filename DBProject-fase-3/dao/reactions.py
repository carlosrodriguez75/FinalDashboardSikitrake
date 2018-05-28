from config.dbconfig import pg_config
import psycopg2


class ReactionDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

        self.conn = psycopg2._connect(connection_url)

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "Select * From Reactions;"  # verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReactionsById(self,rid):
        cursor = self.conn.cursor()
        query = "Select * From Reactions where rid = %s;"  # verificar si corre bien
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllLikes(self):
        cursor = self.conn.cursor()
        query = "Select * From Reactions where MReaction = TRUE;"  # verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllDislikes(self):
        cursor = self.conn.cursor()
        query = "Select * From Reactions where MReaction = FALSE;"  # verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReactionsbyMessageID(self,mid):
        cursor = self.conn.cursor()
        query = "Select rid, mreaction, uid, mid, udispname from Reactions inner join Users using(uid) where mid = %s order by mreaction desc;"  # verificar si corre bien
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllLikesByMessageID(self,mid):
        cursor = self.conn.cursor()
        query = "Select * from Reactions where mid = %s AND mreaction = TRUE;"  # verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllDislikesByMessageID(self,mid):
        cursor = self.conn.cursor()
        query = "Select * from Reactions where mid = %s AND mreaction = FALSE;"  # verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfLikesByMessageID(self,mid):
        cursor = self.conn.cursor()
        query = "Select count(*) from Reactions where mid = %s AND mreaction = TRUE;"  # verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfDislikesByMessageID(self,mid):
        cursor = self.conn.cursor()
        query = "Select count(*) from Reactions where mid = %s AND mreaction = FALSE;"  # verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Phase III
    def insertReactioninMessage(self, MReaction, UID, MID):
        cursor = self.conn.cursor()
        query = "insert into reactions (mreaction, uid, mid) " \
                "values (%s,%s,%s) " \
                "returning rid; "
        cursor.execute(query, (MReaction, UID, MID, ))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result

    def updateReactioninMessage(self, MReaction, UID, MID):
        cursor = self.conn.cursor()
        query = "update reactions " \
                "set mreaction = %s, uid = %s, mid = %s " \
                "where UID = %s and MID = %s ; "
        cursor.execute(query, (MReaction, UID, MID, UID, MID ))
        result = 'Sucess'
        self.conn.commit()
        return result

    def validateReaction(self, UID, MID):
        cursor = self.conn.cursor()
        query = "select * " \
                "from reactions " \
                "where uid = %s and mid = %s; "  # verificar si corre bien
        cursor.execute(query, (UID, MID, ))
        result = cursor.fetchone()
        print ('result : ', result)
        return result