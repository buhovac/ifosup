export function execExo01()
{
    console.log("----- Exo 01 -----");

    const statutElem = document.querySelector("#exo01-statut");
    const boutonToggleElem = document.querySelector("#exo01-btn-toggle");

    // Vérifier les sélections
    if (!statutElem || !boutonToggleElem) {
        console.log("Exo 01: élément manquant (#exo01-statut ou #exo01-btn-toggle).");
        return;
    }

    // Stocker le texte d'origine
    const texteOrigine = statutElem.textContent;

    // Texte publié (valeur exacte demandée)
    const texteMaj = "Statut : Publié";

    // État
    let estPublie = false;

    // Écouteur click
    boutonToggleElem.addEventListener("click", () => {
        estPublie = !estPublie;

        if (estPublie) {
            statutElem.textContent = texteMaj;
            boutonToggleElem.textContent = "Revenir en brouillon";
        } else {
            statutElem.textContent = texteOrigine;
            boutonToggleElem.textContent = "Publier";
        }
    });
}
