//Tmperature given in kelvin
const kelvin = 0;

//celsius is 273 degree less than kelvin
const celsius = kelvin - 273;

//Convert celsius to fahrenheit
let fahrenheit = celsius *(9/5)+32;
//Round the fahrenheit down
fahrenheit = Math.floor(fahrenheit);

//Convert celsius to Newton
let newton = celsius*(33/100);
//Round Newton down 
newton = Math.floor(newton);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);
console.log(`The temperature is ${newton} N.`);
