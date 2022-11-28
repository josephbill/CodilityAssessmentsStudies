// Write a function that takes an array of numbers as input. It should output an array of those same numbers sorted from lowest to highest.
// input [5,3,1,4,2]
// output [1,2,3,4,5]

//pseudocode
//1. Loop through array members regardless of length 
//2. Compare the item in current iteration with the number infront of it. 
//3. If the current number in iteration is greater than the number infront make them swap positions.
//4. Biggest number in array will be swapped to the last position

function bubblesort(arrayN){
    let length = arrayN.length;
    for(let index = 0; index < length; index++){
        //capture next value 
        for(let pos=0; pos < length; pos++){
            if(arrayN[pos] < arrayN[pos + 1]){
                //swap 
                //using a temp. variable. 
                //smaller number here is not the smallest number 
                //just including it in my variable to swap at the end and equal it to the current position.
                const smallerNumber = arrayN[pos + 1];
                arrayN[pos + 1] = arrayN[pos];
                arrayN[pos] = smallerNumber;   
                     }
        }
    }
    return arrayN;

}

console.log(bubblesort([5,3,1,4,2]))
