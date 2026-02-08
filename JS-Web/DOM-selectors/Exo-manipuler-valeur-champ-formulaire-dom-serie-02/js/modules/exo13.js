export const execExo13 = () => {
    console.log("----- Exo 13 -----");

    const champElem = document.querySelector("#exo13-quantite");
    const sortieElem = document.querySelector("#exo13-sortie");

    if (!champElem) {
        console.log("Exo13: champ #exo13-quantite introuvable.");
        return;
    }

    if (!sortieElem) {
        console.log("Exo13: élément #exo13-sortie introuvable.");
        return;
    }

    console.log("Observation : Number('') donne →", Number(""));

    // Écoute de la saisie
    champElem.addEventListener("input", () => {
        const valeurTexte = champElem.value;

        if (valeurTexte.trim() === "") {
            sortieElem.textContent = "Quantité affichée : (aucune valeur)";
            return;
        }

        const valeurNombre = Number(valeurTexte);

        if (Number.isNaN(valeurNombre)) {
            sortieElem.textContent = "Quantité affichée : (valeur invalide)";
            return;
        }

        sortieElem.textContent = "Quantité affichée : " + valeurNombre;
    });
};
