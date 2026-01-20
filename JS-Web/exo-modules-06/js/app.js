import { ajouterNom, supprimerNom, afficherNoms } from "./modules/gererListePresence.js";

console.log(afficherNoms());

ajouterNom("Lambert");
ajouterNom("Dupont");
ajouterNom("El Amrani");

console.log(afficherNoms());

supprimerNom("Dupont");

console.log(afficherNoms());
