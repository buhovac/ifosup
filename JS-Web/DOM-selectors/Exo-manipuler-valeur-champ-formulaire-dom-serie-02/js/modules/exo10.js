export const execExo10 = () =>
{
    console.log("----- Exo 10 -----");

    const selectElem = document.querySelector("#exo10-pays");
    const sortieElem = document.querySelector("#exo10-sortie");
    const boutonInexistantElem = document.querySelector("#exo10-btn-inexistant");
    const boutonResetElem = document.querySelector("#exo10-btn-reset");

    if (!selectElem || !sortieElem || !boutonInexistantElem || !boutonResetElem) {
        console.log("Exo 10: élément manquant (#exo10-pays, #exo10-sortie, #exo10-btn-inexistant, #exo10-btn-reset).");
        return;
    }

    const mettreAJourSortie = () =>
    {
        if (!selectElem.value || selectElem.selectedOptions.length === 0) {
            sortieElem.textContent = "Sélection : (aucune option sélectionnée)";
            return;
        }

        sortieElem.textContent =
            "Sélection : " + selectElem.value + " (" + selectElem.selectedOptions[0].text + ")";
    };

    selectElem.addEventListener("change", () =>
    {
        mettreAJourSortie();
    });

    boutonInexistantElem.addEventListener("click", () =>
    {
        selectElem.value = "xx";
        mettreAJourSortie();
    });

    boutonResetElem.addEventListener("click", () =>
    {
        selectElem.value = "be";
        mettreAJourSortie();
    });

    mettreAJourSortie();
};
