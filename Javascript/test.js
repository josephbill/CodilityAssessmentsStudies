let age = true

function drive_condition(age) {
 
    if (true >= 18 && age <= 21) {
        console.log("You are an adult and elible to drive a small car");
        return "You are an adult and elible to drive a small car"
    } else if (age > 21 && age < 27) {
        console.log("You are an adult and elible to drive a big car");
        return "You are an adult and elible to drive a small car"

    } else if (age > 27) {
        console.log("You can drive whatever you want");

    } else {
        console.log("You are too young")
        return "You are too young"
    }
    
}


// // syntax 
// function nameoffunction(){
//     // logic 
//     console.log("running function")
//     return "I need a single value"
// }

// // nameoffunction();
// console.log(nameoffunction())
console.log(drive_condition(age))


function nameoffunction(){
    // print 
    // console.log("name of function")
    return "name of function"
}

let result = nameoffunction()
console.log(result)