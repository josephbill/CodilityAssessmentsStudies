// for loop statement 
// for defination 
//arrays 
// for loop : loops through a block of code a number of times 
const numbers = [1,2,3,4,5];
console.log(numbers.length);
for (let index = 0; index < numbers.length; index++){
    console.log(numbers[index]);
}
//index is the number of items in the array (items inside the db of jumia)
//

//for in loop : loops through the props. of an object 
// for (key in object){
//   //code to be executed.
// }

const person = { 
  fname: "Joseph",
  lname: "Mbugua"
};

for (let x in person){
  console.log(person[x]);
}

//for ... of : loops through the values of an iterable object 
// // for (variable of iterable){

// }
const cars = ['BMW','Volvo','mini'];
for (let x of cars){
   console.log("Car at yard " + x)
}

// for each : method callls a functions for each element in an array.
// syntax 
// arrayName.forEach(function(currentValue, index , arr), thisVal)
// get the sum of the items in the numbers_array array. 
let sum = 0;
const numbers_array = [65,100,2,14];
numbers_array.forEach(mySum)
function mySum(item){
    sum += item
}


// the while loops : loops through a block of code as long as a specified condition is true 
// while (condition){
//   //code to be executed.
     // optional increment or decrement attached. 
// }
let i = 0;
let text = " ";
while (i < 11){
  text += "The number is " + i;
  console.log(text);
  // //increment 
   i++;
}


// do ... while : statement combo that defines a block of code to be executed once 
//and then repeated as long as a specified condition is true 
// do {
// // code to be executed 
// // optional incrementor or decrementor 
// } while (condition);


do {
  text += i;
  console.log(text);
  i++;
} while(i < 6);