//create an array 
const fruits  = ['apple', 'banana'];

//get length for array 
console.log(fruits.length);
//access item via index position  
console.log(fruits[0]);
// The index of an array's second element is always 1.
fruits[1]; // Banana
// The index of an array's last element is always one less than the length of the array.
fruits[fruits.length - 1]; // Banana
// Using a index number larger than the array's length
// returns 'undefined'.
fruits[99]; // undefined

//to get index of item 
console.log(fruits.indexOf('banana')) //returns one 

//check if an array contains a certain item 
fruits.includes('Banana'); //returns true
fruits.includes('cherry'); //returns false 

//using index of to check if array contains the given item
fruits.indexOf('Banana') !== -1; // true
fruits.indexOf('Cherry') !== -1; // false

//add item to an array 
const newLength = fruits.push('Orange');
//remove last item from an array 
const removeItem = fruits.pop();
//remove multiple items from end of an array 
const fruits_two = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Cherry'];
const start = -3;
//use splice
const removedItems = fruits_two.splice(start);
console.log(fruits_two);

//remove from start of an array 
// const fruits_two = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Cherry'];
// const start = 3;  //change this to positive value
// //use splice
// const removedItems = fruits_two.splice(start);
// console.log(fruits_two);


//remove first item from array 
console.log(fruits_two.shift());
//add a new first item to an array 
console.log(fruits_two.unshift('Strawberry'));

//remove a single item by index
// const fruits = ['Strawberry', 'Banana', 'Mango'];
// const start = fruits.indexOf('Banana');
// const deleteCount = 1;
// const removedItems = fruits.splice(start, deleteCount);
// console.log(fruits);
// // ["Strawberry", "Mango"]
// console.log(removedItems);
// // ["Banana"]

//remove multiple items by index 
// const fruits = ['Apple', 'Banana', 'Strawberry', 'Mango'];
// const start = 1;
// const deleteCount = 2;
// const removedItems = fruits.splice(start, deleteCount);
// console.log(fruits);
// // ["Apple", "Mango"]
// console.log(removedItems);
// // ["Banana", "Strawberry"]

//iterate over an array 

//use a for of. .
const fruits_three = ['Apple', 'Mango', 'Cherry'];
for (const fruit of fruits_three) {
  console.log(fruits_three);
}

// every method 
//  tests whether all elements in the array pass the test implemented by the provided function.
// It returns a Boolean value.

const isBelowThreshold = (currentValue) => currentValue < 40;

const array1 = [1, 30, 39, 29, 10, 13];

console.log(array1.every(isBelowThreshold));
// expected output: true


// filter method 
// creates a shallow copy of a portion of a given array,
// filtered down to just the elements from the given array that pass the test implemented by the 
// provided function.

const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter(word => word.length > 6);

console.log(result);


// flatmap method 
// returns a new array formed by applying a given callback function to each element of the array,
// and then flattening the result by one level.
const arr1 = [1, 2, [3], [4, 5], 6, []];

const flattened = arr1.flatMap(num => num);

console.log(flattened);

// map method 
// creates a new array populated with the results of calling a provided 
// function on every element in the calling array.

const array2 = [1, 4, 9, 16];

// pass a function to map
const map1 = array2.map(x => x * 2);

console.log(map1);
// expected output: Array [2, 8, 18, 32]

// reduce method
// method executes a user-supplied "reducer" callback function on each element of the array, in order.
// passing in the return value from the calculation on the preceding element.

const array3 = [1, 2, 3, 4];

// 0 + 1 + 2 + 3 + 4
const initialValue = 0;
const sumWithInitial = array3.reduce(
  (previousValue, currentValue) => previousValue + currentValue,
  initialValue
);

console.log(sumWithInitial);
// expected output: 10


// reduce right method 
// applies a function against an accumulator and each value of the array (from right-to-left) 
// to reduce it to a single value.

// accumulator is the value returned from the previous iteration. 
// It will be initialValue for the first iteration. currentValue is array item in the current iteration.
const arrayfour = [[0, 1], [2, 3], [4, 5]];

const result1 = arrayfour.reduceRight((accumulator, currentValue) => accumulator.concat(currentValue));

console.log(result);

// to call a function on each element of the array 
//use for each or for of really 

// const fruits = ['Apple', 'Mango', 'Cherry'];
// fruits.forEach((item, index, array) => {
//   console.log(item, index);
// });
// // Apple 0
// // Mango 1
// // Cherry 2


//merge multiple arrays together 
// use the concat method 
const moreFruits = ['Mango', 'Cherry'];
const combinedFruits = fruits.concat(moreFruits);
console.log(combinedFruits);

// copy an array
const fruitscopying = ['Strawberry', 'Mango'];

// Create a copy using spread syntax.
const fruitsCopy = [...fruitscopying];
// ["Strawberry", "Mango"]

// Create a copy using the from() method.
const fruitsCopy2 = Array.from(fruitscopying);
// ["Strawberry", "Mango"]

// Create a copy using the slice() method.
const fruitsCopy3 = fruitscopying.slice();
// ["Strawberry", "Mango"]


// A deep copy of an object is a copy whose properties 
// do not share the same references (point to the same underlying values) 
// as those of the source object from which the copy was made. 
// As a result, when you change either the source or the copy,
//  you can be assured you're not causing the other object to change too;

// we create deep copies using 
// JSON.stringify() to convert the array to a JSON string
// JSON.parse() to convert the string back into a new array that's completely independent from the original
// array.


//reverse method 
// reverses an array 

// const array1 = ['one', 'two', 'three'];
// console.log('array1:', array1);
// // expected output: "array1:" Array ["one", "two", "three"]

// const reversed = array1.reverse();
// console.log('reversed:', reversed);
// // expected output: "reversed:" Array ["three", "two", "one"]

// // Careful: reverse is destructive -- it changes the original array.
// console.log('array1:', array1);


// the some method
// tests whether at least one element in the array passes the test implemented by the provided function.
const array = [1, 2, 3, 4, 5];

// checks whether an element is even
const even = (element) => element % 2 === 0;

console.log(array.some(even));
// expected output: true

// the sort method 
// method sorts the elements of an array in place and returns the reference to the same array, now sorted.
// the default sort sequence is in an ascending fashion 
// const months = ['March', 'Jan', 'Feb', 'Dec'];
// months.sort();
// console.log(months);
// // expected output: Array ["Dec", "Feb", "Jan", "March"]

// const array1 = [1, 30, 4, 21, 100000];
// array1.sort();
// console.log(array1);
// // expected output: Array [1, 100000, 21, 30, 4]


// The time and space complexity of the sort cannot be guaranteed as it depends on the implementation.

 // ------------------SUMMARY------------------------------
// The following methods mutate the original array:

// copyWithin()
// fill()
// pop()
// push()
// reverse()
// shift()
// sort()
// splice()
// unshift()

// The following methods create new arrays with @@species:

// concat()
// filter()
// flat()
// flatMap()
// map()
// slice()
// splice() (to construct the array of removed elements that's returned)

// These methods treat empty slots as if they are undefined:

// entries() : method returns a new Array Iterator object that contains
//  the key/value pairs for each index in the array.

const arrayentries = ['a', 'b', 'c'];

const iterator1 = arrayentries.entries();

console.log(iterator1.next().value);
// expected output: Array [0, "a"]

console.log(iterator1.next().value);
// expected output: Array [1, "b"]


// fill() :  method changes all elements in an array to a static value,
// from a start index (default 0) to an end index (default array.length). It returns the modified array.

// find() :returns the first element in the provided array that satisfies the provided testing function.  
// findIndex() : finds item in specified index 
// findLast() :  method iterates the array in reverse order and 
// returns the value of the first element that satisfies the provided testing function.

const arrayfindlast = [5, 12, 50, 130, 44];

const found = arrayfindlast.findLast((element) => element > 45);

console.log(found);
// expected output: 130


// findLastIndex() : findLastIndex() method iterates the array in reverse order and 
// returns the index of the first element that satisfies the provided testing function. 

const arrayFindLastIndex = [5, 12, 50, 130, 44];

const isLargeNumber = (element) => element > 45;

console.log(arrayFindLastIndex.findLastIndex(isLargeNumber));
// expected output: 3  (of element with value: 130)

// group() : groups the elements of the calling array according to the string values returned
// by a provided testing function. 

// groupToMap() : method groups the elements of the calling array using the values
// returned by a provided testing function

// includes() : checks for something in arrays 

// join() : creates and returns a new string by concatenating all of the elements in an array
const elements = ['Fire', 'Air', 'Water'];

console.log(elements.join());
// expected output: "Fire,Air,Water"

console.log(elements.join(''));
// expected output: "FireAirWater"

console.log(elements.join('-'));

// keys()  : method returns a new Array Iterator object that contains the keys for each index in the array.
const arrayKeys = ['a', 'b', 'c'];
const iterator = arrayKeys.keys();

for (const key of iterator) {
  console.log(key);
}

// expected output: 0
// expected output: 1
// expected output: 2

// toLocaleString() : method returns a string representing the elements of the array. 
const arrayLocale = [1, 'a', new Date('21 Dec 1997 14:12:00 UTC')];
const localeString = arrayLocale.toLocaleString('en', { timeZone: 'UTC' });

console.log(localeString);

// values() : method returns a new array iterator object that iterates the value of each index in the array.
const arrayValues = ['a', 'b', 'c'];
const iteratorValues = array1.values();

for (const arrayValues of iteratorValues) {
  console.log(arrayValues);
}

// more on arrays here 
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#check_if_an_array_contains_a_certain_item