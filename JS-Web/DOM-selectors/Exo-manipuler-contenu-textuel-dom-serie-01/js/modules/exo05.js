export const execExo05 = () =>
{
    console.log("----- Exo 05 -----");

    const etatElem = document.querySelector("#exo05-etat");
    const majElem = document.querySelector("#exo05-maj");
    const boutonSwitchElem = document.querySelector("#exo05-btn-switch");
    const boutonRefreshElem = document.querySelector("#exo05-btn-refresh");
    const carteElem = document.querySelector("#exo05-carte");

    if (!etatElem || !majElem || !boutonSwitchElem || !boutonRefreshElem || !carteElem) {
        console.log("Exo 05: élément manquant (#exo05-etat, #exo05-maj, #exo05-btn-switch, #exo05-btn-refresh, #exo05-carte).");
        return;
    }

    const ETAT_DISPO = "En stock";
    const ETAT_INDISPO = "Rupture";

    const dateDuMoment = () => new Date().toLocaleString();

    const texteRefreshOrigine = boutonRefreshElem.textContent; // "Rafraîchir les textes (textContent)"

    boutonSwitchElem.addEventListener("click", () =>
    {
        etatElem.textContent = (etatElem.textContent === ETAT_DISPO) ? ETAT_INDISPO : ETAT_DISPO;
        majElem.textContent = dateDuMoment();
    });

    boutonRefreshElem.addEventListener("click", () =>
    {
        const now = new Date();

        majElem.textContent = now.toLocaleString();

        const heure = now.toLocaleTimeString(); // [heure]
        boutonRefreshElem.textContent = `${texteRefreshOrigine} (fait à ${heure})`;
    });
};
