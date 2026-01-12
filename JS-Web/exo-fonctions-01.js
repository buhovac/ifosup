function jouerAuNombreMystere()
{
    const nombreMystere = Math.floor(Math.random() * 100) + 1;
    console.log("DEBUG nombre mystère :", nombreMystere);

    let tentative;

    do {
        tentative = Number(prompt("Devinez le nombre mystère (entre 1 et 100) :"));

        if (tentative < nombreMystere) {
            alert("Trop petit !");
        } else if (tentative > nombreMystere) {
            alert("Trop grand !");
        } else {
            alert("Bravo ! Vous avez trouvé le nombre mystère !");
        }
    } while (tentative !== nombreMystere);
}

jouerAuNombreMystere();
