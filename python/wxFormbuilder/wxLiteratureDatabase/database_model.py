class DatabaseModel():

    def __init__(self, pubsub):
        self.pb = pubsub

    def active_log(func):
        def wrapper(self, *args, **kwargs):
            self.pb.sendMessage("MyMainFrame", message = f"{func.__name__} - {args} - {func.__doc__}")
            return func(self, *args, **kwargs)
        return wrapper

    @active_log
    def searchBooks(self, con, args):
        sql = """SELECT title, surname, firstname, publisher, year, genre FROM books WHERE title LIKE ? AND 
                surname LIKE ? AND firstname LIKE ? AND publisher LIKE ? AND year LIKE ? AND genre LIKE ? """
        cur = con.execute(sql, args)
        book_data = cur.fetchall()
        return book_data

    @active_log
    def getBooks(self, con):
        """Get books from given input"""
        sql = """SELECT id, title, surname, firstname, publisher, year, genre FROM books"""
        cur = con.execute(sql)
        all_books = cur.fetchall()
        return all_books
    
    @active_log
    def getArticle(self, con):
        """Get articles from given input"""
        sql = """SELECT id, title, surname, firstname, magazine, issue, date FROM articles"""
        cur = con.execute(sql)
        all_articles = cur.fetchall()
        return all_articles

    @active_log
    def addBook(self, con, tuple):
        """Executes sql insert statement and commits it to book database"""
        sql = """INSERT INTO books (title, surname, firstname, publisher, year, genre) values (?, ?, ?, ?, ?, ?)"""
        cur = con.execute(sql, tuple)
        con.commit()

    @active_log
    def addArticle(self, con, tuple):
        """Executes sql insert statement and commits it to article database"""
        sql = """INSERT INTO articles (title, surname, firstname, magazine, issue, date) values (?, ?, ?, ?, ?, ?)"""
        cur = con.execute(sql, tuple)
        con.commit()

    @active_log
    def deleteBook(self, con, id):
        sql = """DELETE FROM books WHERE id = ?"""
        tuple = (id,)
        cur = con.execute(sql, tuple)
        con.commit()

    @active_log
    def deleteArticle(self, con, id):
        sql = """DELETE FROM articles WHERE id = ?"""
        tuple = (id,)
        cur = con.execute(sql, tuple)
        con.commit()
