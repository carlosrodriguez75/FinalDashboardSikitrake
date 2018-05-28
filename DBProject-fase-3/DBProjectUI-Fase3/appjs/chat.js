angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter  = 0;
        this.newText = "";
        this.likesNdislikes = [];
	this.groupid;
	this.dispname;
	this.userid;

        this.loadMessages = function(){
		thisCtrl.messageList = [];
		console.log("Acquired gid: " + $routeParams.gid);
		console.log("Acquired username: " + $routeParams.UDispName);
	    thisCtrl.groupid = $routeParams.gid;
	    thisCtrl.dispname = $routeParams.UDispName;
            var url = "http://localhost:5000/SikitrakeChat/Messages/GroupChats?GID="+ thisCtrl.groupid;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;
                    $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
                    var i;
                    for(i = 0; i < thisCtrl.messageList.length; i++){
                        thisCtrl.likesNdislikes[i]=00;
                    }
		    console.log("LikesNDislikes: " + thisCtrl.likesNdislikes);

            }, // error callback
            function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            var author = thisCtrl.dispname;
	    var UserInfo;
	    var UserID = 0;
	    thisCtrl.likesNdislikes.push(00);
	    var newmsg = msg.replace(/#/g, "~");
		$log.error("New message: " + newmsg);
	    console.log("Using dispname: " + thisCtrl.dispname);
  	    var url = "http://localhost:5000/SikitrakeChat/Users/Username/"+ author;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    UserInfo = response.data.Users;
                    $log.error("User Loaded: ", UserInfo);
		    $log.error("User ID: ", UserInfo[0].UID);
		    UserID = UserInfo[0].UID;
		    thisCtrl.postToDB(UserID, thisCtrl.groupid, newmsg);

            }, // error callback
            function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }		
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

            $log.error("Message Loaded: ", JSON.stringify(UserInfo));		
        };

	this.postToDB = function(uid,gid,msg){
	   
	    if(uid > 0){
			//post new message using UID, GID and Message
			var reqURL = "http://localhost:5000/SikitrakeChat/GroupChat/Message?UID="+uid+"&GID="+gid+"&Message="+ msg;
		    console.log("reqURL: " + reqURL);
			var empty = {};
			$http.post(reqURL,empty).then(
		        function(response){
		            console.log("data: " + JSON.stringify(response.data));
		        },
		        function(response){
		            var status = response.status;

		            if (status == 0) {
		                alert("No hay conexion a Internet");
		            }
		            else if (status == 401) {
		                alert("Su sesion expiro. Conectese de nuevo.");
		            }
		            else if (status == 403) {
		                alert("No esta autorizado a usar el sistema.");
		            }
		            else if (status == 404) {
		                alert("Error! User already exists or information is not valid.");
		            }
		            else {
		                alert("Error interno del sistema.");
		            }
		        }
		    );

	    }

	}

	this.searchByHashtag = function(){
		//post new message using UID, GID and Message
		var msg = thisCtrl.newText;
		var newmsg = msg.replace(/#/g, "~");
		var reqURL = "http://localhost:5000/SikitrakeChat/GroupChat/Hashtag/Messages?Htext="+newmsg+"&GID="+thisCtrl.groupid;
	    console.log("reqURL: " + reqURL);
		$http.get(reqURL).then(
	        function(response){
	            console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;
                    $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
	        },
	        function(response){
	            var status = response.status;

	            if (status == 0) {
	                alert("No hay conexion a Internet");
	            }
	            else if (status == 401) {
	                alert("Su sesion expiro. Conectese de nuevo.");
	            }
	            else if (status == 403) {
	                alert("No esta autorizado a usar el sistema.");
	            }
	            else if (status == 404) {
	                alert("Error! User already exists or information is not valid.");
	            }
	            else {
	                alert("Error interno del sistema.");
	            }
	        }
	    );

	}

	this.loadUID = function(){
	    var author = thisCtrl.dispname;
	    var UserInfo;
	    var UserID = 0;
	    console.log("Using dispname: " + thisCtrl.dispname);
  	    var url = "http://localhost:5000/SikitrakeChat/Users/Username/"+ author;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    UserInfo = response.data.Users;
                    $log.error("The User Loaded: ", UserInfo);
		    $log.error("User ID: ", UserInfo[0].UID);
		    UserID = UserInfo[0].UID;
		    thisCtrl.userid = UserID;
		    console.log("Registered ID: " + thisCtrl.userid);

            }, // error callback
            function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }		
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });
	}
          
        this.messageDetails = function (id){
	        console.log("Checking message details for message: " + id);
            $location.url('/messageDetails/' + id);
        }

	this.replyToMessage = function(mid){
	    $location.url('/reply/' + thisCtrl.dispname + '/' + thisCtrl.userid + '/' + thisCtrl.groupid + '/' + mid);
	}

	this.goToAddParticipant = function(){
	    $location.url('/addParticipant/'+thisCtrl.dispname+'/'+thisCtrl.userid+'/'+thisCtrl.groupid);
	}

        this.changeLikes = function (id){
	console.log("Changing likes for mid: " + id);
			//post new message using UID, GID and Message
		var reqURL = "http://localhost:5000/SikitrakeChat/GroupChat/Messages/Like?UID="+thisCtrl.userid+"&MID="+id;
	    console.log("reqURL: " + reqURL);
		var empty = {};
		$http.post(reqURL,empty).then(
	        function(response){
	            console.log("data: " + JSON.stringify(response.data));
		    thisCtrl.crossCheckLikes(id);
		    thisCtrl.crossCheckDislikes(id);
	        },
	        function(response){
	            var status = response.status;

	            if (status == 0) {
	                alert("No hay conexion a Internet");
	            }
	            else if (status == 401) {
	                alert("Su sesion expiro. Conectese de nuevo.");
	            }
	            else if (status == 403) {
	                alert("No esta autorizado a usar el sistema.");
	            }
	            else if (status == 404) {
	                alert("Error! User already exists or information is not valid.");
	            }
	            else {
	                alert("Error interno del sistema.");
	            }
	        }
	    );

        }

	this.crossCheckLikes = function(id){
        var i;
	var j;
        var curr_dict;
            for(i=0; i < thisCtrl.messageList.length; i++){
                curr_dict = thisCtrl.messageList[i];
                if(curr_dict["id"] == id){
			j = i;
			console.log("Current message: " + curr_dict["id"] + " Selected id: " + id);
		            
			var url = "http://localhost:5000/SikitrakeChat/Messages/ID/"+id+"/Likes/Amount";
		    $http.get(url).then(
		        function (response){
			    console.log("response: " + JSON.stringify(response));
		            thisCtrl.messageList[j]["like"] = response.data.Reactions[0].Total;

		    }, // error callback
		    function (response){
		        // This is the error function
		        // If we get here, some error occurred.
		        // Verify which was the cause and show an alert.
		        var status = response.status;
		        if (status == 0){
		            alert("No hay conexion a Internet");
		        }
		        else if (status == 401){
		            alert("Su sesion expiro. Conectese de nuevo.");
		        }		
		        else if (status == 403){
		            alert("No esta autorizado a usar el sistema.");
		        }
		        else if (status == 404){
		            alert("No se encontro la informacion solicitada.");
		        }
		        else {
		            alert("Error interno del sistema.");
		        }
		    });
                }
            }
	}

	this.crossCheckDislikes = function(id){
        var i;
	var j;
        var curr_dict;
            for(i=0; i < thisCtrl.messageList.length; i++){
                curr_dict = thisCtrl.messageList[i];
                if(curr_dict["id"] == id){
			j = i;
			console.log("Current message: " + curr_dict["id"] + " Selected id: " + id);
			var url = "http://localhost:5000/SikitrakeChat/Messages/ID/"+id+"/Dislikes/Amount";
		    $http.get(url).then(
		        function (response){
			    console.log("response: " + JSON.stringify(response));
		            thisCtrl.messageList[j]["nolike"] = response.data.Reactions[0].Total;

		    }, // error callback
		    function (response){
		        // This is the error function
		        // If we get here, some error occurred.
		        // Verify which was the cause and show an alert.
		        var status = response.status;
		        if (status == 0){
		            alert("No hay conexion a Internet");
		        }
		        else if (status == 401){
		            alert("Su sesion expiro. Conectese de nuevo.");
		        }		
		        else if (status == 403){
		            alert("No esta autorizado a usar el sistema.");
		        }
		        else if (status == 404){
		            alert("No se encontro la informacion solicitada.");
		        }
		        else {
		            alert("Error interno del sistema.");
		        }
		    });
                }
            }
	}

	this.changeDislikes = function(id){
	console.log("Changing likes for mid: " + id);
			//post new message using UID, GID and Message
		var reqURL = "http://localhost:5000/SikitrakeChat/GroupChat/Messages/Dislike?UID="+thisCtrl.userid+"&MID="+id;
	    console.log("reqURL: " + reqURL);
		var empty = {};
		$http.post(reqURL,empty).then(
	        function(response){
	            console.log("data: " + JSON.stringify(response.data));
		    thisCtrl.crossCheckDislikes(id);
		    thisCtrl.crossCheckLikes(id);
	        },
	        function(response){
	            var status = response.status;

	            if (status == 0) {
	                alert("No hay conexion a Internet");
	            }
	            else if (status == 401) {
	                alert("Su sesion expiro. Conectese de nuevo.");
	            }
	            else if (status == 403) {
	                alert("No esta autorizado a usar el sistema.");
	            }
	            else if (status == 404) {
	                alert("Error! User already exists or information is not valid.");
	            }
	            else {
	                alert("Error interno del sistema.");
	            }
	        }
	    );

        }

        this.loadMessages();
	this.loadUID();
        console.log("Loading Complete");
}]);
