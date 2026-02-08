export const execExo08 = () =>
{
    console.log("----- Exo 08 -----");

    const champElem = document.querySelector("#exo08-prenom");
    const boutonAfficherElem = document.querySelector("#exo08-btn-afficher");
    const boutonResetElem = document.querySelector("#exo08-btn-reset");
    const valueElem = document.querySelector("#exo08-value");
    const defaultValueElem = document.querySelector("#exo08-defaultvalue");

    if (!champElem || !boutonAfficherElem || !boutonResetElem || !valueElem || !defaultValueElem) {
        console.log("Exo 08: élément manquant (#exo08-prenom, #exo08-btn-afficher, #exo08-btn-reset, #exo08-value, #exo08-defaultvalue).");
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
