const produits = [
    { nom: "Clavier", prixHT: 40 },
    { nom: "Souris", prixHT: 25 },
    { nom: "Écran 24 pouces", prixHT: 199 }
];

const tauxTVA = 0.21;

const produitsAffiches = produits.map(produit => {
    const prixTTC = produit.prixHT * (1 + tauxTVA);

    return {
        nom: produit.nom,
        prixHT: produit.prixHT,
        prixTTC: prixTTC,
        libelle: `${produit.nom} : ${prixTTC.toFixed(2)} € TTC`
    };
});

console.log("Produits originaux :", produits);
console.log("Produits affichés :", produitsAffiches);
