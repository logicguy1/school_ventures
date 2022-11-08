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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 820,962 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		self.dataviewstuff = self.dataView_book.AppendTextColumn( u"Firstname" )
		self.m_dataViewListColumn16 = self.dataView_book.AppendTextColumn( u"Surname" )
		self.m_dataViewListColumn17 = self.dataView_book.AppendTextColumn( u"Title" )
		self.m_dataViewListColumn18 = self.dataView_book.AppendTextColumn( u"Publisher" )
		self.m_dataViewListColumn19 = self.dataView_book.AppendTextColumn( u"Year" )
		self.m_dataViewListColumn20 = self.dataView_book.AppendTextColumn( u"Genre" )
		bSizer161.Add( self.dataView_book, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel51.SetSizer( bSizer161 )
		self.m_panel51.Layout()
		bSizer161.Fit( self.m_panel51 )
		sbSizer1.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.search_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.search_button, 0, wx.ALL, 5 )
		
		self.deleteBtn = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Delete books", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.deleteBtn, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( sbSizer1 )
		self.m_panel1.Layout()
		sbSizer1.Fit( self.m_panel1 )
		self.notebook_searchDB.AddPage( self.m_panel1, u"Search Database", True )
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
		
		self.dataView_viewDatabase = wx.dataview.DataViewListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn1 = self.dataView_viewDatabase.AppendTextColumn( u"id" )
		self.m_dataViewListColumn2 = self.dataView_viewDatabase.AppendTextColumn( u"title" )
		self.m_dataViewListColumn3 = self.dataView_viewDatabase.AppendTextColumn( u"surname" )
		self.m_dataViewListColumn4 = self.dataView_viewDatabase.AppendTextColumn( u"firstname" )
		self.m_dataViewListColumn5 = self.dataView_viewDatabase.AppendTextColumn( u"publisher" )
		self.m_dataViewListColumn6 = self.dataView_viewDatabase.AppendTextColumn( u"year" )
		self.m_dataViewListColumn7 = self.dataView_viewDatabase.AppendTextColumn( u"genre" )
		bSizer12.Add( self.dataView_viewDatabase, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer12 )
		self.m_panel3.Layout()
		bSizer12.Fit( self.m_panel3 )
		self.m_notebook2.AddPage( self.m_panel3, u"Books", True )
		self.m_panel5 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataView_viewArticles = wx.dataview.DataViewListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn29 = self.dataView_viewArticles.AppendTextColumn( u"id" )
		self.m_dataViewListColumn30 = self.dataView_viewArticles.AppendTextColumn( u"title" )
		self.m_dataViewListColumn31 = self.dataView_viewArticles.AppendTextColumn( u"surname" )
		self.m_dataViewListColumn32 = self.dataView_viewArticles.AppendIconTextColumn( u"firstname" )
		self.m_dataViewListColumn33 = self.dataView_viewArticles.AppendTextColumn( u"Name" )
		self.m_dataViewListColumn34 = self.dataView_viewArticles.AppendTextColumn( u"Name" )
		self.m_dataViewListColumn35 = self.dataView_viewArticles.AppendTextColumn( u"Name" )
		bSizer16.Add( self.dataView_viewArticles, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer16 )
		self.m_panel5.Layout()
		bSizer16.Fit( self.m_panel5 )
		self.m_notebook2.AddPage( self.m_panel5, u"Articles", False )
		
		bSizer18.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.export_txt_button = wx.Button( self.m_panel2, wx.ID_ANY, u"Export .txt file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.export_txt_button, 0, wx.ALL, 5 )
		
		self.export_pdf_button = wx.Button( self.m_panel2, wx.ID_ANY, u"Export .pdf file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.export_pdf_button, 0, wx.ALL, 5 )
		
		self.addBookBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Add Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.addBookBtn, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel2, wx.ID_ANY, u"Show log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer15, 0, 0, 5 )
		
		
		self.m_panel2.SetSizer( bSizer18 )
		self.m_panel2.Layout()
		bSizer18.Fit( self.m_panel2 )
		self.notebook_searchDB.AddPage( self.m_panel2, u"View Database", False )
		
		problemChild.Add( self.notebook_searchDB, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( problemChild )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.notebook_searchDB.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.loadData )
		self.search_button.Bind( wx.EVT_BUTTON, self.btn_search )
		self.export_txt_button.Bind( wx.EVT_BUTTON, self.btn_txt )
		self.export_pdf_button.Bind( wx.EVT_BUTTON, self.btn_pdf )
		self.addBookBtn.Bind( wx.EVT_BUTTON, self.btn_open_add )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btn_log )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loadData( self, event ):
		event.Skip()
	
	def btn_search( self, event ):
		event.Skip()
	
	def btn_txt( self, event ):
		event.Skip()
	
	def btn_pdf( self, event ):
		event.Skip()
	
	def btn_open_add( self, event ):
		event.Skip()
	
	def btn_log( self, event ):
		event.Skip()
	

###########################################################################
## Class EditDialog
###########################################################################

class EditDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 580,766 ), style = wx.DEFAULT_DIALOG_STYLE )
		
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
		
		self.dlg_textCtrl_fname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.dlg_textCtrl_fname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Author Surname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer23.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.dlg_textCtrl_sname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.dlg_textCtrl_sname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer23.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.dlg_textCtrl_title = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.dlg_textCtrl_title, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Publisher", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer23.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.dlg_textCtrl_publish = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.dlg_textCtrl_publish, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer23.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.dlg_textCtrl_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.dlg_textCtrl_year, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Genre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer23.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		dlg_choice_genreChoices = [ wx.EmptyString, u"Non-fiction", u"Fiction" ]
		self.dlg_choice_genre = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dlg_choice_genreChoices, 0 )
		self.dlg_choice_genre.SetSelection( 0 )
		bSizer23.Add( self.dlg_choice_genre, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Add book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button91 = wx.Button( self, wx.ID_ANY, u"Delete book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button91, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.staticText_alert = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_alert.Wrap( -1 )
		bSizer21.Add( self.staticText_alert, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer20 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.btn_add_book )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_add_book( self, event ):
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
		
		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, 0 )
		bSizer25.Add( self.m_listBox4, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button10, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

