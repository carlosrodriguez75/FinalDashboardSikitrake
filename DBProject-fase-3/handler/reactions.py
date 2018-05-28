
from flask import jsonify, request
from dao.reactions import ReactionDAO

class ReactionHandler:
    def mapToDict(self, row):
        result = {}
        result['RID'] = row[0]
        result['MReaction'] = row[1]
        result['UID'] = row[2]
        result['MID'] = row[3]
        return result

    def mapToDictVariant(self, row):
        result = {}
        result['RID'] = row[0]
        reaction = ""
        if row[1] == True:
            result['MReaction'] = "Liked"
        else:
            result['MReaction'] = "Disliked"
        result['UID'] = row[2]
        result['MID'] = row[3]
        result['Name'] = row[4]
        return result

    def mapToDictNumberOfLikesOrDislikes(self,row):
        result = {}
        result['Total'] = row[0]
        return result

    def mapToDictNumberOfLikesAndDislikes(self,row):
        result={}
        result['MID'] = row[0]
        result['Likes'] = row[1]
        result['Dislikes'] = row[2]
        return result

    def ReactioninMessage_dict(self, MReaction, UID, MID):
        result = {}
        result['MID'] = MID
        result['UID'] = UID
        if MReaction == True:
            result['MReaction'] = "Liked"
        else:
            result['MReaction'] = "Disliked"
        return result

    def getAllReactions(self):
        dao = ReactionDAO()
        result = dao.getAllReactions()
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getReactionsById(self,rid):
        dao = ReactionDAO()
        result = dao.getReactionsById(rid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getAllLikes(self):
        dao = ReactionDAO()
        result = dao.getAllLikes()
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getAllDislikes(self):
        dao = ReactionDAO()
        result = dao.getAllDislikes()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getAllReactionsbyMessageID(self,mid):
        dao = ReactionDAO()
        result = dao.getAllReactionsbyMessageID(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictVariant(r))
            return jsonify(Reactions=mapped_result)

    def getAllLikesByMessageID(self,mid):
        dao = ReactionDAO()
        result = dao.getAllLikesByMessageID(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getAllDislikesByMessageID(self,mid):
        dao = ReactionDAO()
        result = dao.getAllDislikesByMessageID(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getNumberOfLikesByMessageID(self,mid):
        dao = ReactionDAO()
        result = dao.getNumberOfLikesByMessageID(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictNumberOfLikesOrDislikes(r))
            return jsonify(Reactions=mapped_result)

    def getNumberOfDislikesByMessageID(self,mid):
        dao = ReactionDAO()
        result = dao.getNumberOfDislikesByMessageID(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictNumberOfLikesOrDislikes(r))
            return jsonify(Reactions=mapped_result)

    #Phase III
    def insertLikeinMessage(self, form):
        dao = ReactionDAO()
        if len(form) != 2:
            return jsonify(Error="Malformed insert request"), 400
        else:
            UID = form['UID']
            MID = form['MID']
            validate = dao.validateReaction(UID, MID)
            if validate == None:
                MReaction = True
                if UID and MID :
                    row = dao.insertReactioninMessage(MReaction, UID, MID)
                    if row == None:
                        return jsonify(Error="Invalid Insert"), 404
                    else:
                        result = self.ReactioninMessage_dict(MReaction, UID, MID)
                        return jsonify(Like=result)
                else:
                    return jsonify(Error="Unexpected attributes in insert request"), 400
            else:
                return self.updateLikeinMessage(form)

    def updateLikeinMessage(self, form):
        dao = ReactionDAO()
        if len(form) != 2:
            return jsonify(Error="Malformed insert request"), 400
        else:
            MReaction = True
            UID = form['UID']
            MID = form['MID']
            if UID and MID :
                row = dao.updateReactioninMessage(MReaction, UID, MID)
                if row == None:
                    return jsonify(Error="Invalid Update"), 404
                else:
                    result = self.ReactioninMessage_dict(MReaction, UID, MID)
                    return jsonify(Like=result)
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def insertDislikeinMessage(self, form):
        dao = ReactionDAO()
        if len(form) != 2:
            return jsonify(Error="Malformed insert request"), 400
        else:
            UID = form['UID']
            MID = form['MID']
            validate = dao.validateReaction(UID, MID)
            if validate == None:
                MReaction = False
                if UID and MID :
                    row = dao.insertReactioninMessage(MReaction, UID, MID)
                    if row == None:
                        return jsonify(Error="Invalid Insert"), 404
                    else:
                        result = self.ReactioninMessage_dict(MReaction, UID, MID)
                        return jsonify(Dislike=result)
                else:
                    return jsonify(Error="Unexpected attributes in insert request"), 400
            else:
                return self.updateDislikeinMessage(form)

    def updateDislikeinMessage(self, form):
        dao = ReactionDAO()
        if len(form) != 2:
            return jsonify(Error="Malformed insert request"), 400
        else:
            MReaction = False
            UID = form['UID']
            MID = form['MID']
            if UID and MID :
                row = dao.updateReactioninMessage(MReaction, UID, MID)
                if row == None:
                    return jsonify(Error="Invalid Update"), 404
                else:
                    result = self.ReactioninMessage_dict(MReaction, UID, MID)
                    return jsonify(Dislike=result)
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400
