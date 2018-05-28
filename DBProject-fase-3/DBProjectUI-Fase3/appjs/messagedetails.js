angular.module('AppChat').controller('MessageDetailsController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        var messageDetails = [];
        this.loadMessageDetails = function(){
            var mid = $routeParams.id;
            var reqURL = "http://localhost:5000/SikitrakeChat/Messages/ID/" + mid + "/Reactions";
            console.log("reqURL: " + reqURL);

            $http.get(reqURL).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.messageDetails = response.data.Reactions;
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

	this.returnToChat = function(gid){
		$location.url('/chat/'+chatCtrl.groupid);
	}

        this.loadMessageDetails();
}]);
