/* 
Variable lookup : process by which the program searches for a value 
associated with a variable name with regards to the scope chain
VISUALIZATION 
1. Current scope : where the variable was defined / iniatialized (global/local)
2. Outer Scopes : if the variable is not found in the current scope 
3. Global Scope : if the variable is not found in the inner / outer scope 
4. Undefined Scope : if the variable is not found in any scope 
*/
let x = 5

function outerFunction () {
     function innerFunction() {
          console.log(y)
     }
   

}


// taking input 
let userInput = prompt("Give me a number value for x:")
console.log(userInput)