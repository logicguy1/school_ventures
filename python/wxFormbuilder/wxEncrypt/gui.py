# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 553,626 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Encrypt and decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		bSizer2.Add( self.title, 0, wx.ALL, 5 )
		
		self.encrypt_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.encrypt_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.encryptButton = wx.Button( self, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.encryptButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.encryptionTxt = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.encryptionTxt.Wrap( -1 )
		bSizer2.Add( self.encryptionTxt, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.decrypt_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.decrypt_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.decryptButton = wx.Button( self, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.decryptButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.decryptTxt = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.decryptTxt.Wrap( -1 )
		bSizer2.Add( self.decryptTxt, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.encryptButton.Bind( wx.EVT_BUTTON, self.encryptFunc )
		self.decryptButton.Bind( wx.EVT_BUTTON, self.decryptFunc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def encryptFunc( self, event ):
		event.Skip()
	
	def decryptFunc( self, event ):
		event.Skip()
	

