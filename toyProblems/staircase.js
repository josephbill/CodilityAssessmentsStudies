// n is an integer denoting the size of the staircase
// print a staircase of size n using # symbols and spaces and make it right-aligned

//pseudo-code 
//1. input 2
//2. output  s#
//           ##
// we need to account for spaces , also account for joining the spaces with our #
// three loops 
// outer loop takes care of the row iteration 
// inner loop for the spaces 
// nested inner loops for joining the hashtag. 
// space should start out at n -1 
// and should remain greater than or equal to rows 
// because the number of spaces decreases as rows increases
// decrease space bc the number of spaces decreases as rows increases

function staircase(n){
     //empty variable to store my prints 
     let stairHash = ''
    // outer for loop to keep track of the overall number of rows (n)
    for(let i = 0; i < n; i++){
          // transversal 
               // s should start out at n-1 
            // s should be greater than or equal to row because the number of spaces decreases as row increases
            // use decriment space bc the number of spaces decreases as row increases
        for (let s = n - 1; s >= i; s--) {
            stairHash += ' '
        }
        
        // inner for loop to keep track of the #s on each line
            // h should start at one because the first line will always have one #
            // h should be less than or equal to the row that we are on since h will approach and eventually equal n
            // h increases since we increment h to equal row which will eventually equal n
        for (let h = 1; h <= i; h++) {
            stairHash += '#'
        }
        // new line //prints out row. 
        stairHash += "\n"
          
     }
     console.log(stairHash)
}

staircase(5);

// using .repeat 
// String object method that returns a string that has been repeated a desired number of times
function staircaseWithRepeat(n){
// here we use just one for loop where i tracks the number of rows
  // the number of rows (i) should be less than or equal to n
  for (let i = 1; i <= n; i++) {
    // print out a " " n-i times and append a # i times
    // console log adds a new line by default
    
      console.log(" ".repeat(n-i) + "#".repeat(i))
  }   
}


staircaseWithRepeat(5);