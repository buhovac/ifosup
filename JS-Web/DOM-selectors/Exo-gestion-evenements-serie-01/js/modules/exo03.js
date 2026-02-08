export const execExo03 = () => {
    console.log('----- Exo 03 -----');

    const champClavierElem = document.querySelector('#champ-clavier');

    champClavierElem.addEventListener('keydown', (event) => {
        console.log(`Touche pressée : ${event.key}`);
    });
};
