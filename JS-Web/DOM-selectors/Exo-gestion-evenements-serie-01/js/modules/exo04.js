export const execExo04 = () => {
    console.log('----- Exo 04 -----');

    const lienInterditElem = document.querySelector('#lien-interdit');

    lienInterditElem.addEventListener('click', (event) => {
        event.preventDefault();
        console.log('Navigation bloquée (preventDefault) !');
    });
};
