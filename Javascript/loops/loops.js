// // for loop statement 
// // for defination 
// //arrays 
// // for loop : loops through a block of code a number of times 
// const numbers = [1,2,3,4,5];
// console.log(numbers.length);
// for (let index = 0; index < numbers.length; index++){
//     console.log(numbers[index]);
// }
// //index is the number of items in the array (items inside the db of jumia)
// //

// //for in loop : loops through the props. of an object 
// // for (key in object){
// //   //code to be executed.
// // }

// const person = { 
//   fname: "Joseph",
//   lname: "Mbugua"
// };

// for (let x in person){
//   console.log(person[x]);
// }

// //for ... of : loops through the values of an iterable object 
// // // for (variable of iterable){

// // }
// const cars = ['BMW','Volvo','mini'];
// for (let x of cars){
//    console.log("Car at yard " + x)
// }

// // for each : method callls a functions for each element in an array.
// // syntax 
// // arrayName.forEach(function(currentValue, index , arr), thisVal)
// // get the sum of the items in the numbers_array array. 
// let sum = 0;
// const numbers_array = [65,100,2,14];
// numbers_array.forEach(mySum)
// function mySum(item){
//     sum += item
// }


// // the while loops : loops through a block of code as long as a specified condition is true 
// // while (condition){
// //   //code to be executed.
//      // optional increment or decrement attached. 
// // }
// let i = 0;
// let text = " ";
// while (i < 11){
//   text += "The number is " + i;
//   console.log(text);
//   // //increment 
//    i++;
// }


// // do ... while : statement combo that defines a block of code to be executed once 
// //and then repeated as long as a specified condition is true 
// // do {
// // // code to be executed 
// // // optional incrementor or decrementor 
// // } while (condition);


// do {
//   text += i;
//   console.log(text);
//   i++;
// } while(i < 6);

// iterations : repeating tasks : for a constant or collections 
// Range(start, stop , step)

// Example: Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
// should consist of n rows, where n is a given positive integer, and consecutive rows should
// contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:
// *
// * *
// * * *
// * * * *

// 1. positive integer : n 
// 2. trasversal aspect : i need to move from 4 to 1 or 1 to 4 
// 3. each asterisks separated by spaces
// 4. n represents the number of rows 

function printAsters(n) {
   let result = ''
   for(let i = 1; i <= n; i++){
      let row = ''; // the first loop // creates the rows.
      for(let j=1; j <= i; j++){
        row += '* ';
      }
      result += row + '\n';
   }
   return result
}
let n = 10
console.log(printAsters(n))