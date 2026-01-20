const genererMessageStatutServeur = () => {
    const estEnMaintenance = true;

    if (estEnMaintenance) {
        return "Le serveur est en maintenance : il est indisponible.";
    } else {
        return "Le serveur fonctionne normalement : il est disponible.";
    }
};

const messageStatut = genererMessageStatutServeur();
console.log(messageStatut);
