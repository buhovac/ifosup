export const execExo11 = () =>
{
    console.log("----- Exo 11 -----");

    const caseElem = document.querySelector("#exo11-newsletter");
    const sortieElem = document.querySelector("#exo11-sortie");
    const boutonConsoleElem = document.querySelector("#exo11-btn-console");
    const boutonResetElem = document.querySelector("#exo11-btn-reset");

    if (!caseElem || !sortieElem || !boutonConsoleElem || !boutonResetElem) {
        console.log("Exo 11: élément manquant (#exo11-newsletter, #exo11-sortie, #exo11-btn-console, #exo11-btn-reset).");
        return;
    }

    const texteOrigine = sortieElem.textContent;

    caseElem.addEventListener("change", () =>
    {
        if (caseElem.checked) {
            sortieElem.textContent = "Préférence : Activée";
        } else {
            sortieElem.textContent = "Préférence : Désactivée";
        }
    });

    boutonConsoleElem.addEventListener("click", () =>
    {
        console.log("caseElem.checked =", caseElem.checked);
        console.log("caseElem.defaultChecked =", caseElem.defaultChecked);
    });

    boutonResetElem.addEventListener("click", () =>
    {

        sortieElem.textContent = texteOrigine;
    });
};
