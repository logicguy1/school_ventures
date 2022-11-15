import sqlite3 as lite
from pubsub import pub as pb

import wx
import gui
import datetime

from database_model import DatabaseModel
from fpdf import FPDF


class MainFrame(gui.MainFrame):
    """
    Class for second user interface

    Attributes:
        LogFrame: The frame used for logging
        con: sqlite3 database object
        cur: sqlite3 cursor object
        dataModel: The database model used for data communication
    
    Methods:
        btn_search: Searches database with given search args
        loadData: Loads the database with books and articles
        btn_export_txt: exports a txt file of book database
        btn_export_pdf: exports a pdf of book database
        btn_add_book: Opens dialogbox and adds named book
        btn_add_article: Opens dialogbox and adds named article
        btn_delete: Deletes books and articles from database
        btn_log: Opens LogFrame and shows all logs
        onClose: exits window
    """

    def __init__(self, parent): 
        gui.MainFrame.__init__(self, parent)
        self.LogFrame = LogFrame(self)

        # Fixed value
        self.con = lite.connect('literature.db')
        self.cur = self.con.cursor()
        self.dataModel = DatabaseModel(pb)
    
    def btn_search(self, event):
        # Fixed value
        fname = self.textCtrl_firstname.GetValue()
        sname = self.textCtrl_surname.GetValue()
        title = self.textCtrl_title.GetValue()
        publisher = self.textCtrl_publisher.GetValue()
        year = self.textCtrl_year.GetValue()
        genre = self.choice_genre.GetStringSelection()
        
        ctxFilter = lambda x: "%" if str(x) == "" else str(x)

        book_data = self.dataModel.searchBooks(
                self.con, 
                tuple(map(ctxFilter, (title, sname, fname, publisher, year, genre),))
            )
        self.dataView_book.DeleteAllItems()

        for book in book_data:
            self.dataView_book.AppendItem(book)

    def loadData(self, event):
        # Fixed value
        article_data = self.dataModel.getArticle(self.con)
        book_data = self.dataModel.getBooks(self.con)

        self.dataView_viewBooks.DeleteAllItems()
        self.dataView_viewArticles.DeleteAllItems()
        
        # Most recent holder
        for item in article_data:
            self.dataView_viewArticles.AppendItem(list(map(str, item)))

        for item in book_data:
            self.dataView_viewBooks.AppendItem(list(map(str, item)))

    def btn_export_txt(self, event):
        # Fixed value
        all_books = self.dataModel.getBooks(self.con)
        with open("books.txt", "w+", encoding='utf-8') as txt_file:
            for book in all_books:
                txt_file.write(", ".join(book) + '\n')

    def btn_export_pdf(self, event):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 14)
        all_books = self.dataModel.getBooks(self.con)
        
        for book in all_books:
            line = ", ".join(book)
            pdf.cell(200, 10, txt = line, ln = 1, align = 'L')
        pdf.output("books.pdf")  

    def btn_add_book(self, event):
        dlg = gui.AddBookDialog(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            # Fixed value
            fname = dlg.bookCtrl_fname.GetValue()
            sname = dlg.bookCtrl_sname.GetValue()
            title = dlg.bookCtrl_title.GetValue()
            publisher = dlg.bookCtrl_publish.GetValue() 
            year = dlg.bookCtrl_year.GetValue()
            genre = dlg.book_choice_genre.GetStringSelection()
                        
            self.dataModel.addBook(self.con, (title, sname, fname, publisher, year, genre))

        if result == wx.ID_CLOSE:
            self.EndModal(wx.ID_CLOSE)

        self.loadData(None)

    def btn_add_article(self, event):
        dlg = gui.AddArticleDialog(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            # Fixed value
            title = dlg.artCtrl_title.GetValue()
            sname = dlg.artCtrl_sname.GetValue()
            fname = dlg.artCtrl_fname.GetValue()
            magazine = dlg.artCtrl_magazine.GetValue()
            issue = dlg.artCtrl_issue.GetValue()
            month = dlg.choice_month.GetStringSelection()
            year = dlg.artCtrl_year.GetValue()
            date = "{month} {year}"

            self.dataModel.addArticle(self.con, (title, sname, fname, magazine, issue, date))

        self.loadData(None)

    def btn_delete(self, event):
        if self.dataView_viewBooks.HasSelection():
            # Fixed value
            selectedRow = self.dataView_viewBooks.GetSelectedRow()
            item = int(self.dataView_viewBooks.GetValue(selectedRow,0))
            self.dataModel.deleteBook(self.con, item)

        if self.dataView_viewArticles.HasSelection():
            # Fixed value
            selectedRow = self.dataView_viewArticles.GetSelectedRow()
            item = int(self.dataView_viewArticles.GetValue(selectedRow,0))
            self.dataModel.deleteArticle(self.con, item)

        self.loadData(None)

    def btn_log(self, event):
        self.LogFrame.Show(True)

    def onClose(self, event):
        self.con.close()
        exit()


class LogFrame(gui.LogFrame):
    """
    Class for second user interface

    Attributes:
        pb: Pubsub object for handeling events

    Methods:
        listener: Recieves message and adds it to the log
        onClose: Closes window frame
    """

    def __init__(self, parent):
        gui.LogFrame.__init__(self, parent)
        pb.subscribe(self.listener, "MyMainFrame")

    def listener(self, message):
        # Temperarry
        msg = self.log_staticText.Label
        msg += datetime.datetime.now().strftime("%H:%M:%S %m/%d/%Y  | ")
        msg += message + "\n"

        self.log_staticText.SetLabel(msg)

    def onClose(self, event):
        self.Show(False)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
