const formaterMessageTaches = (nombreTaches) => {
    if (nombreTaches <= 0) {
        return "Vous n'avez aucune tâche en attente.";
    } else if (nombreTaches === 1) {
        return "Vous n'avez qu'une seule tâche en attente.";
    } else {
        return `Vous avez ${nombreTaches} tâches en attente.`;
    }
};

// Tests
let messagePourUtilisateur;

messagePourUtilisateur = formaterMessageTaches(0);
console.log(messagePourUtilisateur);

messagePourUtilisateur = formaterMessageTaches(1);
console.log(messagePourUtilisateur);

messagePourUtilisateur = formaterMessageTaches(5);
console.log(messagePourUtilisateur);

messagePourUtilisateur = formaterMessageTaches(-3);
console.log(messagePourUtilisateur);
