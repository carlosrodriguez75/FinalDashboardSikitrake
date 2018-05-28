from flask import jsonify, request
from dao.Users import UsersDAO

class UsersHandler:

    def mapToDict(self,row):
        result = {}
        result['UID'] = row[0]
        result['UDispName'] = row[1]
        result['UPassword'] = row[2]
        result['UFirst_Name'] = row[3]
        result['ULast_Name'] = row[4]
        result['UPhone'] = row[5]
        result['UEmail'] = row[6]
        return result

    def mapToDictContactByID(self,row):
        result = {}
        result['UID'] = row[0]
        result['UDispName'] = row[1]
        result['CID'] = row[2]
        result['UContactDispName'] = row[3]
        return result

    def mapToDictUsersByGroup(self,row):
        result = {}
        result['UID'] = row[0]
        result['UDispName'] = row[1]
        return result

    def insert_user_dict(self, UDispName, UPassword, UFirst_name, ULast_name, UPhone, UEmail, uid):
        result = {}
        result['UDispName'] = UDispName
        result['UPassword'] = UPassword
        result['UFirst_name'] = UFirst_name
        result['ULast_name'] = ULast_name
        result['UPhone'] = UPhone
        result['UEmail'] = UEmail
        result['UID'] = uid
        return result


    def getAllUsers(self):
        dao = UsersDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getUsersByUId(self, UID):
        dao = UsersDAO()
        result = dao.getUsersByUId(UID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getUsersByPhone(self,phone):
        dao = UsersDAO()
        result = dao.getUsersByPhone(phone)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getUsersByEmail(self,email):
        dao = UsersDAO()
        result = dao.getUsersByEmail(email)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getContactsByUserID(self,UID):
        dao = UsersDAO()
        result = dao.getContactsByUserID(UID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictContactByID(r))
            return jsonify(Users=mapped_result)

    def getUsersInGroupChatByID(self,gid):
        dao = UsersDAO()
        result = dao.getUsersInGroupChatByID(gid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictUsersByGroup(r))
            return jsonify(Users=mapped_result)

    def getUsersInGroupChatByName(self,name):
        dao = UsersDAO()
        result = dao.getUsersInGroupChatByName(name)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictUsersByGroup(r))
            return jsonify(Users=mapped_result)

    def getUserByUsername(self,uname):
        dao = UsersDAO()
        result = dao.getUserByUsername(uname)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getUsersThatLikedMessage(self,mid):
        dao = UsersDAO()
        result = dao.getUsersThatLikedMessage(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getUsersThatDislikedMessage(self,mid):
        dao = UsersDAO()
        result = dao.getUsersThatDislikedMessage(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getGroupChatOwnerByName(self,gname):
        dao = UsersDAO()
        result = dao.getGroupChatOwnerByName(gname)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getGroupChatOwnerByID(self,gid):
        dao = UsersDAO()
        result = dao.getGroupChatOwnerByID(gid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    # Phase III #
    def login(self, form):
        dao = UsersDAO()
        UDispName = form['UDispName']
        UPassword = form['UPassword']
        result = dao.login(UDispName, UPassword)
        if result == None:
            return jsonify(Error="Invalid Login"), 404
        else:
            return jsonify(Login=1)

    def insertUser(self, form):
        dao = UsersDAO()
        if len(form) != 6:
            return jsonify(Error="Malformed insert request"), 400
        else:
            UDispName = form['UDispName']
            UPassword = form['UPassword']
            UFirst_name = form['UFirst_name']
            ULast_name = form['ULast_name']
            UPhone = form['UPhone']
            UEmail = form['UEmail']
            if UDispName and UPassword and UFirst_name and UFirst_name \
                and ULast_name and UPhone and UEmail:
                validate = dao.validateUDispName(UDispName)
                if validate != None:
                    return jsonify(Error="User Exist"), 404
                row = dao.insertUser(UDispName, UPassword, UFirst_name, ULast_name, UPhone, UEmail)
                if row == None:
                    return jsonify(Error="Query Fail"), 404
                else:
                    result = self.insert_user_dict(UDispName, UPassword, UFirst_name, ULast_name, UPhone, UEmail, row)
                    return jsonify(User=result)
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def insertContact(self, form):
        dao = UsersDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            UID = form['UID']
            UFirst_name = form['UFirst_name']
            ULast_name = form['ULast_name']
            UPhone = form['UPhone']
            UEmail = form['UEmail']
            if UFirst_name and ULast_name and (UPhone or UEmail):
                validate = dao.validateUser(UFirst_name, ULast_name, UPhone, UEmail)
                if validate == None:
                    return jsonify(Error="User Do't Exist"), 404
                row = dao.insertContact(UID, validate[0])
                if row == None:
                    return jsonify(Error="Query Fail"), 404
                else:
                    return jsonify(User="Success")
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400
