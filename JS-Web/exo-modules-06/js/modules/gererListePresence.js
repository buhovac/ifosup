const noms = [];

export const ajouterNom = (nom) => {
    if (!noms.includes(nom)) {
        noms.push(nom);
    }
};

export const supprimerNom = (nom) => {
    const index = noms.indexOf(nom);
    if (index !== -1) {
        noms.splice(index, 1);
    }
};

export const afficherNoms = () => {
    if (noms.length === 0) {
        return "Aucun nom dans la liste.";
    }

    return noms.join(", ");
};
