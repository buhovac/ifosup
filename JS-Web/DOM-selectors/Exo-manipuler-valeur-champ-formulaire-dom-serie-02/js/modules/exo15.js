export const execExo15 = () => {
    console.log("----- Exo 15 -----");

    const champDateElem = document.querySelector("#exo15-echeance");
    const sortieElem = document.querySelector("#exo15-sortie");
    const boutonAujourdhuiElem = document.querySelector("#exo15-btn-aujourdhui");
    const boutonResetElem = document.querySelector("#exo15-btn-reset");

    // Vérifications
    if (!champDateElem) {
        console.log("Exo15: champ #exo15-echeance introuvable.");
        return;
    }
    if (!sortieElem) {
        console.log("Exo15: élément #exo15-sortie introuvable.");
        return;
    }
    if (!boutonAujourdhuiElem) {
        console.log("Exo15: bouton #exo15-btn-aujourdhui introuvable.");
        return;
    }
    if (!boutonResetElem) {
        console.log("Exo15: bouton #exo15-btn-reset introuvable.");
        return;
    }

    const texteOrigine = sortieElem.textContent;

    const mettreAJourSortie = () => {
        const valeurDate = champDateElem.value; // "YYYY-MM-DD" ou ""

        if (valeurDate === "") {
            sortieElem.textContent = texteOrigine;
            return;
        }

        const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(valeurDate);
        if (!match) {
            sortieElem.textContent = "Échéance : (date invalide)";
            return;
        }

        const annee = Number(match[1]);
        const mois = Number(match[2]); // 1..12
        const jour = Number(match[3]); // 1..31

        const dateChoisie = new Date(annee, mois - 1, jour, 12, 0, 0, 0);

        if (
            Number.isNaN(dateChoisie.getTime()) ||
            dateChoisie.getFullYear() !== annee ||
            dateChoisie.getMonth() !== mois - 1 ||
            dateChoisie.getDate() !== jour
        ) {
            sortieElem.textContent = "Échéance : (date invalide)";
            return;
        }

        const maintenant = new Date();
        const aujourdhui = new Date(
            maintenant.getFullYear(),
            maintenant.getMonth(),
            maintenant.getDate(),
            12,
            0,
            0,
            0
        );

        const msParJour = 24 * 60 * 60 * 1000;
        const diffJours = Math.round((dateChoisie - aujourdhui) / msParJour);

        if (diffJours < 0) {
            sortieElem.textContent =
                "Échéance : " +
                valeurDate +
                " (dépassée de " +
                Math.abs(diffJours) +
                " jour(s))";
            return;
        }

        if (diffJours === 0) {
            sortieElem.textContent = "Échéance : " + valeurDate + " (aujourd'hui)";
            return;
        }

        sortieElem.textContent =
            "Échéance : " + valeurDate + " (dans " + diffJours + " jour(s))";
    };

    champDateElem.addEventListener("change", mettreAJourSortie);

    boutonAujourdhuiElem.addEventListener("click", () => {
        const d = new Date();
        const yyyy = String(d.getFullYear());
        const mm = String(d.getMonth() + 1).padStart(2, "0");
        const dd = String(d.getDate()).padStart(2, "0");
        const aujourdhuiStr = `${yyyy}-${mm}-${dd}`;

        champDateElem.value = aujourdhuiStr;
        mettreAJourSortie();
    });

    boutonResetElem.addEventListener("click", () => {
        champDateElem.value = "";
        sortieElem.textContent = texteOrigine;
        mettreAJourSortie();
    });

    mettreAJourSortie();
};
