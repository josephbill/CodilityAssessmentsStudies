// nested objects 
// an object with a collection objects 
// 1. validate the input passed to the function 
// 2. iterate the object to match desired case
const toyCompany = {
    // 1st level : 1st object 
    redTeam: {
         production: {
              'redprodManager' : 'Karis',
              'redworkerOne' : 'Omondi',
              'redworkerTwo' : 'Mwende'
         },
         sales: {
              'redSalesManager' : 'Kamau',
              'redSalesOne' : 'kibet',
              'redSalesTwo' : 'Matoh'
         }
    },
    blueTeam: {
         production: {
            'bprodManager' : 'blueKaris',
            'bworkerOne' : 'blueOmondi',
            'bworkerTwo' : 'blueMwende'
         },
         sales: {
            'bSalesManager' : 'bKamau',
            'bSalesOne' : 'bkibet',
            'bSalesTwo' : 'bMatoh'
         }
    }
}

// get the work title of the given employee

// 1. get input of the name employee 
function findEmployee(name){
    console.log(name)
    let result = ''
    // 1st level loop : to get red and blue team objects 
    // for .. in 
    for(let team in toyCompany){
        console.log("First level iteration " + team); // expected output // redTeam , blueTeam keys. 
        //value objName[key]
        //team saves both items 

        // access the team Objects (red and blue)
        let teamObject = toyCompany[team];
        // for .. in to go into second level 
        for(let departments in teamObject ){
          console.log("Second Level iterations " + departments); //expected output // production and sales 
          //iterating through third level / department object. 
          let titleObject = teamObject[departments]
          for(let jobTitle in titleObject ){
            console.log("The job titles are " + jobTitle)  //
            console.log(titleObject[jobTitle])
            // searchin for name 
            if(titleObject[jobTitle]  === name){
                console.log(name + ' job title is ' + jobTitle)
                result = name + ' job title is ' + jobTitle
            }
          }
               
        }
    }

    return result
} 


//maiden call to function 
console.log(findEmployee('bMatoh'));