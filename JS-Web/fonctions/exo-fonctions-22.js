const taches = [
    { intitule: "Envoyer le contrat", terminee: true  },
    { intitule: "Relancer le client", terminee: false },
    { intitule: "Mettre à jour le dossier", terminee: true  },
    { intitule: "Archiver les anciens mails", terminee: false }
];

const nombreTachesTerminees = taches.reduce(
    (acc, tache) => tache.terminee ? acc + 1 : acc,
    0
);

console.log(`${nombreTachesTerminees} tâches terminées sur ${taches.length}`);
