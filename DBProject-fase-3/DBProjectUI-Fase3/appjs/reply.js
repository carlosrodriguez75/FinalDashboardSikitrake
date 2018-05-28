angular.module('AppChat').controller('ReplyController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        this.Message = "	Enter Reply";
	this.Or_msg_ID;
	this.groupid;
	this.userid;
	this.disp;

        this.postReply = function(){
            var reqURL = "http://localhost:5000/SikitrakeChat/GroupChat/Messages/Reply?Or_msg_ID=" + thisCtrl.Or_msg_ID + "&Message=" + thisCtrl.Message + "&UID=" + thisCtrl.userid + "&GID=" + thisCtrl.groupid;
            console.log("reqURL: " + reqURL);
	    var empty = {};
            $http.post(reqURL,empty).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.returnToChat();
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

	this.returnToChat = function(){
		$location.url('/chat/'+ thisCtrl.disp + '/' + thisCtrl.groupid);
	}

	this.loadVar = function(){
		thisCtrl.Or_msg_ID = $routeParams.mid;
		thisCtrl.groupid = $routeParams.gid;
		thisCtrl.userid = $routeParams.uid;
		thisCtrl.disp = $routeParams.disp;
		
	}

        this.loadVar();
}]);
