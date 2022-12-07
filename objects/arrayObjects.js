let cars = [
    {
       color: "purple",
       type: "minivan",
       registration: new Date('2022-12-7'),
       capacity: 7
    },
    {
        color: "red",
        type: "hatchback",
        registration: new Date('2022-12-7'),
        capacity: 5
    },
    {
        color: "black",
        type: "sedan",
        registration: new Date('2022-12-7'),
        capacity: 10
    },
    {
        color: "red",
        type: "van",
        registration: new Date('2022-12-7'),
        capacity: 5
    }
]

// array objects : do not always stay the same 
// arrayName.unshift(obj) ;; //insert a new element to the start 
// arrayName.push(obj) ;; inserts a new element to the end position
// arrayName.splice(obj)
// arrayName.splice(
//     index where to start, //required , position to add or remove element 
//     howmany, //optional // number of items you want removed
//     item1, ... , //optional
// )

let fruits = ['Banana','Orange','Apple','Watermelon'];
// add at postion 3 , add two elements 
// lemons ,mango
let x = fruits.splice(2, 1, "Lemon","Mango")
console.log(x);

//removing elements 
// remove 2 items from positon 3  -> index 2
let y = fruits.splice(2,2)
console.log(y);


//inbuilt methods '
//Array.find()
// to find the object(s) where the color of the car is red 
// find needs a condition to base its search on. 
// first element that matches the condition then it returns that element
// if no element -> return undefined. 
let carRed  = cars.find(car => car.color === "red" && car.type === "hatchback" );
console.log(carRed);

// to get multiple results and not just the first matching element 
let allRed = cars.filter(car => car.color === "red");
console.log("From filter " + JSON.stringify(allRed));

//transform objects : 
// arrayName.map()
let sizes  = cars.map(car => {
    if(car.capacity <= 3){
        return "small"
    }
    if(car.capacity <= 5){
        return "medium"
    }
    return "large";
})

console.log("Sizes " +  sizes)
// adding props. 
// using the above array of objects  ( cars ) : to create/transform the objects to add 
// a new value which will be size 
// expected output.
// {
//     color: "black",
//     type: "sedan",
//     registration: new Date('2022-12-7'),
//     capacity: 10,
//     size : "large"
// },

// // arrayName.forEach(element => {

// })

// sorting of an array : arrangement of elements in the ARRAY
// to sort an array of objects : base it on a value that each property has. 
// ArrayName.sort()
// always provide a function that will define the sorting mechanism
// example : sort the cars in descending order based on capacity 
let sortedCars = cars.sort((c1,c2) => (c1.capacity < c2.capacity) ? 1 : (c1.capacity > c2.capacity) ? -1 : 0);
console.log(sortedCars)

// we can check if an array fulfills a certain condition 
// Array.every , Array.some 
// expected output of this two methods is // true or false 

cars.some(car => car.color === "red" && car.type === "Plane")
//false 
cars.some(car => car.color === "red")
//true 

// for (let i = 0 ; i < cars.length; i++) {
    //execution on each obj by pointing to i
    //purpose of the loop
// }