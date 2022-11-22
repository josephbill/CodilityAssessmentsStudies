'use strict';
// JS -> OOP , PP : procedural programming
// objects 
// capabilities of an OOP language 
// 1. Encapsulation : capability of storing related info 
// 2. Aggregation : capability of storing one object inside another object 
// 3. Inheritance : //class based syntax OOP. 
// 4. Polymorphism : one function being used in a variety of ways.


//objects 
// composed of attributes (variables, properties)
// attributes contain methods (functions)

//defination of a custom object in JS
let book = new Object();
//assign properties/attributes 
book.coverTitle = "Gifted Hands";
book.author = "Ben Carson";


//

//define methods for our objects console.log("Book name is : " + book.coverTitle);

function addPrice(amount){
  //executions 
   //constructor to pass in the price 
   this.price = amount;
}
//to create an object with a user defined function 
//this  : ,in a function context 
function secondBook (title, author) {
    //constructor 
    this.title = title;
    this.author = author;
    this.addPrice = addPrice;
    //methods to work on the attributrs 
}

let book_two = new secondBook("Born a Crime", "Trevor Noah");
book_two.addPrice(1000);
console.log("our second book is " + book_two.title + " the price is " + book_two.price);


//creating objects 
// 1. Object literal syntax 
let newObject = {
    coverTitle: "c",
}

// 2. Object constructor 
//defination of a custom object in JS
// let book = new Object();
// //assign properties/attributes 
// book.coverTitle = "Gifted Hands";
// book.author = "Ben Carson";
// book.info = function () {
//     console.log(`${book.coverTitle}`)
// }

//  3. Constructor : template for how an object should be created 

//define methods for our objects 
// function addPrice(amount){
//     //executions 
//      //constructor to pass in the price 
//      this.price = amount;
//   }
//   //to create an object with a user defined function 
//   //this  : ,in a function context 
//   function secondBook (title, author) {
//       //constructor 
//       this.title = title;
//       this.author = author;
//       this.addPrice = addPrice;
//       //methods to work on the attributrs 
//   }
  
//   let book_two = new secondBook("Born a Crime", "Trevor Noah");
//   book_two.addPrice(1000);
//   console.log("our second book is " + book_two.title + " the price is " + book_two.price);


// 4. Prototypes. //inherit all methods and properties of the copied object 
//object A  //list of teams qualified for the WOrld cup 
let teams = { 
    teamA: 'Brazil',
    teamB: 'Iran'
}

//object B //teams not qualified 
let teams_eliminated = Object.create(teams)
let displined_teams = Object.create(teams)
console.log(displined_teams.teamA);
console.log(teams_eliminated["teamB"]);

// Inherited properties 
//own props 
const user = {
    name : 'Joseph',
    age: 26,
    toString (){
        return 'Hey There!';
    }
}

console.log(user.toString()); //hey there

// getOwnPropertyNames();

const props  = Object.getOwnPropertyNames(user);
console.log(props); //true
//hasOwnProperty()
user.hasOwnProperty('name'); //true 
user.hasOwnProperty('email'); //false -> point to an inherited prop. 


//nested properties  // inheritance 
let departmentIT = Object.create(user,{
    unit:{
        unita: 'Computer Science'
    }
   
})

console.log(departmentIT.toString()); //override in string.

//transverse / Loop / iterate -> Object 
// access keys inside the object 
// enumerable -> methods can be attached/executed on items during looping
// for ... in construct will only work on enumerables 
// inherited properties from the Object.property construct in objects are not enumerable. 
// but inherited props from other objects are enumerable .

let person  = {
    gender: 'male'
}

let person2 = Object.create(person);
person2.name = "joseph";
person2.nationality = "kenyan";

//to transverse and access the keys 
for (let key in person2 ){
    //validation
    // > ES8 , Object.entries() : keys and values , Object.values()
    if(person2.hasOwnProperty(key)){
    //execute different functions on the key 
    console.log(`${key} : ${person2[key]}`);
    }
}

//delete a prop from an object 
//delete operator 
delete person2.nationality;

console.log(person2.nationality);


