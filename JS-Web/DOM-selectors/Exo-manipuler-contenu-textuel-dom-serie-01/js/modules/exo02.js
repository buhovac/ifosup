export const execExo02 = () =>
{
    console.log("----- Exo 02 -----");

    const texteElem = document.querySelector("#exo02-texte");
    const sortieElem = document.querySelector("#exo02-sortie");
    const boutonToggleElem = document.querySelector("#exo02-btn-toggle");

    if (!texteElem || !sortieElem || !boutonToggleElem) {
        console.log("Exo 02: élément manquant (#exo02-texte, #exo02-sortie ou #exo02-btn-toggle).");
        return;
    }

    const texteVide = "(vide)";
    let sortieEstVisible = false;

    sortieElem.textContent = texteVide;
    boutonToggleElem.textContent = "Générer le résumé visible";

    boutonToggleElem.addEventListener("click", () =>
    {
        sortieEstVisible = !sortieEstVisible;

        if (sortieEstVisible) {

            sortieElem.textContent = texteElem.innerText;
            boutonToggleElem.textContent = "Effacer le résumé";
        } else {
            sortieElem.textContent = texteVide;
            boutonToggleElem.textContent = "Générer le résumé visible";
        }
    });
};
