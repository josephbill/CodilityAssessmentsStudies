// 1. create the library object 
const library = {
    name: "",
    books: [] // array to hold the library's books 
}
// 2. CRUD operations 
// function to add books to the lib. 
function addBooks(title,genre,publication_year,author){
//   create an object to store reference to a single book 
    //  create a book object using parameters passed to this function 
    const newBook = {
        bookname: title,
        publication: publication_year,
        author: author,
        genre: genre
    }
    // arrays : I want to add a book object to my books array in the library object
    // to add elements to an array we use the method .push() 
    // how to access keys in an object , we use the dot notation
    library.books.push(newBook)
    // check if new book is added
    console.log(`Book ${newBook.bookname} has been added`)

}

// function displayBooks(){
//     // for each loop to iterate over the books array 
//     const results = library.books.forEach((book) => {
//            console.log()
//            return `Title: ${book.bookname} Author: ${book.author}`
//     })

//     return results
// }


addBooks("Another Book","Poetry","2025","Someone Poet")
addBooks("More Book","Poetry","2025","Someone Poet")
addBooks("Another One","Poetry","2025","Someone Poet")

// Access the books directly
console.log(library.books)
// books = [
//     {

//     },
//     {

//     }
// ]

//  : string interpoleters 
// ''  : single quotes
// " " : double quotes 
// "joseph mbugua"
// let x = "joseph"
// let greet = `Welcome to my app ${x}`

// `` = directly below the esc key , before the key `1`

// 1. creation of an object 
// 2. accessing elements in an object 
// 3. different format of an object 
// 4. iterating objects 
 

