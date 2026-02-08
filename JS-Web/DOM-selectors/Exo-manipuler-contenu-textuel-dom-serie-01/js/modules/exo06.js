export const execExo06 = () => {
    console.log('----- Exo 06 -----');

    const boutonTestElem = document.querySelector('#btn-test');
    const boutonActiverElem = document.querySelector('#btn-activer');
    const boutonDesactiverElem = document.querySelector('#btn-desactiver');

    let ecouteurBoutonTestEstActif = false;

    const gestionClicBoutonTest = () => {
        console.log('Le bouton Test est actif !');
    };

    boutonActiverElem.addEventListener('click', () => {
        if (ecouteurBoutonTestEstActif) {
            console.log("Déjà actif : l'écouteur est déjà en place.");
            return;
        }

        boutonTestElem.addEventListener('click', gestionClicBoutonTest);
        ecouteurBoutonTestEstActif = true;
        console.log('Écouteur ACTIVÉ.');
    });

    boutonDesactiverElem.addEventListener('click', () => {
        if (!ecouteurBoutonTestEstActif) {
            console.log("Déjà inactif : aucun écouteur à retirer.");
            return;
        }

        boutonTestElem.removeEventListener('click', gestionClicBoutonTest);
        ecouteurBoutonTestEstActif = false;
        console.log('Écouteur SUPPRIMÉ.');
    });
};
