// There is a road consisting of N segments (numbered from 0 to N-1) described by an array R of integers. The K-th segment is described by an integer R[K]. If the segment is smooth (there is no pothole in it), then R[K] = 0; otherwise it contains a pothole of depth R[K]. Consecutive potholes join together and create a larger group of potholes. The pothole indicator is the number of consecutive single potholes that have joined into a pothole group, multipled by the depth of the deepest pothole among them. For example, the indicator for a group of three consecutive joined potholes of size [1,4,1] is 3 * 4 = 12. What is the largest pothole indicator on the entire road ? Write a Js function . function solution(R); that , given an array R of N integers , returns the largest pothole indicator on the road. 1. Given R = [0,2,1,1,0,4,1] the function should return 8. 2. Given R = [1,4,1,0,5,2,3,0,8] the function should return 15.  3. Given R = [9,8,7,0,0,0,2,3,6,4] the function should return 27   4. Given R = [0,0,0] function should return 0 .  assume N is an integer within the range [1..100,000] , each element of array R is an integer within the range [0..9]

//pseudo
//i thinks idea is to keep track of the depth of the deepest pothole ; maxphIndicator
//also the length of the current group (phGroupLength)
// everytime i get a pothole update the depth if its deeper than maxphIndicator 
// also increment the length of the group 
// on encounter of a smooth segment i.e R[i] == 0 
// calc the current ph indicator (phGroupLength * maxphIndicator) 
// update the maxphIndicator if the present is deeper than the depth. 

function solution(R) {
    let maxphIndicator = 0; //store and update the maximum pothole indicator found thus far
    let phGroupLength = 0; //update and store the pothole group length
    let maxphDepth = 0; //store depth of the deepest pothole

    // looping each road segment 
    for (let i = 0; i < R.length; i++) {
        // if segment is smooth (then we have reached the end of the group of potholes)
        if (R[i] === 0) { 
                    // Calculate the pothole indicator for the current group (length * depth)
            let cphIndicator = phGroupLength * maxphDepth;
            if (cphIndicator > maxphIndicator) {
                     // If this pothole indicator is larger than the maximum found so far, update the maximum
                maxphIndicator = cphIndicator;
            }
            // Reset the group length and depth for the next group of potholes
            phGroupLength = 0;
            maxphDepth = 0;
        } else { // if its a pothole segment
            // Increment the length of the current group of potholes
            phGroupLength++;
            // If the depth of this pothole is greater than the maximum depth found so far in this group, update the maximum
            if (R[i] > maxphDepth) {
                maxphDepth = R[i];
            }
        }
    }
    // wait 
    // the loop updates the maxphIndicator value when it encounters a smooth road segment i.e R[i] === 0
    // so what if the array ends with a pothole i.e no smooth segment to signify the end of a group. 
    // i'll calculate the for such so that the maxphIndicator is arrived at 

    // Check the last group of potholes
    let lphIndicator = phGroupLength * maxphDepth;
    if (lphIndicator > maxphIndicator) {
        maxphIndicator = lphIndicator;
    }

    // my return. 
    return maxphIndicator;
}


console.log(solution([0,2,1,1,0,4,1]))  //8
console.log(solution([1,4,1,0,5,2,3,0,8])) //15
console.log(solution([9,8,7,0,0,0,2,3,6,4])) //27
console.log(solution([0,0,0])) //0

// There is a road consisting of N segments (numbered from 0 to N-1) described by an array R of integers. The K-th segment is described by an integer R[K]. 
// If the segment is smooth (there is no pothole in it), then R[K] = 0; otherwise it contains a pothole of depth R[K]. 
// Consecutive potholes join together and create a larger group of potholes. 
// The pothole indicator is the number of consecutive single potholes that have joined into a pothole group, multipled by the depth of the deepest pothole among them. 
// For example, the indicator for a group of three consecutive joined potholes of size [1,4,1] is 3 * 4 = 12. What is the largest pothole indicator on the entire road ?
//  Write a Js function . function solution(R); that , given an array R of N integers , returns the largest pothole indicator on the road. 
//  1. Given R = [0,2,1,1,0,4,1] the function should return 8. 2. Given R = [1,4,1,0,5,2,3,0,8] the function should return 15.  3. Given R = [9,8,7,0,0,0,2,3,6,4]
//   the function should return 27   4. Given R = [0,0,0] function should return 0 .  assume N is an integer within the range [1..100,000] ,
//    each element of array R is an integer within the range [0..9]