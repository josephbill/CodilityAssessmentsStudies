// Write a function that merges two strings together. It does so by merging the end of the first string with the start of the second string together when they are an exact match.

// "abcde" + "cdefgh" => "abcdefgh"

// "abaab" + "aabab" => "abaabab"

// "abc" + "def" => "abcdef"

// "abc" + "abc" => "abc"

// NOTE: The algorithm should always use the longest possible overlap.

// "abaabaab" + "aabaabab" would be "abaabaabab" and not "abaabaabaabab"


// 1. 

// In the context of the given problem, an overlap refers to the number of characters at the end of the first string 
// that match the beginning of the second string.

// For example, given the strings "abcde" and "cdefgh", the overlap is "cde" (the 3 characters at the end of "abcde" 
// that match the 3 characters at the start of "cdefgh").

// The merge_strings() function uses the overlap to determine how much of the second string should be appended to the first 
// string in order to create the merged string. It ensures that the overlapping part is only included once in the merged string,
//  and the algorithm always tries to use the longest possible overlap.

// 2.
// suppose you have two strings s1 and s2. You want to merge them into a single string such that the end of 
// s1 matches the start of s2.

// Here are some examples to illustrate:

// "abcde" and "cdefgh" can be merged into "abcdefgh". Notice how "cde" is common to both strings, 
// so we only include it once in the merged string.

// "abaab" and "aabab" can be merged into "abaabab". Notice how "aab" is common to both strings, 
// but "aba" is also common. However, we need to use the longest possible overlap, which is "aab", 
// to avoid duplicating characters in the merged string.

// "abc" and "def" can be merged into "abcdef". There is no overlap between these two strings, so we just concatenate them.

// "abc" and "abc" can be merged into "abc". The two strings are identical, so we just return one of them.

// In general, the function should use the longest possible overlap between s1 and s2 to create the merged string, 
// to avoid duplicating any characters in the merged string.


function mergeStrings(s1, s2) {
    let overlap = 0;
    for (let i = 1; i <= Math.min(s1.length, s2.length); i++) {
      if (s1.slice(-i) === s2.slice(0, i)) {
        overlap = i;
      }
    }
    return s1 + s2.slice(overlap);
  }

  
  console.log(mergeStrings("abaabaab", "aabaabab"));  // output: "abaabaabab"


