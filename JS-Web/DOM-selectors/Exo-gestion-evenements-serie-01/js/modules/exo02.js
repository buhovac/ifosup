export const execExo12 = () =>
{
    console.log("----- Exo 12 -----");

    const formElem = document.querySelector("#form-inscription");
    const champsRequiredElements = formElem.querySelectorAll("[required]");

    console.log(champsRequiredElements);
    console.log("length:", champsRequiredElements.length);
};
