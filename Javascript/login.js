// ### Q1
// WRITE A FUNCTION THAT CHECKS IF A USER IS ALLOWED TO LOG IN 
// a USER CAN LOGIN IF THEY ARE EITHER AN ADMIN (isAdmin) or 
// if a user is verified (isVerified) but only if they are not banned 

// abstraction 
//  user properties , is my user 
//  1. isAdmin 2. isVerified 3. isBanned

// decomposition 
// check if user is banned , 
// check if user is allowed based on their role isAdmin || isVerified 

// data modelling 
//  let isAdmin = false , let isVerified  = false , let isBanned = false 
// const user = {
//     isAdmin: false,
//     isVerified: true, 
//     isBanned : false
// }

// pattern recognition 
// Logical operators to check if user is verified and not banned , or isAdmin 

let isAdmin = false 
let isVerified = true
let isBanned = false 

function canLogin(){
    // if user is banned it does not matter if user is admin or verified 
    if(isBanned){
        console.log("The user is banned")
        return false;
    }

    // is user admin or is verified
    if(isAdmin || isVerified){
        console.log("The user is either an admin or verified")
        return true;
    }
    console.log("user is not registered in the system")
    return false; 
}

console.log(canLogin())

function quickLogin(){
    return !isBanned && (isVerified || isAdmin)
}

console.log(quickLogin())