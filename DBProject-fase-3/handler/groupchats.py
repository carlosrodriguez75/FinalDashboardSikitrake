from flask import jsonify, request
from dao.groupchats import GroupChatDAO
import datetime

class GroupChatHandler:
    def mapToDict(self, row):
        result = {}
        result['GID'] = row[0]
        result['GName'] = row[1]
        result['GCDate'] = row[2]
        result['GOwner'] = row[3]
        return result

    def mapToDictIdtoName(self,row):
        result = {}
        result['GName'] = row
        return result

    def mapToDictInfoByName(self,row):
        result = {}
        result['GID'] = row[0]
        result['GCDATE'] = row[1]
        result['GOwner'] = row[2]
        return result
    def mapToDictInfoByOwner(self,row):
        result = {}
        result['UID'] = row[0]
        result['GID'] = row[1]
        result['GName'] = row[2]
        return result

    def insert_NewChatGroup_dict(self, GName, GCDate, UID):
        result = {}
        result['GName'] = GName
        result['GCDATE'] = GCDate
        result['UID'] = UID
        return result

    def insert_Participant_dict(self, GID, UID):
        result = {}
        result['GID'] = GID
        result['UID'] = UID
        return result

    def getAllGroupChats(self):
        dao = GroupChatDAO()
        result = dao.getAllGroupChats()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(
                    self.mapToDict(r))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatsByName(self,name):
        dao = GroupChatDAO()
        result = dao.getGroupChatsByName(name)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(
                    self.mapToDict(r))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatsById(self,gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatsById(gid)
        if(result == None):
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatNameById(self,gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatNameById(gid)
        if(result == None):
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            mapped_result.append(self.mapToDictIdtoName(result))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatInfoByName(self,name):
        dao = GroupChatDAO()
        result = dao.getGroupChatInfoByName(name)
        if(result == None):
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictInfoByName(r))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatsByUsername(self,name):
        dao = GroupChatDAO()
        result = dao.getGroupChatsByUsername(name)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(
                    self.mapToDict(r))
            return jsonify(GroupChats=mapped_result)

    #Phase III
    def getGroupChatByUserID(self, form):
        uid = form['UID']
        dao = GroupChatDAO()
        result = dao.getGroupChatByUserID(uid)
        if (result == None):
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictInfoByOwner(r))
            return jsonify(GroupChatsByOwner=mapped_result)

    def insertNewChatGroup(self, form):
        dao = GroupChatDAO()
        if len(form) != 2:
            return jsonify(Error="Malformed insert request"), 400
        else:
            GName = form['GName']
            GCDate = datetime.datetime.today().strftime('%d-%m-%Y')
            UID = form['UID']
            if GName and GCDate and UID :
                row = dao.insertNewChatGroup(GName, GCDate, UID)
                if row == None:
                    return jsonify(Error="Invalid Insert"), 404
                else:
                    GID = row
                    print ('GID : ', GID)
                    dao.insertParticipant(GID, UID)
                    result = self.insert_NewChatGroup_dict(GName, GCDate, UID)
                    return jsonify(User=result)
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def insertParticipant(self, form):
        dao = GroupChatDAO()
        if len(form) != 3:
            return jsonify(Error="Malformed insert request"), 400
        else:
            GID = form['GID']
            UID = form['UID']
            CUID = form['CUID']
            if GID and UID :
                validate = dao.validateContact(UID, CUID)
                if (validate == None):
                    return jsonify(Error="Not a Contact"), 404
                row = dao.insertParticipant(GID, CUID)
                if row == None:
                    return jsonify(Error="Invalid Insert"), 404
                else:
                    #result = self.insert_NewChatGroup_dict(GID, UID)
                    return jsonify(User="Success")
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400


