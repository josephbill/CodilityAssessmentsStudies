// // taking input 
// let userInput = prompt("Give me a number value for x:")
// console.log(userInput)

//using readline 

// Import the readline module
const readline = require('readline');

// Create an interface for input and output
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let globalName = ''
// Prompt the user for input
rl.question('What is your name? ', (name) => {
    console.log(`Hello, ${name}!`);
    globalName = name
    // Close the readline interface after use
    rl.close();
});

console.log("Outsude the asynchronous operations" , globalName)  //promises. 

// Asynchronous (when operations run independent of other operations) and Synchronous Operations (when operations in js are executed sequentially)
// function a , b , c 