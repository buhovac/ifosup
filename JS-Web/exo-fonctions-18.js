const utilisateurs = [
    { email: "alice@example.com", accepteNewsletter: true,  actif: true },
    { email: "marc@example.com", accepteNewsletter: false, actif: true },
    { email: "nour@example.com", accepteNewsletter: true,  actif: false },
    { email: "sophie@example.com", accepteNewsletter: true,  actif: true }
];

const destinataires = utilisateurs.filter(
    u => u.accepteNewsletter && u.actif
);

const emails = destinataires.map(u => u.email);

console.log("Emails des destinataires :", emails);
