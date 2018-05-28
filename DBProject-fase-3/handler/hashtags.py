from flask import jsonify, request
from dao.hashtags import HashtagDAO

class HashtagHandler:
    def mapToDict(self, row):
        result = {}
        result['HTID'] = row[0]
        result['HText'] = row[1]
        return result


    def getAllHashtags(self):
        dao = HashtagDAO()
        result = dao.getAllHashtags()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(
                    self.mapToDict(r))
            return jsonify(Hashtags=mapped_result)

    def getHashtagsById(self,htid):
        dao = HashtagDAO()
        result = dao.getHashtagsById(htid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(
                    self.mapToDict(r))
            return jsonify(Hashtags=mapped_result)

    def getHashtagsByMessageId(self,mid):
        dao = HashtagDAO()
        result = dao.getHashtagsByMessageId(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Hashtags=mapped_result)