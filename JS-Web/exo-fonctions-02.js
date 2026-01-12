function jouerAuNombreMystere(nombreMin, nombreMax)
{
    const nombreMystere = Math.floor(
        Math.random() * (nombreMax - nombreMin + 1)
    ) + nombreMin;

    console.log("DEBUG nombre mystère :", nombreMystere);

    let tentative;

    do {
        tentative = Number(
            prompt(`Devinez le nombre mystère (entre ${nombreMin} et ${nombreMax}) :`)
        );

        if (tentative < nombreMystere) {
            alert("Trop petit !");
        } else if (tentative > nombreMystere) {
            alert("Trop grand !");
        } else {
            alert("Bravo ! Vous avez trouvé le nombre mystère !");
        }
    } while (tentative !== nombreMystere);
}

jouerAuNombreMystere(10, 30);
