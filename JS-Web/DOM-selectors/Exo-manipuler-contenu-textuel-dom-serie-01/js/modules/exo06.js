export const execExo06 = () =>
{
    console.log("----- Exo 06 -----");

    const zoneElem = document.querySelector("#exo06-zone");
    const btnTextContentElem = document.querySelector("#exo06-btn-textcontent");
    const btnInnerHtmlElem = document.querySelector("#exo06-btn-innerhtml");
    const btnResetElem = document.querySelector("#exo06-btn-reset");

    if (!zoneElem || !btnTextContentElem || !btnInnerHtmlElem || !btnResetElem) {
        console.log("Exo 06: élément manquant (#exo06-zone, #exo06-btn-textcontent, #exo06-btn-innerhtml, #exo06-btn-reset).");
        return;
    }

    const noteUtilisateur = `<img src="x" onerror="alert('Attaque XSS')">`;

    const texteRetour = "(Aucune note pour le moment)";

    btnTextContentElem.addEventListener("click", () =>
    {
        zoneElem.textContent = noteUtilisateur;
    });

    btnInnerHtmlElem.addEventListener("click", () =>
    {
        zoneElem.innerHTML = noteUtilisateur; // peut déclencher une alerte via onerror => illustration XSS
    });

    btnResetElem.addEventListener("click", () =>
    {
        zoneElem.textContent = texteRetour;
    });
};
