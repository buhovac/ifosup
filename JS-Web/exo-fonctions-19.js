const produits = [
    { nom: "Souris sans fil", categorie: "accessoires", stock: 12 },
    { nom: "Clavier mécanique", categorie: "accessoires", stock: 0  },
    { nom: "Écran 27 pouces", categorie: "ecrans", stock: 5  },
    { nom: "Tapis de souris XL", categorie: "accessoires", stock: 7  }
];

const produitsAffiches = produits.filter(
    p => p.categorie === "accessoires" && p.stock > 0
);

console.log("Produits à afficher :", produitsAffiches);
