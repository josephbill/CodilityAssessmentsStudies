function isPalindrome(text){
    // Clean the input string by converting to lowercase and removing non-alphanumeric characters
    const cleanedStr = text.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
    
    // define base case for the recursive call 
    if(cleanedStr.length <= 1){
        return true;
    }

    //check if last character and first character of the cleaned 
    // string are not equal 
    if(cleanedStr[0] !== cleanedStr[cleanedStr.length - 1]){
        return false; 
    }
    //recursion : recursively call the function with string 
    // exculding the first and last characters.
    //slice : 1. creates a new string by extracting a portion 
    //of the original string 2. Below 1 stands for the chr
    // to extract , -1 represent the last index / character,
    //this in effect removes the first character and last character from the string
    return isPalindrome(cleanedStr.slice(1, -1));
}

// Example usage:
console.log(isPalindrome("mom")); // true
console.log(isPalindrome("A man, a plan, a canal, Panama!")); // true
console.log(isPalindrome("hello world")); // false
console.log(isPalindrome("clarc")); // false


