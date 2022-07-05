function register(){
    var email=document.getElementById("email").value;
    var pass=document.getElementById("pass").value;
    var repass=document.getElementById("repass").value;
    var pwd_expression = /^[0-9]+$/;
    var letters = /^[A-Za-z]+$/;
    var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if(email==""){
        alert('Please enter Your user mail');
    }
    else if(!filter.test(email)){
        alert('Invalid Email');
    }
    else if(pass=='')
     {
            alert('Please enter Password');
    }
    else if(repass=='')
    {
            alert('Enter Confirm Password');
    }
    else if(!pwd_expression.test(pass)){
        alert ('Password must have numeric characters only');
    }
    else if(pass!=repass){
        alert ('Password not Matched');
    }
    else if(pass.value.length < 6)
    {
        alert ('Password minimum length is 6');
    }
    else if(pass.value.length > 12)
    {
        alert ('Password max length is 12');
    }
    else
        {                                           
               alert('Thank You for Registration');
        }

}