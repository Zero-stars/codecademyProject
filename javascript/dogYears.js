/*
Program that convert to human age to dog year based on:
  1) The first two years of a dog’s life count as 10.5 dog years each.
  2) Each year following equates to 4 dog years. 
*/

//set my age(23) to the variable myAge
const myAge = 23;

//Two years are consider early year
let earlyYears = 2;
//Multiply by 10.5 to find the total early year
earlyYears*=10.5;
//The difference between myAge and first two years will give the later years
laterYears= myAge - 2;
//Each later year is 4 dog years
laterYears*=4;

//Add the early dog year and later dog year to find the age in dog year
const myAgeInDogYears = earlyYears + laterYears;

const myName="Stephen Lin".toLowerCase();

console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`);
