angular.module('AppChat').controller('MainPageController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.grouplist = [];
	this.dispname;
        
        this.loadMainPage = function(){
            thisCtrl.dispname = $routeParams.UDispName;
	
            var reqURL = "http://localhost:5000/SikitrakeChat/GroupChats/User/name/" + thisCtrl.dispname;
            console.log("reqURL: " + reqURL);

            $http.get(reqURL).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.grouplist = response.data.GroupChats;
		    $log.error("GroupChats Loaded: ", JSON.stringify(thisCtrl.grouplist));
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
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

	this.goToAddChatPage = function(){
		$location.url('/addChat/'+thisCtrl.dispname);
	}
	
	this.goToAddContactPage = function(){
		$location.url('/addContact/'+thisCtrl.dispname);
	}

	this.chatpage = function (gid){
	        console.log("Going to message page for group: " + gid);
            $location.url('/chat/' + thisCtrl.dispname + '/' + gid);
        }

	this.loadMainPage();
}]);
