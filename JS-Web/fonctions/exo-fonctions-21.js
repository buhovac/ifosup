const sessions = [
    { pseudo: "Alice", dureeMinutes: 30 },
    { pseudo: "Marc", dureeMinutes: 45 },
    { pseudo: "Nour", dureeMinutes: 25 },
    { pseudo: "Sophie", dureeMinutes: 50 }
];

const dureeTotale = sessions.reduce(
    (acc, session) => acc + session.dureeMinutes,
    0
);

const dureeMoyenne = dureeTotale / sessions.length;

console.log(`Durée totale : ${dureeTotale} minutes`);
console.log(`Durée moyenne : ${dureeMoyenne} minutes`);
