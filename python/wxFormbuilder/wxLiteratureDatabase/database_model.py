class DatabaseModel():
    """
    Model used for communication with the database

    Attributes:
        pb: Pubsub object used for logging

    Methods: 
        active_log: Function declorator for handeling automatic logging of all datbase interactions
        searchBooks: Search up a book in the database
        getBooks: Get books from given input
        getArticle: Get articles from given input
        addBook: Executes sql insert statement and commits it to book database
        addArticle: Executes sql insert statement and commits it to article database
        deleteBook: Deletes a book from the database
        deleteArticle: Delete an article from the database
    """

    def __init__(self, pubsub):
        self.pb = pubsub

    def active_log(func):
        """ Logger declorator """
        def wrapper(self, *args, **kwargs):
            self.pb.sendMessage("MyMainFrame", message = f"{func.__name__} - {args} - {func.__doc__}")
            return func(self, *args, **kwargs)
        return wrapper

    @active_log
    def searchBooks(self, con, args):
        """ Search up a book in the database """
        sql = """SELECT title, surname, firstname, publisher, year, genre FROM books WHERE title LIKE ? AND 
                surname LIKE ? AND firstname LIKE ? AND publisher LIKE ? AND year LIKE ? AND genre LIKE ? """
        cur = con.execute(sql, args)
        book_data = cur.fetchall()
        return book_data

    @active_log
    def getBooks(self, con):
        """ Get books from given input """
        sql = """SELECT id, title, surname, firstname, publisher, year, genre FROM books"""
        cur = con.execute(sql)
        all_books = cur.fetchall()
        return all_books
    
    @active_log
    def getArticle(self, con):
        """ Get articles from given input """
        sql = """SELECT id, title, surname, firstname, magazine, issue, date FROM articles"""
        cur = con.execute(sql)
        all_articles = cur.fetchall()
        return all_articles

    @active_log
    def addBook(self, con, tuple):
        """ Executes sql insert statement and commits it to book database """
        sql = """INSERT INTO books (title, surname, firstname, publisher, year, genre) values (?, ?, ?, ?, ?, ?)"""
        cur = con.execute(sql, tuple)
        con.commit()

    @active_log
    def addArticle(self, con, tuple):
        """ Executes sql insert statement and commits it to article database """
        sql = """INSERT INTO articles (title, surname, firstname, magazine, issue, date) values (?, ?, ?, ?, ?, ?)"""
        cur = con.execute(sql, tuple)
        con.commit()

    @active_log
    def deleteBook(self, con, id):
        """ Deletes a book from the database """
        sql = """DELETE FROM books WHERE id = ?"""
        tuple = (id,)
        cur = con.execute(sql, tuple)
        con.commit()

    @active_log
    def deleteArticle(self, con, id):
        """ Delete an article from the database """
        sql = """DELETE FROM articles WHERE id = ?"""
        tuple = (id,)
        cur = con.execute(sql, tuple)
        con.commit()
