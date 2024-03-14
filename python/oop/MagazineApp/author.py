class Author:
    def __init__(self, name) -> None:
        # check if the name is a valid string / must of type of str , > 0 characters
        # validation 
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name should be a string and not empty")
        self._name = name
        self._articles = []

    # getter for name 
    @property
    def name(self):
        return self._name
    
    #returning list of all articles belonging to the author 
    def articles(self):
        return self._articles
    
    # creating a new article instance and associating it to my author
    def add_articles(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article) # ensured that my list always returns instances of the article class 
        return article

    # return a unique list of strings that belong to the author article 
    def topic_areas(self):
        if not self._articles:
            return None
        
        return list(set(article.magazine.category for article in self._articles))
    
    # return a unique list of magazines which my author has contributed to 
    def magazines(self):
        #collect unique magazines from my articles lists 
        return list(set( article.magazine for article in self._articles if isinstance(article.magazine , Magazine)))
 

from article import Article
from magazine import Magazine