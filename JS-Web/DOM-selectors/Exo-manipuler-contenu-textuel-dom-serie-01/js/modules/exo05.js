export const execExo05 = () => {
    console.log('----- Exo 05 -----');

    const boutonsParamElements = document.querySelectorAll('.js-btn-param');

    const saluerUtilisateur = (nom) => {
        console.log(`Bonjour ${nom} !`);
    };

    for (const bouton of boutonsParamElements) {
        bouton.addEventListener('click', () => {
            saluerUtilisateur(bouton.innerText);
        });
    }
};
