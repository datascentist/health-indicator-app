document.addEventListener("DOMContentLoaded", clickMe());

function clickMe(){
    button = document.getElementById('send');
    button.addEventListener('click', ()=>{
        window.location.href = "sendMessage"
    });
    alert(document.getElementById('message').innerHTML);
}