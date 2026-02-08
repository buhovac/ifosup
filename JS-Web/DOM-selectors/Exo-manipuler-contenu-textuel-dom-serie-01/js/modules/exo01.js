export function execExo01() {
    console.log('----- Exo 01 -----');

    const boutonClicElem = document.querySelector('#btn-clic');

    boutonClicElem.addEventListener('click', () => {
        console.log('Clic détecté !');
    });
}
