'''
Object relationship refers to how objects interact and relate to each other in a program. 
* Representation 
- representation is done using classes and their instances 
- From the chosen representation then the types of relationships are formed : 


one to many relationship 
idea : simple school system where we have classes for students and courses.  (one student can belong to many courses)

the many clause of the program should be stored in a data structure (proper list.)
'''
class Student:
    def __init__(self, name) -> None:
        self.name = name 
        self.courses = []

    def enroll(self,course):
        self.courses.append(course)
        course.students.append(self)


class Course: 
    def __init__(self, name) -> None:
        self.name = name
        self.students = []

    def add_student(self,student):
        self.students.append(student)
        student.courses.append(self)


# create the students 
student1 = Student("Alice")
student2 = Student("Kamau")
# create the courses 
course1 = Course("Math")
course2 = Course("Science")
#establishing the relationship 
student1.enroll(course1)
course2.add_student(student2)
student1.enroll(course2)
# printing the relationships 
# from student 
for student in [student1, student2]:
    print(f"{student.name} is enrolled in the following courses")
    for course in student.courses:
        print(f"- {course.name}")

# from the courses 
for course in [course1, course2]:
    print(f"{course.name} has the following students enrolled")
    for student in course.students:
        print(f"- {student.name}")
        



'''
Many to many relationships 
-always involves a third table/model/class (Contract class , join class , association class)



Register the skillsets of my mechanics in my garage 
two entities 
- Mechanic 
- Skill 

Mechanic 
id | name  |  staffno  
 1    Joseph   1                     
 2    Mary     2           

Skill 
id |  name  |  skillid  
1     body works   1        
2     engine       2        

mechanic_skils
id |  mechid  | skillid 
1     1           1
2     1           2 
3     2           2  


BOOKS AND AUTHORS 
 - Books : create my books  : one book can hold many authors 
 - Author : create my authors : author can have many books 
 - Authorship  : third entity to create the relationship between the two entities above. 
 '''
class Book: 
    book_count = 0

    def __init__(self, title) -> None:
        self.title = title
        self.authors = []  #list to hold book authors 
        Book.book_count +=1  # keep count 

    def add_author(self,author):
        self.authors.append(author)
        author.books.append(self)


class Author: 
    author_count = 0

    def __init__(self, name) -> None:
        self.name = name
        self.books = [] # list to hold author books
        Author.author_count +=1 


    def write_book(self, book):
        self.books.append(book)
        book.authors.append(self)


class Authorship: 
    def __init__(self, book , author) -> None:
        self.book = book 
        self.author = author

    def print_relationship(self):
        print(f"Authorship between '{self.author.name}' and '{self.book.title}'")


# create some instances
book1  = Book("Python Programming")
book2 = Book("Data Science Essentials")
author1 = Author("Joseph Mbugua")
author2 = Author("Mary")

# establish the authorship 
authorship1 = Authorship(book1, author1)
authorship2 = Authorship(book1, author2)
authorship3 = Authorship(book2, author2)

# # print author for each book 

# for book in [book1, book2]:
#     print(f"{book.title} has the following author(s)")
#     for authorship in book.authors:
#         print(f"- {authorship.author.name}")

# # from the author 
# for author in [author1, author2]:
#     print(f"{author.name} has written the following books")
#     for authorship in author.books:
#         print(f"- {authorship.book.title}")

authorship1.print_relationship()
authorship2.print_relationship()
authorship3.print_relationship()
        

