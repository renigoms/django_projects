function gritar(){
    alert("Ahhhhhhhhhhhhhhhhhhhhhhhhhhh!")
}

function perguntar(){
    var nome = prompt("Qual é o seu nome? ");
    if (nome.trim() == ""){
        return   
    }
    alert("Olá "+nome);
    
}

function mudar_texto(){
    var text1 = "Geek Univesity";
    var text2 = "Evolua seu lado geek";
    var h1 = document.getElementsByTagName("h1");

    // alert(h1[0].innerText);

    if (h1[0].innerText == text1){
        h1[0].innerText = text2;
        return;
    }
    h1[0].innerText = text1;
}

function incrementar() {
    var p1 = document.getElementById("p1")
    p1.innerText = parseInt(p1.innerText) + 1
}