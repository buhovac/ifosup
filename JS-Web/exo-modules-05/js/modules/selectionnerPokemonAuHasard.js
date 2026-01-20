const pokemonPopulaires = [
    "Pikachu",
    "Greninja",
    "Lucario",
    "Mimikyu",
    "Charizard",
    "Umbreon",
    "Sylveon",
    "Garchomp",
    "Rayquaza",
    "Gengar",
];

export const selectionnerPokemonAuHasard = () => {
    const randomDecimal = Math.random();
    const index = Math.floor(randomDecimal * pokemonPopulaires.length);
    return pokemonPopulaires[index];
};
