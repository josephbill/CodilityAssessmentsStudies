// functions 
// 1. Named Function 
function nameoffunction(){
    // logic
    return " return sth. "
}

// 2. functions with parameters 
function nameoffunctionwithparameters(a,b){
    const sum  = a + b
    return sum

}

// function arguements : information required by function with params.
let result = nameoffunctionwithparameters(7,9) 
console.log(result)
result = nameoffunctionwithparameters(10,15)
console.log(result)


// 3 Function expressions : when functions are reference with variables 
const functionName = function(a,b){
    return "from function expressions"
}

console.log(functionName())

// 4. arrow functions (this keyword) (execution context)
// they don't own their own 'this'

const arrowfunction = (n,m,o,p) => {
    // logic 
    const output = n + m.toString() + o + p 
    return output
}

console.log(arrowfunction("Joseph",10,"a","TM"))


let x = "joseph"
console.log(x.toUpperCase())