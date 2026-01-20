
import { enregistrerEvenement as enregistrerEvenementUtilisateur } from "./modules/journalUtilisateur.js";
import { enregistrerEvenement as enregistrerEvenementSysteme } from "./modules/journalSysteme.js";

console.log(enregistrerEvenementUtilisateur("Connexion réussie"));
console.log(enregistrerEvenementSysteme("Cache vidé"));
