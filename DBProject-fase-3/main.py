from flask import Flask, jsonify, request
from handler.reactions import ReactionHandler
from handler.groupchats import GroupChatHandler
from handler.Users import UsersHandler
from handler.Message import MessageHandler
from handler.hashtags import HashtagHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@app.route('/SikitrakeChat')
def home():
    return ('Welcome to SikitrakeChat!')


"""@app.route('/login')
def login():
    return "Login Not Currently Available" """

@app.route('/SikitrakeChat/Reactions')
def reactions():
    handler = ReactionHandler()
    return handler.getAllReactions()

@app.route('/SikitrakeChat/Reactions/ID/<int:rid>')
def getReactionsById(rid):
    return ReactionHandler().getReactionsById(rid)

@app.route('/SikitrakeChat/Reactions/Likes')
def getAllLikes():
    return ReactionHandler().getAllLikes()

@app.route('/SikitrakeChat/GroupChats/User/name/<string:name>')
def getGroupChatsByUsername(name):
    handler = GroupChatHandler()
    return handler.getGroupChatsByUsername(name)

@app.route('/SikitrakeChat/Reactions/Dislikes')
def getAllDislikes():
    return ReactionHandler().getAllDislikes()

@app.route('/SikitrakeChat/GroupChats')
def getAllGroupChats():
    return GroupChatHandler().getAllGroupChats()

@app.route('/SikitrakeChat/GroupChats/name/<string:name>')
def getGroupChatsByName(name):
    return GroupChatHandler().getGroupChatsByName(name)

""""@app.route('/SikitrakeChat/GroupChats/owner/<int:uid>')
def getGroupChatByOwner(uid):
    return GroupChatHandler().getGroupChatByOwner(uid)"""

@app.route('/SikitrakeChat/GroupChats/ID/<int:gid>')
def getGroupChatsById(gid):
    return GroupChatHandler().getGroupChatsById(gid)

@app.route('/SikitrakeChat/GroupChats/ID/<int:gid>/name')
def getGroupChatNameById(gid):
    return GroupChatHandler().getGroupChatNameById(gid)

@app.route('/SikitrakeChat/GroupChats/name/<string:name>/info')
def getGroupChatInfoByName(name):
    return GroupChatHandler().getGroupChatInfoByName(name)

@app.route('/SikitrakeChat/Users')
def getAllUsers():
    return UsersHandler().getAllUsers()

@app.route('/SikitrakeChat/Users/ID/<int:UID>')
def getUsersByUId(UID):
    handler = UsersHandler()
    return handler.getUsersByUId(UID)

@app.route('/SikitrakeChat/Users/phone/<string:phone>')
def getUsersByPhone(phone):
    handler = UsersHandler()
    return handler.getUsersByPhone(phone)

@app.route('/SikitrakeChat/Users/email/<string:email>')
def getUsersByEmail(email):
    handler = UsersHandler()
    return handler.getUsersByEmail(email)

@app.route('/SikitrakeChat/Users/contacts/<int:UID>')
def getContactsByUserID(UID):
    handler = UsersHandler()
    return handler.getContactsByUserID(UID)

@app.route('/SikitrakeChat/Messages')
def getAllMessages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/SikitrakeChat/Messages/ID/<int:mid>/Reactions')
def getAllReactionsByMessageID(mid):
    handler = ReactionHandler()
    return handler.getAllReactionsbyMessageID(mid)

@app.route('/SikitrakeChat/Messages/ID/<int:mid>/Likes')
def getAllLikesByMessageID(mid):
    handler = ReactionHandler()
    return handler.getAllLikesByMessageID(mid)

@app.route('/SikitrakeChat/Messages/ID/<int:mid>/Dislikes')
def getAllDislikesByMessageID(mid):
    handler = ReactionHandler()
    return handler.getAllDislikesByMessageID(mid)

@app.route('/SikitrakeChat/Messages/ID/<int:mid>/Likes/Amount')
def getNumberOfLikesByMessageID(mid):
    handler = ReactionHandler()
    return handler.getNumberOfLikesByMessageID(mid)

@app.route('/SikitrakeChat/Messages/ID/<int:mid>/Dislikes/Amount')
def getNumberOfDislikesByMessageID(mid):
    handler = ReactionHandler()
    return handler.getNumberOfDislikesByMessageID(mid)

@app.route('/SikitrakeChat/Messages/ID/<int:mid>')
def getMessageById(mid):
    return MessageHandler().getMessageById(mid)

@app.route('/SikitrakeChat/Messages/GroupChats/ID/<int:cid>')
def getMessagesbyChatID(cid):
    handler = MessageHandler()
    return handler.getMessagesbyChatID(cid)

@app.route('/SikitrakeChat/Messages/GroupChats/ID/<int:cid>/User/ID/<int:uid>')
def getMessagesbyChatIDAndUser(cid, uid):
    handler = MessageHandler()
    return handler.getMessagesbyChatIDAndUser(cid, uid)

@app.route('/SikitrakeChat/Hashtags')
def getAllHashtags():
    handler = HashtagHandler()
    return handler.getAllHashtags()

@app.route('/SikitrakeChat/Hashtags/ID/<int:htid>')
def getHashtagsById(htid):
    handler = HashtagHandler()
    return handler.getHashtagsById(htid)

@app.route('/SikitrakeChat/Messages/ID/<int:mid>/Hashtags')
def getHashtagsByMessageId(mid):
    handler = HashtagHandler()
    return handler.getHashtagsByMessageId(mid)

@app.route('/SikitrakeChat/Users/GroupChats/ID/<int:gid>')
def getUsersInGroupChatByID(gid):
    handler = UsersHandler()
    return handler.getUsersInGroupChatByID(gid)

@app.route('/SikitrakeChat/Users/Username/<string:uname>')
def getUserByUsername(uname):
    handler = UsersHandler()
    return handler.getUserByUsername(uname)

@app.route('/SikitrakeChat/Users/GroupChats/name/<string:name>')
def getUsersInGroupChatByName(name):
    handler = UsersHandler()
    return handler.getUsersInGroupChatByName(name)

@app.route('/SikitrakeChat/Users/Liked/Messages/<int:mid>')
def getUsersThatLikedMessage(mid):
    handler = UsersHandler()
    return handler.getUsersThatLikedMessage(mid)

@app.route('/SikitrakeChat/Users/Disliked/Messages/<int:mid>')
def getUsersThatDislikedMessage(mid):
    handler = UsersHandler()
    return handler.getUsersThatDislikedMessage(mid)

@app.route('/SikitrakeChat/GroupChats/Name/<string:gname>/owner')
def getGroupChatOwnerByName(gname):
    handler = UsersHandler()
    return handler.getGroupChatOwnerByName(gname)

@app.route('/SikitrakeChat/GroupChats/ID/<int:gid>/owner')
def getGroupChatOwnerByID(gid):
    handler = UsersHandler()
    return handler.getGroupChatOwnerByID(gid)

@app.route('/SikitrakeChat/Messages/LikesAndDislikes')
def getMessagesWithLikesAndDislikes():
    handler = MessageHandler()
    return handler.getMessagesWithLikesAndDislikes()


############################
#Phase III Routes
############################

#The ability to login a user
@app.route('/SikitrakeChat/Login', methods = ['GET'])
def Login():
    if request.method == 'GET':
        print ('estoy en la ruta')
        handler = UsersHandler()
        return handler.login(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#The ability to logout a user (no esta en los requerimientos)
# Creo que no se necesita hacer logout como tal
# bastaria con enviar al usuario a la pg de login y ya
"""@app.route('/SikitrakeChat/Logout')
def Logout():
    handler = UsersHandler()
    return handler.logout(request.args)"""

#The ability to add a new user
@app.route('/SikitrakeChat/AddUser', methods = ['POST'])
def insertUser():
    if request.method == 'POST':
        handler = UsersHandler()
        return handler.insertUser(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#The ability to post a new message
@app.route('/SikitrakeChat/GroupChat/Message', methods = ['POST'])
def insertMessageinChatGroup():
    if request.method == 'POST':
        handler = MessageHandler()
        return handler.insertMessageinChatGroup(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405


#The ability to like a message
@app.route('/SikitrakeChat/GroupChat/Messages/Like', methods = ['POST'])
def manageLikeMessage():
    # tengo que hacer la rutina para vetificar si alguien no le dio
    # like o dislike, se alguien le dio like/dislike seria un update
    if request.method == 'POST':
        handler = ReactionHandler()
        return handler.insertLikeinMessage(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#The ability to dislike a message
@app.route('/SikitrakeChat/GroupChat/Messages/Dislike', methods = ['POST'])
def manageDislikeMessage():
    if request.method == 'POST':
        handler = ReactionHandler()
        return handler.insertDislikeinMessage(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#List of chat groups to which a user belongs
#The ability to join a chat group
@app.route('/SikitrakeChat/GroupChats', methods = ['GET', 'POST'])
def getAllChatGroupsByUser():
    if request.method == 'GET':
        handler = GroupChatHandler()
        return handler.getGroupChatByUserID(request.args)
    if request.method == 'POST' :
        handler = GroupChatHandler()
        return handler.insertNewChatGroup(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#List of messages in a given chat group
@app.route('/SikitrakeChat/Messages/GroupChats', methods = ['GET'])
def getAllMessagesByChatGroup():
    if request.method == 'GET':
        handler = MessageHandler()
        return handler.getMessagesWithLikesAndDislikesByChatGroup(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#List of messages with a given hashtag on a chat group
@app.route('/SikitrakeChat/GroupChat/Hashtag/Messages', methods = ['GET'])
def getAllMessagesByHashtag():
    if request.method == 'GET':
        handler = MessageHandler()
        return handler.getAllMessagesByHashtaginGC(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#The ability to post a reply to a message
@app.route('/SikitrakeChat/GroupChat/Messages/Reply', methods = ['POST'])
def insertReplyMessage():
    if request.method == 'POST':
        handler = MessageHandler()
        return handler.insertReplyMessage(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#The add a participant to a group chat
@app.route('/SikitrakeChat/GroupChat/Participants', methods = ['POST'])
def insertParticipant():
    if request.method == 'POST':
        handler = GroupChatHandler()
        return handler.insertParticipant(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Add User to your contact list based on first name, last name and either phone or number
@app.route('/SikitrakeChat/AddContact', methods = ['POST'])
def insertContact():
    if request.method == 'POST':
        handler = UsersHandler()
        return handler.insertContact(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405
#DASHBOARD
@app.route('/SikitrakeChat/Messages/countbymessagesperday')
def getCountByMessagesPerDay():
    return MessageHandler().getCountByMessagesPerDay()

@app.route('/SikitrakeChat/Messages/countlikesperday')
def getCountLikesPerDay():
    return MessageHandler().getCountLikesPerDay()

@app.route('/SikitrakeChat/Messages/countdislikesperday')
def getCountDisLikesPerDay():
    return MessageHandler().getCountDisLikesPerDay()

@app.route('/SikitrakeChat/Messages/countrepliesperday')
def getCountRepliesPerDay():
    return MessageHandler().getCountRepliesPerDay()

@app.route('/SikitrakeChat/Messages/countuserpostperday')
def getCountUserPostPerDay():
    return MessageHandler().getCountUserPostPerDay()
@app.route('/SikitrakeChat/Messages/counthashtagsperday')
def getCountHashtagsPerDay():
    return MessageHandler().getCountHashtagsPerDay()
if __name__=='__main__':
    app.run()
