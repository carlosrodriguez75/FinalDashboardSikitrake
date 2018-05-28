angular.module('AppChat').controller('AddParticipantController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.groupid;
	this.userid;
	this.disp;
	this.contactList = [];


	this.loadContacts = function(){
		var url = "http://localhost:5000/SikitrakeChat/Users/contacts/"+thisCtrl.userid;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.contactList = response.data.Users;
                    $log.error("Contacts Loaded: ", JSON.stringify(thisCtrl.contactList));

            }, // error callback
            function (response){
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

        this.addParticipant = function(id){
            var empty = {};
            var url = "http://localhost:5000/SikitrakeChat/GroupChat/Participants?GID="+thisCtrl.groupid+"&UID="+thisCtrl.userid+"&CUID="+id;
            console.log("reqURL: " + url);

            $http.post(url,empty).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.returnToChatPage();
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
		});
        }

        this.returnToChatPage = function(){
            console.log("Moving to chat page.");
            $location.url('/chat/'+thisCtrl.disp+'/'+thisCtrl.groupid);
        }


	this.loadVar = function(){
		thisCtrl.groupid = $routeParams.gid;
		thisCtrl.userid = $routeParams.uid;
		thisCtrl.disp = $routeParams.disp;
		
	}

	this.loadVar();
	this.loadContacts();
}]);
