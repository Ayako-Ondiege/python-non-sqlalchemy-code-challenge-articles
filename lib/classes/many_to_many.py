class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of the type Magazine")
        self._magazine = value
        
class Author:
    def __init__(self, name):
        # if not isinstance(name, str) or len(name.strip()) == 0:
        #     raise Exception("Name must be an non-empty string")
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            return
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Name must be a non_empty string")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles ()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <=16):
            return
            # raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            return
            # raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        if not self.articles():
            return None
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None