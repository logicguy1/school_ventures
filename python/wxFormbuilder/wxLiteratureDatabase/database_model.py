class DatabaseModel():

    def getBooks(self, con):
        """Get books from given input"""
        sql = """SELECT id, title, surname, firstname, publisher, year, genre FROM books"""
        cur = con.execute(sql)
        all_books = cur.fetchall()
        return all_books
    
    def getArticle(self, con):
        """Get articles from given input"""
        sql = """SELECT id, title, surname, firstname, magazine, issue, date FROM articles"""
        cur = con.execute(sql)
        all_articles = cur.fetchall()
        return all_articles

    def addBook(self, con, tuple):
        """Executes sql insert statement and commits it to database"""
        sql = """INSERT INTO books (title, surname, firstname, publisher, year, genre) values (?, ?, ?, ?, ?, ?)"""
        cur = con.execute(sql, tuple)
        con.commit()

    def deleteItems(self, con):
        sql = """DELETE FROM books (title, surname, firstname, publisher, year, genre) WHERE (?, ?, ?, ?, ?, ?)"""
        cur = con.execute(sql)
        delete_book = cur.fetchall()
        return delete_book