// This code is embeedded in login htm file.
console.log("testing");
  document.querySelector('#tt').onkeyup = function(){
     if (document.querySelector('#tt').value === '') {
       document.querySelector('#add').disabled = true;}
     else{
      document.querySelector('#add').disabled = false;}
   }
  var test = document.querySelector('#chk');
  chk.addEventListener('change', fnc);

  function fnc() {
    var x = document.querySelector("#pw");
  if (x.type === "password") {
   x.type = "text";}
  else {
   x.type = "password";}
  }
  console.log("end");
