class Magazine:

    _all_magazines = []  #class attribute to store all magazine instances 

    def __init__(self, name , category) -> None:
        #check if name and category are strings and inclusive 2 and 16 chr 
        if not isinstance(name, str) or not isinstance(category, str) or len(name) < 2 or len(name) > 16 or len(category) == 0:
            raise ValueError("name should be str and btw 2 to 16 and category must be a non empty string")
        
        self._name = name
        self._category = category
        self._articles = []  # list to store my articles 
        Magazine._all_magazines.append(self) # instance to list all magazines 
        

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self,value):
        if not isinstance(value,str) or len(value) < 2 or len(value) > 16: 
            raise ValueError("name should be str and btw 2 to 16")
        
        self._name = value
        
    @property
    def category(self):
        return self._category


    @category.setter
    def category(self,value):
        if not isinstance(value,str) or len(value) == 0: 
            raise ValueError("category should not be an empty string")

        self._category = value

    # articles to return all aricles 
    # to add an article to my magazine 
    # articles_titles 
        
    def articles(self):
        return self._articles
    
    def add_article(self,author,title):
        article = Article(author,self,title)
        self._articles.append(article)
        return article
    
    # return list of article titles 
    def article_titles(self):
        if not self._articles:
            return None
        
        return [article.title for article in self._articles]
    
    # return contributors
    def contributors(self):
        # collect unique authors for articles 
        return list(set(article.author for article in self._articles if isinstance(article.author, Author)))
    
    # return a list of authors with more than 2 articcles 
    def contibuting_authors(self):
        # dictonary that will create keys 0> author  and keeps a count of the appearance of the author in 
        # my article list 
        author_counts = {}
        for article in self._articles:
            author = article.author 
            if author in author_counts:
                author_counts[author] += 1 
            else:
                author_counts[author] = 1

        #  filter authors with more than 2 articles 
        filtered_author = [author for author,count in author_counts.items() if count > 2]

        if not filtered_author:
            return None 
        
        return filtered_author
    
    # finding the magazine wih the most articles 
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None 
        
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))



from author import Author
from article import Article

    


    

