export const execExo14 = () => {
    console.log("----- Exo 14 -----");

    const champElem = document.querySelector("#exo14-quantite");
    const sortieElem = document.querySelector("#exo14-sortie");

    if (!champElem) {
        console.log("Exo14: champ #exo14-quantite introuvable.");
        return;
    }

    if (!sortieElem) {
        console.log("Exo14: élément #exo14-sortie introuvable.");
        return;
    }

    champElem.addEventListener("input", () => {
        const valeurNombre = champElem.valueAsNumber;

        if (Number.isNaN(valeurNombre)) {
            sortieElem.textContent = "Quantité affichée : (aucune valeur)";
            return;
        }

        sortieElem.textContent = "Quantité affichée : " + valeurNombre;
    });
};
