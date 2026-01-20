function afficherTirageDuLotto()
{
    const resultatDuTirage = [];

    for (let i = 0; i < 7; i++) {
        const nombre = Math.floor(Math.random() * 45) + 1;
        resultatDuTirage.push(nombre);
    }

    console.log("Résultat du tirage :", resultatDuTirage);
}

afficherTirageDuLotto();
