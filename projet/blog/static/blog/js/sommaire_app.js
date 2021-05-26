

// --------------------------------------------------------
// GESTION DU SOMMAIRE : ACCES AUX PARAGRAPHES D UN ARTICLE 
// --------------------------------------------------------

const slideUp = document.getElementById("slideup");


window.addEventListener('scroll', boutonScrollTop);



function boutonScrollTop() {
    if (window.scrollY > 800){
        slideUp.style.display = "block";
    } else {
        slideUp.style.display = "none";
    };
}

        
