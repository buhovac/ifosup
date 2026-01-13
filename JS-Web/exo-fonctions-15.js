const utilisateurs = [
    { prenom: "Nour", nom: "El Amrani" },
    { prenom: "Marc", nom: "Renard" },
    { prenom: "Sophie", nom: "Lambert" }
];

const nomsComplets = utilisateurs.map(
    utilisateur => `${utilisateur.prenom} ${utilisateur.nom}`
);

console.log("Utilisateurs :", utilisateurs);
console.log("Noms complets :", nomsComplets);
