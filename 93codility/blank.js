// You are given a list of names of new employees in a company. 
// You need to generate a company email address for them. The name of each person consists of two or three parts  : a first name , an optional middle name and a last name ,
//  separated by spaces. Each part can include only english letters (but the last name may additionally contain hyphens) The name of the company also consists only of english letters . 
//  Each address must use the format "FirstMiddleLast@Company.com" where 1. First is the initial of the first name,
//   2. Middle is the intial of the middle name (but only if the person has a middle name) ,
//    3. last is the last name, truncated to at most 8 initial letters 
//    4. Company is the company name.  - 
//     The address should be in lower case and should not contain hyphens. Note that hyphens should be removed before truncating the last name. 
//     Additionally, if more than one person would have the same email address , differentiate their addresses by adding subsequent 
//     integers (starting from the second address and number 2) before the @ sign . FOr example, if there are three people who would have the address "jd@company.com" , 
//     they should be assigned "jd@company.com", "jd2@company.com", "jd3@company.com" respectively. Help me with a JS function : 
//     function solution(S, C) ; that given a string S containing a list of names separated by the characters ", " (a comma followed by a space)
//      and a string C specifying the name of the company, returns a string containing the list of email addresses separated by characters ", " in the same order as they were input. 
//      Each entry on the list should be of the form "Name <Email>" 
//      e.g. given C = "Example" and a String S as follows "John Doe, James Doe,  Peter Parker, Mary Jane Watson-Parker, John Elvis Doe"
//       returns "John Doe <jdoe@example.com>, James Doe <jdoe2@example.com>, Peter Parker <pparker@example.com>, Mary Jane Watson-Parker <mjwatsonpa@example.com>, John Elvis Doe <jedoe@example.com>"
//       . Assume , the length of the String S is within the range [3..1,000] ,the length of the String S is within the range [1..100] , 
//       String S consists of only letters (a-z and /or A-Z), spaces, hyphens and commas,
//        string S contains valid names : no name appears more than once and string C is made only of letters (a-z and /or A-Z). Give best solution


// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S, C) {
    // Implement your solution here
    // first splitting the input names and company 
    const employee_names = S.split(', ');
    const employee_company = C.toLowerCase();
    //object to store my email creations
    // also use this to keep track of the frequency of the email initial 
    const emailBook = {};
    
    // selecting each name 
    const emailsCreations = employee_names.map(name => {
        // i need to split the names in the three parts 
        let nameparts = name.split(' ');
        //rules specify that i need to truncate and assess the input to remove hyphens , and blanks 
        // also convert to lower cases 
        // taking the first character from the first part of the name, converting it to lowercase, and storing it
        const first = nameparts[0].charAt(0).toLowerCase();
        // taking the last part of the name, removing any hyphens, taking at most the first eight characters, converting it to lowercase, and storing it
        const last = nameparts[nameparts.length - 1].replace('-', '').slice(0, 8).toLowerCase();
                // hecking whether there are three parts to the name
        // if not replacing middle for them with an empty string
        const middle = nameparts.length === 3 ? nameparts[1].charAt(0).toLowerCase() : '';
        // my emails
        let emailIntial = first + middle + last;

        // Check for potential duplicates
        // if so append name with next character 
        if(emailBook[emailIntial]) {
            // keeping track of intials occurances 
            emailBook[emailIntial]++;
            //append the current count to the intial to make it unique
            emailIntial = emailIntial + emailBook[emailIntial];
        } else {
            //if new then start count from 1. 
            emailBook[emailIntial] = 1;
        }
          // constructing my full address 
        const email = `${emailIntial}@${employee_company}.com`;
        //my string return 
        return `${name} <${email}>`;
    });

    return emailsCreations.join(', ');
}


// usage
const S = "John Doe, James Doe, Jane Doe, Peter Parker, Mary Jane Watson-Parker, John Elvis Doe";
const C = "Example";
console.log(solution(S, C));
