angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$location',
    function($http, $log, $scope, $location) {
        var thisCtrl = this;
        this.UDispName = "	Enter Username";
        this.UPassword = "	Enter Password";

	this.signin = function(){
            //Implement login check! Ask Coralis for pointers
            var reqURL = "http://localhost:5000/SikitrakeChat/Login?UDispName="+ thisCtrl.UDispName+"&UPassword=" + thisCtrl.UPassword + "";
            console.log("reqURL: " + reqURL);

            $http.get(reqURL).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    if(response.data.Login == 1){
			console.log("Login successful. Moving to main page");
                        $location.url('/mainpage/' + thisCtrl.UDispName);
                    }
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
                        alert("Login failed!");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        }

        this.signup = function(){
            console.log("Moving to signup page.");
            $location.url('/signup');
        }

}]);
