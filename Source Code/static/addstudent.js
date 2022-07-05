function confirmAdd()
{
    confirm('Are you sure you want to add this student ?')
}
function addstudent() 
{ 
    var name=document.getElementById('name').value; 
    var id=document.getElementById('id').value; 
    var level=document.getElementById('level').value; 
    var email=document.getElementById('email').value; 
    var gpa=document.getElementById('gpa').value; 
    var phone_no=document.getElementById('phone').value; 
    var pwd_expression = /^[0-9]+$/; 
    var letters = /^[A-Za-z]+$/; 
    var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/; 
    if(name==''){ 
        alert('Please enter name'); 
    } 
    else if(id==''){ 
        alert('Please enter  id '); 
    } 
     else if(level==''){ 
        alert('Please enter  level'); 
    } 
     else if(level.value.length >4  ) 
    { 
        alert ('level maxmum length is 4 '); 
    } 
     else if(level.value.length < 1) 
    { 
        alert ('level minmum length is 1'); 
    } 
    else if(email==''){ 
        alert('Please enter  mail '); 
    } 
    else if(!filter.test(email)){ 
        alert('Invalid Email'); 
    } 
    else if(gpa==''){ 
        alert('Please enter  gba '); 
    } 
    else if(gpa.value.length < 0) 
    { 
        alert ('level minmum length is 0'); 
    } 
   else if(gba.value.length > 4) 
    { 
        alert ('level maxmum length is 4'); 
    }
    else if(phone_no==''){
        alert('Please enter  phone number '); 
    } 
    
}