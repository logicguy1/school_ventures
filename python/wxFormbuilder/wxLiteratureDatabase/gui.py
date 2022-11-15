# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		problemChild = wx.BoxSizer( wx.VERTICAL )
		
		self.notebook_searchDB = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.notebook_searchDB, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Literature Database", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )
		sbSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline5 = wx.StaticLine( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		sbSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer3.Add( self.m_staticText5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer3.Add( self.m_staticText7, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrl_firstname = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.textCtrl_firstname, 1, wx.ALL, 5 )
		
		self.textCtrl_surname = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.textCtrl_surname, 1, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		sbSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.textCtrl_title = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.textCtrl_title, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Publisher", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer11.Add( self.m_staticText9, 1, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer11.Add( self.m_staticText11, 1, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrl_publisher = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.textCtrl_publisher, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrl_year = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.textCtrl_year, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Genre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		sbSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		choice_genreChoices = [ wx.EmptyString, u"Fiction", u"Non-fiction" ]
		self.choice_genre = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_genreChoices, 0 )
		self.choice_genre.SetSelection( 0 )
		sbSizer1.Add( self.choice_genre, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel51 = wx.Panel( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataView_book = wx.dataview.DataViewListCtrl( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataviewstuff = self.dataView_book.AppendTextColumn( u"Title" )
		self.m_dataViewListColumn16 = self.dataView_book.AppendTextColumn( u"Surname" )
		self.m_dataViewListColumn17 = self.dataView_book.AppendTextColumn( u"First name" )
		self.m_dataViewListColumn18 = self.dataView_book.AppendTextColumn( u"Publisher" )
		self.m_dataViewListColumn19 = self.dataView_book.AppendTextColumn( u"Year" )
		self.m_dataViewListColumn20 = self.dataView_book.AppendTextColumn( u"Genre" )
		bSizer161.Add( self.dataView_book, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel51.SetSizer( bSizer161 )
		self.m_panel51.Layout()
		bSizer161.Fit( self.m_panel51 )
		sbSizer1.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.search_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.search_button, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer22, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( sbSizer1 )
		self.m_panel1.Layout()
		sbSizer1.Fit( self.m_panel1 )
		self.notebook_searchDB.AddPage( self.m_panel1, u"Search Database", False )
		self.m_panel2 = wx.Panel( self.notebook_searchDB, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText13 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Literature Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer18.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer18.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_notebook2 = wx.Notebook( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel3 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataView_viewBooks = wx.dataview.DataViewListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn21 = self.dataView_viewBooks.AppendTextColumn( u"id" )
		self.m_dataViewListColumn2 = self.dataView_viewBooks.AppendTextColumn( u"Title" )
		self.m_dataViewListColumn3 = self.dataView_viewBooks.AppendTextColumn( u"Surname" )
		self.m_dataViewListColumn4 = self.dataView_viewBooks.AppendTextColumn( u"First name" )
		self.m_dataViewListColumn5 = self.dataView_viewBooks.AppendTextColumn( u"Publisher" )
		self.m_dataViewListColumn6 = self.dataView_viewBooks.AppendTextColumn( u"Year" )
		self.m_dataViewListColumn7 = self.dataView_viewBooks.AppendTextColumn( u"Genre" )
		bSizer12.Add( self.dataView_viewBooks, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer12 )
		self.m_panel3.Layout()
		bSizer12.Fit( self.m_panel3 )
		self.m_notebook2.AddPage( self.m_panel3, u"Books", False )
		self.m_panel5 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataView_viewArticles = wx.dataview.DataViewListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn22 = self.dataView_viewArticles.AppendTextColumn( u"id" )
		self.m_dataViewListColumn30 = self.dataView_viewArticles.AppendTextColumn( u"Title" )
		self.m_dataViewListColumn31 = self.dataView_viewArticles.AppendTextColumn( u"Surname" )
		self.m_dataViewListColumn32 = self.dataView_viewArticles.AppendTextColumn( u"First name" )
		self.m_dataViewListColumn33 = self.dataView_viewArticles.AppendTextColumn( u"Magazine" )
		self.m_dataViewListColumn34 = self.dataView_viewArticles.AppendTextColumn( u"Issue" )
		self.m_dataViewListColumn35 = self.dataView_viewArticles.AppendTextColumn( u"Date" )
		bSizer16.Add( self.dataView_viewArticles, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer16 )
		self.m_panel5.Layout()
		bSizer16.Fit( self.m_panel5 )
		self.m_notebook2.AddPage( self.m_panel5, u"Articles", True )
		
		bSizer18.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.export_txt_button = wx.Button( self.m_panel2, wx.ID_ANY, u"Export .txt file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.export_txt_button, 0, wx.ALL, 5 )
		
		self.export_pdf_button = wx.Button( self.m_panel2, wx.ID_ANY, u"Export .pdf file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.export_pdf_button, 0, wx.ALL, 5 )
		
		self.addBookBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Add book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.addBookBtn, 0, wx.ALL, 5 )
		
		self.addArticle_button18 = wx.Button( self.m_panel2, wx.ID_ANY, u"Add article", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.addArticle_button18, 0, wx.ALL, 5 )
		
		self.deleteBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Delete item", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.deleteBtn, 0, wx.ALL, 5 )
		
		self.logBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Show log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.logBtn, 0, wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer15, 0, 0, 5 )
		
		
		self.m_panel2.SetSizer( bSizer18 )
		self.m_panel2.Layout()
		bSizer18.Fit( self.m_panel2 )
		self.notebook_searchDB.AddPage( self.m_panel2, u"View Database", True )
		
		problemChild.Add( self.notebook_searchDB, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( problemChild )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.notebook_searchDB.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.loadData )
		self.search_button.Bind( wx.EVT_BUTTON, self.btn_search )
		self.export_txt_button.Bind( wx.EVT_BUTTON, self.btn_export_txt )
		self.export_pdf_button.Bind( wx.EVT_BUTTON, self.btn_export_pdf )
		self.addBookBtn.Bind( wx.EVT_BUTTON, self.btn_add_book )
		self.addArticle_button18.Bind( wx.EVT_BUTTON, self.btn_add_article )
		self.deleteBtn.Bind( wx.EVT_BUTTON, self.btn_delete )
		self.logBtn.Bind( wx.EVT_BUTTON, self.btn_log )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loadData( self, event ):
		event.Skip()
	
	def btn_search( self, event ):
		event.Skip()
	
	def btn_export_txt( self, event ):
		event.Skip()
	
	def btn_export_pdf( self, event ):
		event.Skip()
	
	def btn_add_book( self, event ):
		event.Skip()
	
	def btn_add_article( self, event ):
		event.Skip()
	
	def btn_delete( self, event ):
		event.Skip()
	
	def btn_log( self, event ):
		event.Skip()
	

###########################################################################
## Class AddBookDialog
###########################################################################

class AddBookDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 650,680 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Add Book to Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer20.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer20.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Author First name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer23.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.bookCtrl_fname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_fname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Author Surname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer23.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.bookCtrl_sname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_sname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer23.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.bookCtrl_title = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_title, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Publisher", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer23.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.bookCtrl_publish = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_publish, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer23.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.bookCtrl_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_year, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Genre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer23.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		book_choice_genreChoices = [ wx.EmptyString, u"Non-fiction", u"Fiction" ]
		self.book_choice_genre = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, book_choice_genreChoices, 0 )
		self.book_choice_genre.SetSelection( 0 )
		bSizer23.Add( self.book_choice_genre, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self, wx.ID_OK, u"Add book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_CLOSE, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer20 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.addBook )
		self.m_button9.Bind( wx.EVT_BUTTON, self.exitDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addBook( self, event ):
		event.Skip()
	
	def exitDialog( self, event ):
		event.Skip()
	

###########################################################################
## Class AddArticleDialog
###########################################################################

class AddArticleDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 450,480 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Add Article to Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer20.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer20.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Author First name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer23.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.artCtrl_fname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_fname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Author Surname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer23.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.artCtrl_sname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_sname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer23.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.artCtrl_title = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_title, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Magazine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer23.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.artCtrl_magazine = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_magazine, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Issue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer23.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.artCtrl_issue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_issue, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Date Month", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		bSizer36.Add( self.m_staticText40, 1, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Date Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer36.Add( self.m_staticText41, 1, wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		choice_monthChoices = [ wx.EmptyString, u"januar", u"februar", u"marts", u"april", u"maj", u"juni", u"juli", u"august", u"september", u"oktober", u"november", u"december" ]
		self.choice_month = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_monthChoices, 0 )
		self.choice_month.SetSelection( 7 )
		bSizer37.Add( self.choice_month, 1, wx.ALL, 5 )
		
		self.artCtrl_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.artCtrl_year, 1, wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer37, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self, wx.ID_OK, u"Add article", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_CLOSE, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer20 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.addArticle )
		self.m_button9.Bind( wx.EVT_BUTTON, self.exitDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addArticle( self, event ):
		event.Skip()
	
	def exitDialog( self, event ):
		event.Skip()
	

###########################################################################
## Class LogFrame
###########################################################################

class LogFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 611,703 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Log frame", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer25.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer261 = wx.BoxSizer( wx.VERTICAL )
		
		self.log_staticText = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.log_staticText.Wrap( -1 )
		bSizer261.Add( self.log_staticText, 0, wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( bSizer261 )
		self.m_panel6.Layout()
		bSizer261.Fit( self.m_panel6 )
		bSizer25.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button10, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button10.Bind( wx.EVT_BUTTON, self.onClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onClose( self, event ):
		event.Skip()
	

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		problemChild = wx.BoxSizer( wx.VERTICAL )
		
		self.notebook_searchDB = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.notebook_searchDB, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Literature Database", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )
		sbSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline5 = wx.StaticLine( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		sbSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer3.Add( self.m_staticText5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer3.Add( self.m_staticText7, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrl_firstname = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.textCtrl_firstname, 1, wx.ALL, 5 )
		
		self.textCtrl_surname = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.textCtrl_surname, 1, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		sbSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.textCtrl_title = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.textCtrl_title, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Publisher", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer11.Add( self.m_staticText9, 1, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer11.Add( self.m_staticText11, 1, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrl_publisher = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.textCtrl_publisher, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrl_year = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.textCtrl_year, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Genre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		sbSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		choice_genreChoices = [ wx.EmptyString, u"Fiction", u"Non-fiction" ]
		self.choice_genre = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_genreChoices, 0 )
		self.choice_genre.SetSelection( 0 )
		sbSizer1.Add( self.choice_genre, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel51 = wx.Panel( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataView_book = wx.dataview.DataViewListCtrl( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataviewstuff = self.dataView_book.AppendTextColumn( u"Title" )
		self.m_dataViewListColumn16 = self.dataView_book.AppendTextColumn( u"Surname" )
		self.m_dataViewListColumn17 = self.dataView_book.AppendTextColumn( u"First name" )
		self.m_dataViewListColumn18 = self.dataView_book.AppendTextColumn( u"Publisher" )
		self.m_dataViewListColumn19 = self.dataView_book.AppendTextColumn( u"Year" )
		self.m_dataViewListColumn20 = self.dataView_book.AppendTextColumn( u"Genre" )
		bSizer161.Add( self.dataView_book, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel51.SetSizer( bSizer161 )
		self.m_panel51.Layout()
		bSizer161.Fit( self.m_panel51 )
		sbSizer1.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.search_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.search_button, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer22, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( sbSizer1 )
		self.m_panel1.Layout()
		sbSizer1.Fit( self.m_panel1 )
		self.notebook_searchDB.AddPage( self.m_panel1, u"Search Database", False )
		self.m_panel2 = wx.Panel( self.notebook_searchDB, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText13 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Literature Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer18.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer18.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_notebook2 = wx.Notebook( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel3 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataView_viewBooks = wx.dataview.DataViewListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn21 = self.dataView_viewBooks.AppendTextColumn( u"id" )
		self.m_dataViewListColumn2 = self.dataView_viewBooks.AppendTextColumn( u"Title" )
		self.m_dataViewListColumn3 = self.dataView_viewBooks.AppendTextColumn( u"Surname" )
		self.m_dataViewListColumn4 = self.dataView_viewBooks.AppendTextColumn( u"First name" )
		self.m_dataViewListColumn5 = self.dataView_viewBooks.AppendTextColumn( u"Publisher" )
		self.m_dataViewListColumn6 = self.dataView_viewBooks.AppendTextColumn( u"Year" )
		self.m_dataViewListColumn7 = self.dataView_viewBooks.AppendTextColumn( u"Genre" )
		bSizer12.Add( self.dataView_viewBooks, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer12 )
		self.m_panel3.Layout()
		bSizer12.Fit( self.m_panel3 )
		self.m_notebook2.AddPage( self.m_panel3, u"Books", False )
		self.m_panel5 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataView_viewArticles = wx.dataview.DataViewListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn22 = self.dataView_viewArticles.AppendTextColumn( u"id" )
		self.m_dataViewListColumn30 = self.dataView_viewArticles.AppendTextColumn( u"Title" )
		self.m_dataViewListColumn31 = self.dataView_viewArticles.AppendTextColumn( u"Surname" )
		self.m_dataViewListColumn32 = self.dataView_viewArticles.AppendTextColumn( u"First name" )
		self.m_dataViewListColumn33 = self.dataView_viewArticles.AppendTextColumn( u"Magazine" )
		self.m_dataViewListColumn34 = self.dataView_viewArticles.AppendTextColumn( u"Issue" )
		self.m_dataViewListColumn35 = self.dataView_viewArticles.AppendTextColumn( u"Date" )
		bSizer16.Add( self.dataView_viewArticles, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer16 )
		self.m_panel5.Layout()
		bSizer16.Fit( self.m_panel5 )
		self.m_notebook2.AddPage( self.m_panel5, u"Articles", True )
		
		bSizer18.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.export_txt_button = wx.Button( self.m_panel2, wx.ID_ANY, u"Export .txt file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.export_txt_button, 0, wx.ALL, 5 )
		
		self.export_pdf_button = wx.Button( self.m_panel2, wx.ID_ANY, u"Export .pdf file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.export_pdf_button, 0, wx.ALL, 5 )
		
		self.addBookBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Add book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.addBookBtn, 0, wx.ALL, 5 )
		
		self.addArticle_button18 = wx.Button( self.m_panel2, wx.ID_ANY, u"Add article", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.addArticle_button18, 0, wx.ALL, 5 )
		
		self.deleteBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Delete item", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.deleteBtn, 0, wx.ALL, 5 )
		
		self.logBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Show log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.logBtn, 0, wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer15, 0, 0, 5 )
		
		
		self.m_panel2.SetSizer( bSizer18 )
		self.m_panel2.Layout()
		bSizer18.Fit( self.m_panel2 )
		self.notebook_searchDB.AddPage( self.m_panel2, u"View Database", True )
		
		problemChild.Add( self.notebook_searchDB, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( problemChild )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.notebook_searchDB.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.loadData )
		self.search_button.Bind( wx.EVT_BUTTON, self.btn_search )
		self.export_txt_button.Bind( wx.EVT_BUTTON, self.btn_export_txt )
		self.export_pdf_button.Bind( wx.EVT_BUTTON, self.btn_export_pdf )
		self.addBookBtn.Bind( wx.EVT_BUTTON, self.btn_add_book )
		self.addArticle_button18.Bind( wx.EVT_BUTTON, self.btn_add_article )
		self.deleteBtn.Bind( wx.EVT_BUTTON, self.btn_delete )
		self.logBtn.Bind( wx.EVT_BUTTON, self.btn_log )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loadData( self, event ):
		event.Skip()
	
	def btn_search( self, event ):
		event.Skip()
	
	def btn_export_txt( self, event ):
		event.Skip()
	
	def btn_export_pdf( self, event ):
		event.Skip()
	
	def btn_add_book( self, event ):
		event.Skip()
	
	def btn_add_article( self, event ):
		event.Skip()
	
	def btn_delete( self, event ):
		event.Skip()
	
	def btn_log( self, event ):
		event.Skip()
	

###########################################################################
## Class AddBookDialog
###########################################################################

class AddBookDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 650,680 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Add Book to Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer20.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer20.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Author First name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer23.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.bookCtrl_fname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_fname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Author Surname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer23.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.bookCtrl_sname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_sname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer23.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.bookCtrl_title = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_title, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Publisher", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer23.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.bookCtrl_publish = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_publish, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer23.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.bookCtrl_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.bookCtrl_year, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Genre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer23.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		book_choice_genreChoices = [ wx.EmptyString, u"Non-fiction", u"Fiction" ]
		self.book_choice_genre = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, book_choice_genreChoices, 0 )
		self.book_choice_genre.SetSelection( 0 )
		bSizer23.Add( self.book_choice_genre, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self, wx.ID_OK, u"Add book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_CLOSE, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer20 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.addBook )
		self.m_button9.Bind( wx.EVT_BUTTON, self.exitDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addBook( self, event ):
		event.Skip()
	
	def exitDialog( self, event ):
		event.Skip()
	

###########################################################################
## Class AddArticleDialog
###########################################################################

class AddArticleDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 450,480 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Add Article to Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer20.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer20.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Author First name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer23.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.artCtrl_fname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_fname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Author Surname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer23.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.artCtrl_sname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_sname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer23.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.artCtrl_title = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_title, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Magazine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer23.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.artCtrl_magazine = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_magazine, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Issue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer23.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.artCtrl_issue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.artCtrl_issue, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Date Month", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		bSizer36.Add( self.m_staticText40, 1, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Date Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer36.Add( self.m_staticText41, 1, wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		choice_monthChoices = [ wx.EmptyString, u"januar", u"februar", u"marts", u"april", u"maj", u"juni", u"juli", u"august", u"september", u"oktober", u"november", u"december" ]
		self.choice_month = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_monthChoices, 0 )
		self.choice_month.SetSelection( 7 )
		bSizer37.Add( self.choice_month, 1, wx.ALL, 5 )
		
		self.artCtrl_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.artCtrl_year, 1, wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer37, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self, wx.ID_OK, u"Add article", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_CLOSE, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer20 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.addArticle )
		self.m_button9.Bind( wx.EVT_BUTTON, self.exitDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addArticle( self, event ):
		event.Skip()
	
	def exitDialog( self, event ):
		event.Skip()
	

###########################################################################
## Class LogFrame
###########################################################################

class LogFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 611,703 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Log frame", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer25.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer261 = wx.BoxSizer( wx.VERTICAL )
		
		self.log_staticText = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.log_staticText.Wrap( -1 )
		bSizer261.Add( self.log_staticText, 0, wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( bSizer261 )
		self.m_panel6.Layout()
		bSizer261.Fit( self.m_panel6 )
		bSizer25.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button10, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button10.Bind( wx.EVT_BUTTON, self.onClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onClose( self, event ):
		event.Skip()
	

