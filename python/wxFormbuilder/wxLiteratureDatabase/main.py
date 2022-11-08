import wx
import gui
import sqlite3 as lite


class DatabaseModel():
    #def setParameters():

    def getBooks(self, con):
        sql = """SELECT id, title, surname, firstname, publisher, year, genre FROM books"""
        cur = con.execute(sql)
        all_books = cur.fetchall()
        return all_books
    
    def getArticle(self, con):
        sql = """SELECT id, title, surname, firstname, magazine, issue, date FROM"""
        cur = con.execute(sql)
        all_articles = cur.fetchall()
        return all_articles

    def addBook(self, con):
        sql = """INSERT INTO books (title, surname, firstname, publisher, year, genre) values (?, ?, ?, ?, ?, ?')"""
        cur = con.execute(sql)
        dataAdd = cur.fetchall()
        return dataAdd

    #def insertBook():

class MainFrame(gui.MainFrame):
    """
    Class for second user interface

    Methods:
        btn_search = Searches database
        onClose = exits window

    """

    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.LogFrame = LogFrame(self)

        self.con = lite.connect('literature.db')
        self.cur = self.con.cursor()
        self.dataModel = DatabaseModel()
    
    def btn_search(self, event):
        fname = str(self.textCtrl_firstname.GetValue())
        sname = str(self.textCtrl_surname.GetValue())
        title = str(self.textCtrl_title.GetValue())
        publisher = str(self.textCtrl_publisher.GetValue())
        year = str(self.textCtrl_year.GetValue())
        genre = str(self.choice_genre.GetStringSelection())

        if fname == "":
            fname = "%"
        if sname == "":
            sname = "%"
        if title == "":
            title = "%"
        if publisher == "":
            publisher = "%"
        if year == "":
            year = "%"
        if genre == "":
            genre = "%"
        
        # Make query statement
        sql_query = """SELECT title, surname, firstname, publisher, year, genre FROM books WHERE title LIKE ? AND surname LIKE ? AND firstname LIKE ? AND publisher LIKE ? AND year LIKE ? AND genre LIKE ? """
        search_args = (title, sname, fname, publisher, year, genre)
        cursor = self.con.execute(sql_query, search_args)
        book_data = cursor.fetchall()
        self.dataView_book.DeleteAllItems()

        for item in book_data:
            self.dataView_book.AppendItem(item)

    def loadData(self, event):
        self.dataView_viewDatabase.DeleteAllItems()
        data = self.dataModel.getBooks(self.con)

        for item in data:
            self.dataView_viewDatabase.AppendItem(item)

    def btn_log(self, event):
        self.LogFrame.Show(True)

    def btn_add(self, event):
        
        dlg = gui.EditDialog(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            fname = dlg.dlg_textCtrl_fname.GetValue()
            sname = dlg.dlg_textCtrl_sname.GetValue()
            title = dlg.dlg_textCtrl_title.GetValue()
            publisher = dlg.dlg_textCtrl_publish.GetValue()
            year = dlg.dlg_textCtrl_year.GetValue()
            genre = dlg.dlg_choice_genre.GetStringSelection()
            
            print("Button clicked")
            self.con.addBook(fname, sname, title, publisher, year, genre)
            self.staticText_alert.SetLabel("New book has been added")

    def onClose(self, event):
        self.con.close()
        exit()

class LogFrame(gui.LogFrame):

    def __init__(self, parent):
        gui.LogFrame.__init__(self, parent)

    def onClose(self, event):
        exit()

app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()