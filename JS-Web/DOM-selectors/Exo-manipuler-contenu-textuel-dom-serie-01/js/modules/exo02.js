export const execExo02 = () => {
    console.log('----- Exo 02 -----');

    const zoneSourisElem = document.querySelector('#zone-souris');

    zoneSourisElem.addEventListener('mousemove', (event) => {
        const x = event.clientX;
        const y = event.clientY;
        console.log(`Position X: ${x}, Position Y: ${y}`);
    });
};
