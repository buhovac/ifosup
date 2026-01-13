const avis = [
    { auteur: "Alice", note: 5 },
    { auteur: "Marc", note: 1 },
    { auteur: "Luc", note: 3 },
    { auteur: "Nour", note: 4 },
    { auteur: "Sophie", note: 2 }
];

const avisPositifs = avis.filter(a => a.note >= 3);

console.log("Nombre d'avis positifs :", avisPositifs.length);
console.log("Avis positifs :", avisPositifs);
