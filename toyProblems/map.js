// Remember, all submissions are being checked for plagiarism.
// Your recruiter will be informed in case suspicious activity is detected.

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 14)
    //getting array length 
    let lengthArray = A.length;
    //storing sum of digits in a map = key
    //max no having sum of digits = value
    let myMap = new Map();
    let negativeOutput= -1;
    let pair_one = 0;
    let pair_two = 0;
    for(let v=0; v < lengthArray; v++){
        //storing current sum in temporary variable 
        let temporary = sumOfDigits(A[v]);
            if (!myMap.has(temporary)) {
                   myMap.set(temporary, 0);
               }
               if (myMap.get(temporary) != 0) {
                   if (A[v] + myMap.get(temporary) > negativeOutput) {
                       pair_one = A[v];
                       pair_two = myMap.get(temporary);
                       negativeOutput = pair_one + pair_two;
                   }
               }
 
               // Changing value in map as per iteration
               myMap.set(temporary, Math.max(A[v], myMap.get(temporary)));

    }
    return pair_one + pair_two
}

    // Function to find sum of digits
       function sumOfDigits (intdata) {
           let sum = 0;
           while (intdata) {
               sum += (intdata % 10);
               intdata = Math.floor(intdata / 10);
           }
           return sum;
       }




