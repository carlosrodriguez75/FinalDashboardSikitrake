(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).when('/chat/:UDispName/:gid', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/messageDetails/:id', {
            templateUrl: 'pages/messagedetails.html',
            controller: 'MessageDetailsController',
            controllerAs: 'msgdetailsCtrl'
        }).when('/signup', {
            templateUrl: 'pages/signup.html',
            controller: 'SignupController',
            controllerAs: 'signupCtrl'
        }).when('/reply/:disp/:uid/:gid/:mid', {
            templateUrl: 'pages/reply.html',
            controller: 'ReplyController',
            controllerAs: 'repCtrl'
        }).when('/registersuccess', {
            templateUrl: 'pages/registersuccess.html',
            controller: 'SignupController',
            controllerAs: 'signupCtrl'
        }).when('/mainpage/:UDispName', {
            templateUrl: 'pages/mainpage.html',
            controller: 'MainPageController',
            controllerAs: 'mainCtrl'
        }).when('/addChat/:UDispName', {
            templateUrl: 'pages/addChat.html',
            controller: 'AddChatController',
            controllerAs: 'addCtrl'
        }).when('/addParticipant/:disp/:uid/:gid', {
            templateUrl: 'pages/addParticipant.html',
            controller: 'AddParticipantController',
            controllerAs: 'addPCtrl'
        }).when('/addContact/:disp', {
            templateUrl: 'pages/addContact.html',
            controller: 'AddContactController',
            controllerAs: 'addCCtrl'
        }).otherwise({
            redirectTo: '/login'
        });
    }]);
    console.log("Main");
})();
