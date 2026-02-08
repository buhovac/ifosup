export const execExo17 = () =>
{
    console.log("----- Exo 17 -----");

    const champsRequiredHorsMdpElements = document.querySelectorAll(
        '[required]:not([type="password"])'
    );

    console.log(champsRequiredHorsMdpElements);
};
