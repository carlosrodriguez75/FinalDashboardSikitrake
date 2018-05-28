angular.module('AppChat').controller('SignupController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        this.UDispName = "sample";
        this.UPassword = "samplepw";
        this.UFirst_name = "John";
        this.ULast_name = "Tester";
        this.UEmail = "sampleemail@gmail.com";
        this.UPhone = "7874561234";
        this.received = [];

        this.register = function(){
            //Implement login check!
            var signupinfo = {};
            signupinfo["UDispName"] = thisCtrl.UDispName;
            signupinfo["UPassword"] = thisCtrl.UPassword;
            signupinfo["UFirst_name"] = thisCtrl.UFirst_name;
            signupinfo["ULast_name"] = thisCtrl.ULast_name;
            signupinfo["UEmail"] = thisCtrl.UEmail;
            signupinfo["UPhone"] = thisCtrl.UPhone;
            var reqURL = "http://localhost:5000/SikitrakeChat/AddUser?UDispName="+thisCtrl.UDispName+"&UPassword="+thisCtrl.UPassword+"&UFirst_name="+thisCtrl.UFirst_name+"&ULast_name="+thisCtrl.ULast_name+"&UEmail="+thisCtrl.UEmail+"&UPhone="+thisCtrl.UPhone+"";
            console.log("reqURL: " + reqURL);

            $http.post(reqURL,signupinfo).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    if(response.data.User.UDispName = thisCtrl.UDispName){
                        thisCtrl.registersuccess();
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
                        alert("Error! User already exists or information is not valid.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        }

        this.registersuccess = function(){
            console.log("Moving to buffer page.");
            $location.url('/registersuccess');
        }

        this.loginpage = function(){
            console.log("Moving to login page.");
            $location.url('/login');
        }
        //this.loadMessageDetails();
}]);
