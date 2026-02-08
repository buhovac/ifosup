export const execExo12 = () => {
    console.log("----- Exo 12 -----");

    const radiosElements = document.querySelectorAll('input[name="exo12-niveau"]');

    const sortieElem = document.querySelector("#exo12-sortie");
    const btnExistant = document.querySelector("#exo12-btn-existant");
    const btnInexistant = document.querySelector("#exo12-btn-inexistant");
    const btnReset = document.querySelector("#exo12-btn-reset");

    // Vérifications
    if (!radiosElements || radiosElements.length === 0) {
        console.log('Exo12: radios introuvables (input[name="exo12-niveau"]).');
        return;
    }
    if (!sortieElem) {
        console.log("Exo12: élément #exo12-sortie introuvable.");
        return;
    }
    if (!btnExistant) {
        console.log("Exo12: bouton #exo12-btn-existant introuvable.");
        return;
    }
    if (!btnInexistant) {
        console.log("Exo12: bouton #exo12-btn-inexistant introuvable.");
        return;
    }
    if (!btnReset) {
        console.log("Exo12: bouton #exo12-btn-reset introuvable.");
        return;
    }

    const texteOrigine = sortieElem.textContent;

    const mettreAJourSortie = () => {
        const radioCoche = document.querySelector(
            'input[name="exo12-niveau"]:checked'
        );

        if (!radioCoche) {
            sortieElem.textContent = "Niveau sélectionné : (aucun)";
            return;
        }

        sortieElem.textContent = "Niveau sélectionné : " + radioCoche.value;
    };

    radiosElements.forEach((radioElem) => {
        radioElem.addEventListener("change", mettreAJourSortie);
    });

    btnExistant.addEventListener("click", () => {
        const radioIntermediaire = document.querySelector(
            'input[name="exo12-niveau"][value="intermediaire"]'
        );

        if (radioIntermediaire === null) {
            sortieElem.textContent = "Niveau sélectionné : (valeur introuvable)";
            return;
        }

        radioIntermediaire.checked = true;
        mettreAJourSortie();
    });

    btnInexistant.addEventListener("click", () => {
        const radioInexistant = document.querySelector(
            'input[name="exo12-niveau"][value="inexistant"]'
        );

        if (radioInexistant === null) {
            sortieElem.textContent = "Niveau sélectionné : (valeur introuvable)";
        }
    });

    btnReset.addEventListener("click", () => {
        radiosElements.forEach((radioElem) => {
            radioElem.checked = false;
        });

        sortieElem.textContent = texteOrigine;
        mettreAJourSortie();
    });

    mettreAJourSortie();
};
