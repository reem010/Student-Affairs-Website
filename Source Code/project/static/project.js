function myFunction() {

  var input, filter, table, tr, tdname, i, txtValueforname;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    tdname = tr[i].getElementsByTagName("td")[0];
    if (tdname ) {
      txtValueforname = tdname.textContent || tdname.innerText;
      if (txtValueforname.toUpperCase().indexOf(filter) > -1&& myFunctions(i)) {
          tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
function myFunctions(i){
  var table, tr, td,val,i;
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
    td=tr[i].getElementsByTagName("td")[3];
    if (td) {
      val=td.innerText || td.textContent;
    if (val=="active") {
    return true;
    }
    else {
    return false;
    }
 }
}
function submitForm(name) {
  if(document.getElementsByClassName("level")[name].innerText=="3"){
      open("depart.html");
  }else{
    alert("Sorry, you have to be level 3 to change your department!")
  }
}

