// named function using the function keyword 
function nameoffunction(){

}
// functions with parameters (variables,whole functions)
function name_of_function(a,b){
    //validate if entries are integers ....
   let x  = a + b;
   console.log(x);
}
// if a function has named parameters , then during the call of the function , the function
// should indicate it's arguements. 
name_of_function(10,20);

//using a variable to reference a function 
const printName = function () {

}

printName();
printName //reference the variable. 

// arrow syntax 
const greet = (paremeters) => {

}

greet()

//with the arrow syntax and regular functions 5 key differences. 
// 1. this value
// 2. constructors (objects)
// 3. arguments object (parameters)
// 4. Implicit return
// 5. Methods.

// 1. this value
function myFunction(){
    console.log(this);
}

//
myFunction(); //this here references the global object 


// inside an arrow function , the this keyword always points or equals to 
// the value(s) of the outer function
// this inside an arrow function is mostly used in a callback scenerio

// callback functions. 
// function(s) passed to another function inform of arguements 
// usage here 
// 1. API calls (WK2. Communicating with servers )
// 2. DOM (listening to events)
// simple callback scenerio 

function add (a,b,callback){
   console.log(`${a + b }`);
   callback();
}

function disp(){
    console.log(`Callback example`);
}

add(5,6,disp);

// asynchronous operations : don't require a sequence -> invoked : erros and successes
// synchronous operations : sequence -> event , 

// callback in D.O.M 

//tagging the input world cup 
// let select = document.getElementById('dropdown');
// select.addEventListener('change', function () {
//     // execution is defined by the program. 
//     console.log(`The user has selected ${select.value} as the winner!`)
// } );


// now this keyword inside a arrow syntax
const myObject = {
    //is an outer function
    myMethod(items){
        console.log("From outer function" + this); //log out myObject
        // inner function 
        const callback = () => {
        console.log(this); //logs out the object 
        };
        //reference to the items 
        items.forEach(callback)
    }
} 

myObject.myMethod([1,2,3]);
