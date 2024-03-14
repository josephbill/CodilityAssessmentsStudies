class Article: 
    def __init__(self, author, magazine , title) -> None:
        if not isinstance(title,str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a str and btw 5 and 50 characters")
        
        if not isinstance(author, Author):
            raise ValueError("author must be of the Author instance")
        
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be of the Magazine instance")
        
        self._author = author
        self._magazine = magazine
        self._title = title


    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
      if not isinstance(value, Author):
            raise ValueError("author must be of the Author instance")
      self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
      if not isinstance(value, Magazine):
            raise ValueError("magazine must be of the Magazine instance")
      self._magazine = value
    


from author import Author 
from magazine import Magazine

        
        
        
    