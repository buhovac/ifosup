export const execExo10 = () =>
{
    console.log("----- Exo 10 -----");

    const zoneSecondaireElem = document.querySelector("#zone-secondaire");

    // :scope znači "ovaj element", pa :scope > p hvata samo direktnu djecu <p>
    const zoneSecondaireDirectPElements = zoneSecondaireElem.querySelectorAll(":scope > p");

    console.log(zoneSecondaireDirectPElements);
};
