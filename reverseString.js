let inputString = prompt("Digite uma string: ");
let reversedString = "";

for(let i = inputString.length - 1; i >= 0; i--) {
  reversedString += inputString[i];
}

console.log("A string invertida é: " + reversedString);
