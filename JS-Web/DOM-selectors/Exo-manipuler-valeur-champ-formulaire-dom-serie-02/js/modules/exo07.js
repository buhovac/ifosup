export const execExo07 = () =>
{
    console.log("----- Exo 07 -----");

    const champNomElem = document.querySelector("#exo07-nom");
    const sortieElem = document.querySelector("#exo07-sortie");

    if (!champNomElem || !sortieElem) {
        console.log("Exo 07: élément manquant (#exo07-nom ou #exo07-sortie).");
        return;
    }

    champNomElem.addEventListener("input", () =>
    {
        const valeurBrute = champNomElem.value;

        console.log(JSON.stringify(valeurBrute));

        let valeurNettoyee = valeurBrute.trim();

        if (valeurNettoyee === "") {
            valeurNettoyee = "(vide)";
        }

        sortieElem.textContent = "Nom affiché : " + valeurNettoyee;
    });
};
