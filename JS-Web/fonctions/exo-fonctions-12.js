const taches = [
    'Envoyer le mail au client',
    'Relancer le fournisseur',
    'Préparer le rapport mensuel'
];

const pourChaqueTache = (listeTaches, action) => {
    for (let i = 0; i < listeTaches.length; i++) {
        const tache = listeTaches[i];
        action(tache, i);
    }
};

const afficherTacheAvecIndex = (tache, index) => {
    console.log(`${index} - ${tache}`);
};

pourChaqueTache(taches, afficherTacheAvecIndex);

const afficherTacheSiLongue = (tache, index) => {
    if (tache.length > 25) {
        console.log(`${index} - ${tache}`);
    }
};

pourChaqueTache(taches, afficherTacheSiLongue);
