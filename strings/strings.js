//to create a string 
const a  = "new string"
const b = new String("A string object")
//character access 
// access a single character in the string using the charAt() method. 
'cat'.charAt(1) //will return "a"
//or 
'cat'[1] 
//compare strings using logical operators 
// < , > , = 
// operators such as === and == compare strings using a case-sensitive approach 
// to get rid of such an approach the common method is to convert the strings to be case insensitive 
function areEqualCaseInsensitive(str1, str2) {
    return str1.toUpperCase() === str2.toUpperCase();
  }

//popular JS methods on strings include 

// String length : captures lenght of string 
// String slice() : used to extract part of a string and returns a new index, takes two parameters , start index and end index 
// String substring() : same as slice
// String substr() : same as slice but the two parameters are the start positoon and the length of the string
// String replace() : returns a new string , used to replace part of string , takes in two parameters , new word and word to be replaced
// String replaceAll() : method allows you to specify a regular expression instead of a string to be replaced.
// String toUpperCase()
// String toLowerCase()
// String concat() : used to join string 
// String trim() : method removes whitespace from both sides of a string:
// String trimStart() : removes whitespace from start position
// String trimEnd() : removes whitespace from end position
// String padStart() : method pads a string with another string:
// String padEnd() : method pads a string with another string:
// String charAt() : gets character in string at a specified index position i.e. transforms strings into new arrays
// String charCodeAt() : method returns the unicode of the character at a specified index in a string:
// The method returns a UTF-16 code (an integer between 0 and 65535).
// String split() : converts string to an ARRAY. 


