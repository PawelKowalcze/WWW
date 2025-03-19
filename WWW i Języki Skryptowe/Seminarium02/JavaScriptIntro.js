
console.log("Hello, World!");
let y = 20; //zakres blokowy
const z = 30; //zakres blokowy

let number = 45; //Number
let string = "Hello"; //String
let boolean = true; //Boolean
let object = {name: "John", age: 30}; //Object
let array = [1, 2, 3, 4, 5]; //Array

let student = {
    imie: "Jan",
    nazwisko: "Kowalski",
    wiek: 20,
    przedmioty: ["WWW", "JS", "Python"],
    oceny: [5, 4.5, 3]
};

console.log(student.imie);
console.log(student["imie"]);
console.log(student.nazwisko);
console.log(student.wiek);
console.log(student.przedmioty);
console.log(student.oceny[0]);
console.log(`Cześć, mam na imię ${student.imie} i mam ${student.wiek} lat.`);

console.log(y + z);