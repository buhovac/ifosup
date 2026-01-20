export default function selectionnerElementAleatoireDansTableau(tableau) {
    const randomDecimal = Math.random();
    const index = Math.floor(randomDecimal * tableau.length);
    return tableau[index];
}
