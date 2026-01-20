const commandes = [120, 90, 45, 230];

const chiffreAffaires = commandes.reduce(
    (acc, montantActuel) => acc + montantActuel,
    0
);

console.log(`Chiffre d'affaire du jour : ${chiffreAffaires} €`);
