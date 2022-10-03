import wx
import gui
from math import *
 
class CalcFrame(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MainFrame.__init__(self,parent)
 

    def solveFunc(self,event):
        try:
            #evaluate the string in 'text' and put the answer back
            ans = eval(self.text.GetValue())
            self.text.SetValue (str(ans))
        except Exception:
            print('error')
    
    #put a blank string in text when 'Clear' is clicked
    def clearFunc(self,event):
        self.text.SetValue(str(''))
 

app = wx.App(False)

frame = CalcFrame(None)
frame.Show(True)

app.MainLoop()