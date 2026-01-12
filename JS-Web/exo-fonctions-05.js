function afficherTirageDuLotto(quantiteDeNombres, valeurMin, valeurMax)
{
    const resultatDuTirage = [];

    for (let i = 0; i < quantiteDeNombres; i++) {
        const nombre = Math.floor(
            Math.random() * (valeurMax - valeurMin + 1)
        ) + valeurMin;

        resultatDuTirage.push(nombre);
    }

    console.log("Résultat du tirage :", resultatDuTirage);
}

afficherTirageDuLotto(10, 1, 20);
