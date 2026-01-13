const executerSiConnecte = (estConnecte, actionLorsqueConnecte) => {
    if (estConnecte) {
        actionLorsqueConnecte();
    } else {
        console.log("Accès refusé, merci de vous connecter.");
    }
};

// Utilisateur connecté
executerSiConnecte(true, () => {
    console.log("Ouverture du tableau de bord...");
});

// Utilisateur non connecté
executerSiConnecte(false, () => {
    console.log("Cette action ne devrait pas s'exécuter.");
});
