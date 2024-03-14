from author import Author
from article import Article
from magazine import Magazine

# testing 
# author
try: 
  #create an author instance 
  author1 = Author("Joseph")
  print("Author namr" , author1.name)

  # test other methods 

except ValueError as e:
    print("error author isntance " , e)

# testing 
# magazine
try: 
  #create an author instance 
  magazine1 = Magazine("Tech Review", "Technology")
  magazine2 = Magazine("Science Today", "Science")
  print("Magazine name: " , magazine1.name)
  print("Magazine category: " , magazine1.category)
  # test other methods 

except ValueError as e:
    print("error author isntance " , e)

# testing 
# article
try: 
  #create an author instance 
  author2 = Author("Mary")
  article1 = Article(author1, magazine1, "The future of AI")
  article2 = Article(author1, magazine1, "The Daily Tech")
  article3 = Article(author2,magazine2, "Germination Process")
  print("Atricle name: " , article1.title)
  print("Atricle author: " , article1.author.name)
  print("Atricle magazine: " , article1.magazine.name)
  # test other methods 

except ValueError as e:
    print("error author instance " , e)

# Testing additional methods and relationships
try: 
  article4 = author1.add_articles(magazine1, "AI Trends")
  article5 = author1.add_articles(magazine2, "Science Breakthroughs")
  article6 = author2.add_articles(magazine1, "ML applications")

  print("\n Author's articles ")
  for article in author1.articles():
    print("-" , article.title)

    # magazine authors 
    #  contributig authors 
except ValueError as e:
    print("error author isntance " , e)


# Testing top_publisher method
try: 
    top_magazine = Magazine.top_publisher()
    if top_magazine:
       print("\n Top Publisher: " , top_magazine.name)
    else: 
       print("\n Articles not sufficient,top publisher cannot be determined.")
except ValueError as e:
    print("error author isntance " , e)




