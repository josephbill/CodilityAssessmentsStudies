//pseudo 
// create an object e.g. doctorsWorkSheet where eachprop is a doctors id and the value is a set of ids of the hospital where they have worked at. 
// Why set ? the values basically the hospital ids for each doctor i.e. should be unique

function solution(A) {
    // Implement your solution here
    // creating an object to hold the doctors worksheet 
    let doctorsWorkSheet = {}

    //outer loop to loop through all hospital 
    for (let k = 0; k < A.length; k++){
        //loop through all days to check if doctor has worked in more than one hospital 
        // inner loop will work for each iteration to check if a doctor worked in that hospital that day 
        for (let l = 0; l < A[k].length; l++){
            // treat this as the doctor id " [A[k][l]]" indicates hospital and day as in loop structure
            // if this key i.e dr id already exists then the doctor is assigned to atleast one hospital
            if(doctorsWorkSheet[A[k][l]]){
                 //so add this hospital to the doctors worksheet 
                 // a dr works in multiple hospitals 
                 doctorsWorkSheet[A[k][l]].add(k)
              } else {
                  // add this doctor to our set 
                   // creating a new Set with the hosputal id and doctors id
                   doctorsWorkSheet[A[k][l]] = new Set([k])      
           }
        }
        
    }

    //check how many doctors have worked in more than one hospital 
    let multipleWorkPlaces = 0;
    //looping the doctorsworksheet object i.e use the ID of the doctor 
    //if dr has more than one assinged id then he is a hustler giving us prompt to increase our multipleWorkPlaces count by 1. 
    for (let dr in doctorsWorkSheet){
        if(doctorsWorkSheet[dr].size > 1){
            multipleWorkPlaces++
        }
    }
    //my function return. 
    return multipleWorkPlaces;
}


console.log(solution([[1,2,2],[3,1,4]])); // Outputs: 1
console.log(solution([[1,1,5,2,3],[4,5,6,4,3],[9,4,4,1,5]])); // Outputs: 4
console.log(solution([[4,3],[5,5],[6,2]])); // Outputs: 0


// question 
// There are N hospitals , numbered from 0 to N-1. You are Given a schedule of work in each of teh hospitals for the following M days.
//  The schedule is provided in the form of a two dimensional Array A containing N rows, each row representing the schedule of one hospital , and M columns , 
//  each column representing one day. Integer A[K][L] (for K within the range [0..N-1] and L within the range [0..M-1]) represents 
//  the ID of the doctor working at the hospital K on day L. Note that sometimes an individual doctor may work at more than one hospital even on the same day. 
//  Write a function in JS : function solution(A); that given a matrix A consisting of N rows and M columns representing the hospitals' schedules , 
//  find the number of doctors working at more than one hospital. Examples , 1. given A = [[1,2,2],[3,1,4]] the function should return 1. 
//  2. given A = [[1,1,5,2,3],[4,5,6,4,3],[9,4,4,1,5]] the function should return 4. 3. given A = [[4,3],[5,5],[6,2]] the function should return 0.
//   In the solution kindly add code comments explaining the use of each code section.Give the most efficient answer

