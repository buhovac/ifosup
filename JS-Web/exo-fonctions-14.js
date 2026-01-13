const taches = [
    "Envoyer le mail au client",
    "Préparer le devis",
    "Mettre à jour le site"
];

const tachesFormatees = taches.map(tache => `→ ${tache}`);

console.log("Tâches originales :", taches);
console.log("Tâches formatées :", tachesFormatees);
