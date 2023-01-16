import { transport } from "./transport.js"
import { speak_confiramtion, speak_error } from "./speak.js"


export class handel_login extends transport {


    constructor(){
        
        super()
        this.initiate_transport()
        this.LOGIN_PATH = '/auth/registered_user/login/'
        
    }


    inititate_handel_login(){
        
        this.handlers()

    }


    handlers(){

        $("#web_login").on("click", ()=>this.send_login_form());
        

    }


    redirect_to_desired_location_on_login(){

        

        speak_confiramtion('Successfully logged in, redirecting...', ()=>console.log("good"));//window.location = window.location.href);
        
        
    }


    speak_auth_error(){

        speak_error('Please check your username & password');
    }


    speak_validation_error(){

        

        speak_error('Please provide Username & password')

    }


    send_login_form(){


        let data = {

            "username": "",
            "email": $("input[name='user_email']").val(),
            "password": $("input[name='user_password']").val()
        }

        

        if (data.email != '' && data.password != ''){

            this.send_post(this.LOGIN_PATH, data, ()=>{

                this.send_post('/auth/login', console.log, console.log);
                
            }, this.speak_auth_error);

        } else {

            this.speak_validation_error();
        }

        

    }

}



