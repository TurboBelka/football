var user = {}

function doLogin(){
    FB.login(function(response){
        if(response.status === 'connected'){
            // Logged into your app and Facebook.
            getDataAboutUser(response);
        }else if(response.status === 'not_authorized'){
            //The person is logged into Facebook, but not your app.
            getDataAboutUser(response);
        }else {
            // The person is not logged into Facebook, so we're not sure if
            // they are logged into this app or not.
        }
    }, {scope: 'public_profile, email'});
}


window.fbAsyncInit = function() {
    FB.init({
    appId      : '1648420282108034',
    cookie     : true,  // enable cookies to allow the server to access
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.5' // use version 2.5
});}

function getDataAboutUser(response){
    FB.api('/me', function(response){

        user = JSON.stringify(response);
    });
    console.log(user);

}

