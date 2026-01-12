console.log("Hello, World!");

// Exercice 1
const a = 10;
const b = 18;

const moyenne = (a + b) / 2;

console.log(`La moyenne de ${a} et ${b} est égale à ${moyenne}.`);

// Exercice 2
let a2 = '2';
const b2 = 2;

const somme = parseInt(a2) + b2;

console.log(`La somme de ${a2} et ${b2} est égale à ${somme}.`);

// Exercice 3
const eleve1 = 'Sébastien';
const eleve2 = 'Martine';
const eleve1NoteMath = 4;
const eleve1NoteFrancais = 2;

const eleve2Citation = `Comme dirait ${eleve2} : "${eleve1} est un cancre, il n'a que ${(eleve1NoteMath + eleve1NoteFrancais) / 2} de moyenne !"`;

console.log(eleve2Citation);

// Exercice 4

const tableau1 = [8, 3, 4];

console.log(`La deuxième valeur du tableau est : ${tableau1[1]}.`);

tableau1[0] = 2;

tableau1.push(5);

tableau1.unshift(1);

const tableau2 = [6, 7, 8, 9, 10];

const tableauFusionne = tableau1.concat(tableau2);

console.log("Le tableau fusionné est :", tableauFusionne);

// Exercice 5

const film = ['Hellraiser', 'Jean-Michel Barker'];

console.log(`Le réalisateur du film est : ${film[1]}.`);

film[1] = 'Clive Barker';

film.push(1987);

console.log("Les informations mises à jour du film sont :", film);  

// Exercice 6

const filmObj = {
    nomDuFilm: 'Hellraiser',
    realisateur: 'Jean-Michel Barker'
};

console.log(`Le réalisateur du film est : ${filmObj.realisateur}.`);

filmObj.realisateur = 'Clive Barker';

filmObj.anneeDeSortie = 1987;

console.log("Les informations mises à jour du film sont :", filmObj);   

// Exercice 7

const horreur = [
    {
        nomDuFilm: 'Hellraiser',
        realisateur: 'Clive Barker',
        anneeDeSortie: 1987
    },
    {
        nomDuFilm: 'La colline a des yeux',
        realisateur: 'Alexandre Aja',
        anneeDeSortie: 2006
    }
];

console.log(`Le nom du premier film est : ${horreur[0].nomDuFilm}.`);

console.log(`Le réalisateur du second film est : ${horreur[1].realisateur}.`);

horreur[0].anneeDeSortie = 1990;

horreur.push({
    nomDuFilm: 'Heretic',
    realisateur: 'Scott Beck & Bryan Woods',
    anneeDeSortie: 2024
});

console.log("Le tableau complet :", horreur); 

// Exercice 8
