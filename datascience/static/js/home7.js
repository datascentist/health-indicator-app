document.addEventListener("DOMContentLoaded", clickMe());

function clickMe(){
    alert(document.getElementById('message').innerHTML);
    console.log(document.getElementById('message').innerHTML)
}