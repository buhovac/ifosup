function afficherTirageDuLotto(quantiteDeNombres, valeurMin, valeurMax)
{
    const resultatDuTirage = [];

    while (resultatDuTirage.length < quantiteDeNombres) {
        const nombre = Math.floor(
            Math.random() * (valeurMax - valeurMin + 1)
        ) + valeurMin;

        if (!resultatDuTirage.includes(nombre)) {
            resultatDuTirage.push(nombre);
        }
    }

    console.log("Résultat du tirage :", resultatDuTirage);
}

afficherTirageDuLotto(10, 1, 20);
