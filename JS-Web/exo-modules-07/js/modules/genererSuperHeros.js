import * as mots from "./donnees.js";
import choisirMotAleatoire from "./selectionAleatoireDansTableau.js";

export function genererSuperHeros() {
    const adjectifs = mots.obtenirAdjectifs();
    const animaux = mots.obtenirAnimaux();
    const pouvoirs = mots.obtenirPouvoirs();

    const adjectif = choisirMotAleatoire(adjectifs);
    const animal = choisirMotAleatoire(animaux);
    const pouvoir = choisirMotAleatoire(pouvoirs);

    return `${adjectif} ${animal} avec ${pouvoir}`;
}
