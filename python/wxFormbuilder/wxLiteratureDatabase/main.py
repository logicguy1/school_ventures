import wx
import gui
import sqlite3 as lite
from database_model import DatabaseModel

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
        sql_query = """SELECT title, surname, firstname, publisher, year, genre FROM books WHERE title LIKE ? AND 
                    surname LIKE ? AND firstname LIKE ? AND publisher LIKE ? AND year LIKE ? AND genre LIKE ? """
        search_args = (title, sname, fname, publisher, year, genre)
        cursor = self.con.execute(sql_query, search_args)
        book_data = cursor.fetchall()
        self.dataView_book.DeleteAllItems()

        for book in book_data:
            self.dataView_book.AppendItem(book)

    def loadData(self, event):
        self.dataView_viewDatabase.DeleteAllItems()
        self.dataView_viewArticles.DeleteAllItems()
        article_data = self.dataModel.getArticle(self.con)
        book_data = self.dataModel.getBooks(self.con)
        
        for item in article_data:
            itemView = (item[1],item[2],item[3],item[4],item[5],item[6])
            self.dataView_viewArticles.AppendItem(itemView)

        for item in book_data:
            itemView = (item[1],item[2],item[3],item[4],item[5],item[6])
            self.dataView_viewDatabase.AppendItem(itemView)

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
                        
            self.dataModel.addBook(self.con, (title, sname, fname, publisher, year, genre))
            self.staticText_alert.SetLabel("New book has been added")

        if result == wx.ID_CLOSE:
            exit()

        if result == wx.ID_DELETE:
            self.dataModel.deleteItems(self.con)

    def onClose(self, event):
        self.con.close()
        exit()

class LogFrame(gui.LogFrame):

    def __init__(self, parent):
        gui.LogFrame.__init__(self, parent)

app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()
