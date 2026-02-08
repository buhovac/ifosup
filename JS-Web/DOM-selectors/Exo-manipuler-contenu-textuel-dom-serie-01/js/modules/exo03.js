export const execExo03 = () =>
{
    console.log("----- Exo 03 -----");

    const zoneElem = document.querySelector("#exo03-zone");
    const boutonToggleElem = document.querySelector("#exo03-btn-toggle");

    if (!zoneElem || !boutonToggleElem) {
        console.log("Exo 03: élément manquant (#exo03-zone ou #exo03-btn-toggle).");
        return;
    }

    const texteRetour = "(Aucun message pour le moment)";

    const gabaritHtml = `<p><b>Info</b> : maintenance prévue.</p>
<ul>
    <li>Début : 22h00.</li>
    <li>Durée estimée : 30 minutes.</li>
    <li>Impact : accès intermittent.</li>
</ul>`;

    let messageEstAffiche = false;


    zoneElem.textContent = texteRetour;
    boutonToggleElem.textContent = "Afficher le message";

    boutonToggleElem.addEventListener("click", () =>
    {
        messageEstAffiche = !messageEstAffiche;

        if (messageEstAffiche) {

            zoneElem.innerHTML = gabaritHtml;
            boutonToggleElem.textContent = "Masquer le message";
        } else {
            zoneElem.textContent = texteRetour;
            boutonToggleElem.textContent = "Afficher le message";
        }
    });
};
