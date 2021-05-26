

// ----------------------------------------
// GESTION DU MENU DEROULANT EN PETIT ECRAN 
// ----------------------------------------

const bouton_menu_deroulant = document.getElementById("bouton_menu_deroulant");
const barre_bouton = document.getElementsByClassName("barre_bouton");
const croix_carree = document.getElementById("croix_carree");
const navbar = document.getElementById("navbar");

let menu_deroule = false;

bouton_menu_deroulant.addEventListener('mouseenter', allumerBouton);
bouton_menu_deroulant.addEventListener('mouseleave', eteindreBouton);
bouton_menu_deroulant.addEventListener('click', cliquerMenu);

window.addEventListener('resize', barreNavResponsive);


// ------------------
// FONCTIONS CALLBACK
// ------------------

// gestion de la barre de navigation si la largeur de la fenêtre change
function barreNavResponsive(event){
    if (window.innerWidth > 1080){
        navbar.style.display = "block";
        menu_deroule = false;
    } else {
        if (menu_deroule == true) {
            navbar.style.display = "block";
        } else {
            navbar.style.display = "none";
            afficherHamburger();
        };
    };
}

// allumage du bouton Hamburger (gris --> orange)
function allumerBouton(event){
    // bouton menu déroulant (3 barres) devient orange
    for (let elt of barre_bouton){
        elt.style.backgroundColor = "#FE5A02";
        };
    }

// éteinte du bouton Hamburger (orange --> gris)
function eteindreBouton(event){
    // bouton menu déroulant (3 barres) redevient gris sauf si on a cliqué
    if (menu_deroule == false){
        for (let elt of barre_bouton){
            elt.style.backgroundColor = "#2C3E50";
            };
        };
    }

// affichage / masquage du menu déroulant si clic sur hamburger ou croix
function cliquerMenu(event){
    event.preventDefault();

    // cas où on clique pour dérouler le menu
    if (menu_deroule == false){
        menu_deroule = true;
        // derouler le menu 
        navbar.style.display = "block";
        // remplacer le hamburger par une croix
        afficherCroixCarree();
    
    // cas où on clique pour masquer le menu
    } else {
        menu_deroule = false;
        // masquer le menu
        navbar.style.display = "none";
        // remplacer la croix par un hmaburger
        afficherHamburger();
        }
    }

function afficherHamburger(){ 
    // efface la croix carree et affiche le hamburger
        croix_carree.style.display = "none";
        for (let elt of barre_bouton){
            elt.style.display = "block";
            elt.style.backgroundColor = "#2C3E50";
            };
        }


function afficherCroixCarree(){
        for (let elt of barre_bouton){
            elt.style.display = "none";
            };
        croix_carree.style.display = "block";
    }


