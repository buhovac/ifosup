export const execExo09 = () =>
{
    console.log("----- Exo 09 -----");

    const champElem = document.querySelector("#exo09-message");
    const boutonAfficherElem = document.querySelector("#exo09-btn-afficher");
    const boutonResetElem = document.querySelector("#exo09-btn-reset");
    const valueElem = document.querySelector("#exo09-value");
    const defaultValueElem = document.querySelector("#exo09-defaultvalue");

    if (!champElem || !boutonAfficherElem || !boutonResetElem || !valueElem || !defaultValueElem) {
        console.log("Exo 09: élément manquant (#exo09-message, #exo09-btn-afficher, #exo09-btn-reset, #exo09-value, #exo09-defaultvalue).");
        return;
    }

    const texteVide = "(vide)";

    boutonAfficherElem.addEventListener("click", () =>
    {
        valueElem.textContent = "value : " + champElem.value;
        defaultValueElem.textContent = "defaultValue : " + champElem.defaultValue;
    });

    boutonResetElem.addEventListener("click", () =>
    {
        valueElem.textContent = "value : (vide)";
        defaultValueElem.textContent = "defaultValue : (vide)";
    });
};
