### Meet 
1. Canva content coverage check and Methods
2. Assignment Overview 
   - Logical Operators / Conditional Statements activity 
3. Functions 
4. JS Objects 
5. JS Methods


### LOGICAL OPERATORS 
## WHAT ?
Operators that evaluate to true or false 
Conditions / Comparisons 
Perform logical operations on values 

## TYPES OF LOGICAL OPERATORS 
1. AND OPERATOR (&&) :: returns true if both conditions are met
2. NOT OPERATOR (!) :: returns false if the single operand can be converted to true  
3. OR OPERATOR (||) :: returns true if one condition is met 

Algorithm :: Step by step process to solve a problem 

5 Steps in writing logic 
1. Abstraction :: focusing on what matters 
2. Decomposition :: breaking down the problem into smaller sets
3. Data modelling :: representing data using a structure 
4. Pattern Recognition :: identify existing solutions to problems 
5. Algo. thinking :: develop a step by step solution 

### Q1
WRITE A FUNCTION THAT CHECKS IF A USER IS ALLOWED TO LOG IN 
a USER CAN LOGIN IF THEY ARE EITHER AN ADMIN (isAdmin) or if a user is verified (isVerified) but only if they are not banned 

### Q2
WRITE A FUNCTION THAT CHECKS IF A NUMBER IS IN A VALID RANGE. A NUMBER IS VALID IF ITS BETWEEN 10 AND 50 (INCLUSIVE) OR EQUAL TO 100. 


if () { 
  <!-- logic -->
} 

function namedfunction(){
    <!-- logic -->

}

<!-- a function with parameters -->

function canLogin(isAdmin,isVerified,isBanned){
    <!-- logic -->
}

canLogin(false,true,false) 
<!-- in the call : false , true , false are function arguements  -->


<!--  DATA TYPES  -->
What ? formats, or the type of data 

Categories ? Primitive data types and Non-Primitive data types 

## Primitive 
represents only a single value 

### Primitive data types 
1. String : sequence of characters : "Joseph"
2. Character : "J" J
3. Boolean : true or false 
4. Number / Integers / BigInt / float(double) : 0-100000000000 ,  0.1 , 1.1. 
5. symbol : unique , immutable identifiers :: "ASCIII" 
6. null : intential absence of any value  : null 
7. undefined : returned data type when a variable has been declared but not assigned any value, functions without return statements also return 

## Non primitive 
storage references to memory locations and can hold multiple values 

### types 
1. Array : ordered Collection of elements (indexing : positioning)
2. functions : block of reusable code that can be executed when invoked / called. 
3. Object : key and value pairs 

const user = {
  isAdmin : false, 
  isVerified : true,
}


Strings (special guest)
classes : blueprints for object creation (constructors , OOP)

a collection of values = array 

joseph , 12 , true , (a,b,c,d,e,f,g) , "0" , J 


### FUNCTIONS 
- blocks of reusable code that can be executed when invoked / called.
- the can be defined in various ways 
   1. accept parameters (information that a function will use to process logic)
   2. return values 
   3. perform actions without returning anything : i.e console.logs


### Objects 
1. Collections of keya nd values pair 
2. Standalone entities that store data and functionality together 
3. Every JS is an object 

<!-- syntax of an object  -->
1. Creation via Object Literal 
const variablename = {
  key: value
}

keys are strings 
values can be of any data type

<!--school system app -> users ->  user object  -->

const user = {
  name : "Joseph Mbugua",
  role : "TM",
  phonenumber : 0798501343,
  password : "xxxxxx",
  feeBalance : false
  greet: function () {
    return `Good morning ${this.name}`
  }
}