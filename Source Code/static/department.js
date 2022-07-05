function confirmDep() {
    var txt;
    if (confirm("Are you sure you want to add this department?")) {
      txt = "You confirmed!";
    } else {
      txt = "You Canceled!";
    }
    document.getElementById("demo").innerHTML = txt;
  }