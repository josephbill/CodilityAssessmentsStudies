const data = {
    code: 42,
    items: [
        {
        id:1, 
        name:'foo'
    },
    {
        id:2,
        name:'bar'
    },

]
}
// object : data 



console.log(data.code)
console.log(data.items)

// getting the properties 
for(const x in data){
    // x contains name of each property 
    // data[x] refers to the value of each property

}

// As alternative to for...in with hasOwnProperty, 
// you can use Object.keys [MDN] to get an array of property names:

// Object.keys(data).forEach(function(prop) {
//   // `prop` is the property name
//   // `data[prop]` is the property value
// });

let itemArray = data.items;
// to iterate 
// use a for loop 
for (let i = 0; i < itemArray.length; i++){
    console.log(itemArray[i]);
    // break; continue; 
}

itemArray.forEach(item => {

})

itemArray.forEach(function(value, index, array){
    // for each element in itemArray ;callback gets executed 
    // `value`` : element itself: equivalent to [`array[index]`]
    // `index` : index position element in the array
    // `arrray` : pointing to the array itself (data.items)
})

// depth and keys are unknown entites. 
// test the type of value and act accordingly 
// typeof method 
// push to an array 
function toArray(obj) {
    const result = []; //empty array to carry my output 
    //loop through the object 
    for(const prop in obj) {
        const value  = obj[prop]; //code to point to the value 
        // each iteration test what the value is 
        //base case : to stop recurssion process
        if(typeof value === 'object'){
           result.push(toArray(value)) // recurssion gives our value for the object : unknown keys and entities 
        } else {
           result.push(value); // single values 
        }

    }
    return result;  // return the array 
} 

console.log(toArray(data))