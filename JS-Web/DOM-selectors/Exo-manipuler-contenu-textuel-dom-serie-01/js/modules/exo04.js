export const execExo04 = () =>
{
    console.log("----- Exo 04 -----");

    const carteElem = document.querySelector("#exo04-carte");
    const etatElem = document.querySelector("#exo04-etat");
    const majElem = document.querySelector("#exo04-maj");
    const boutonSwitchElem = document.querySelector("#exo04-btn-switch");
    const boutonRefreshElem = document.querySelector("#exo04-btn-refresh");
    const boutonResetElem = document.querySelector("#exo04-btn-reset");

    if (!carteElem || !etatElem || !majElem || !boutonSwitchElem || !boutonRefreshElem || !boutonResetElem) {
        console.log("Exo 04: élément manquant (#exo04-carte, #exo04-etat, #exo04-maj, #exo04-btn-switch, #exo04-btn-refresh, #exo04-btn-reset).");
        return;
    }

    const carteHtmlOrigine = carteElem.innerHTML;

    const ETAT_DISPO = "En stock";
    const ETAT_INDISPO = "Rupture";
    const DATE_INIT = "Aucune";

    const dateDuMoment = () => new Date().toLocaleString();

    const poserEcouteurSwitch = (btn) =>
    {
        btn.addEventListener("click", () =>
        {
            etatElem.textContent = (etatElem.textContent === ETAT_DISPO) ? ETAT_INDISPO : ETAT_DISPO;

            majElem.textContent = dateDuMoment();
        });
    };

    poserEcouteurSwitch(boutonSwitchElem);

    boutonRefreshElem.addEventListener("click", () =>
    {
        const etatCourant = etatElem.textContent;
        const dateCourante = dateDuMoment();

        carteElem.innerHTML = `
      <h3>Produit : Clavier mécanique</h3>
      <p>Disponibilité : <span id="exo04-etat">${etatCourant}</span></p>
      <p>Dernière mise à jour : <span id="exo04-maj">${dateCourante}</span></p>
      <button id="exo04-btn-switch">Basculer disponibilité</button>
    `;
        const newEtat = document.querySelector("#exo04-etat");
        const newMaj = document.querySelector("#exo04-maj");
        if (newEtat) etatElem.textContent = newEtat.textContent; // garde cohérence
        if (newMaj) majElem.textContent = newMaj.textContent;
    });

    boutonResetElem.addEventListener("click", () =>
    {
        carteElem.innerHTML = carteHtmlOrigine;

        const etatRecree = document.querySelector("#exo04-etat");
        const majRecree = document.querySelector("#exo04-maj");
        const switchRecree = document.querySelector("#exo04-btn-switch");

        if (!etatRecree || !majRecree || !switchRecree) {
            console.log("Exo 04 reset: éléments recréés introuvables.");
            return;
        }

        majRecree.textContent = DATE_INIT;

        etatElem.textContent = etatRecree.textContent;
        majElem.textContent = majRecree.textContent;

        poserEcouteurSwitch(switchRecree);
    });
};
