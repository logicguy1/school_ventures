import wx
import gui
from math import *

class EncryptFrame(gui.MainFrame):
    """
    Class for user interface

    Attributes:

    Methods:
        encryptFunc: Encrypts given text
        decryptFunc: Decrypts given text
        onClose: Exits loop

    """

    def __init__(self,parent):
        gui.MainFrame.__init__(self,parent)

    def encryptFunc(self, event):
        plain_text =  self.encrypt_textCtrl.GetValue()
        cipher_text = ""
        key = 7
        for i in range(len(plain_text)):
            letter = plain_text[i]
            
            # Uppercase scenario
            if (letter.isupper()):
                cipher_text += chr((ord(letter)+key-65)%26+65)
            # Lowercase scenario
            else:
                cipher_text += chr((ord(letter)+key-97)%26+97)
        
        self.encryptionTxt.SetLabel(cipher_text)
    
    def decryptFunc(self, event):
        cipher_text = self.decrypt_textCtrl.GetValue()
        plain_text = ""
        key = 7

        for i in range(len(cipher_text)):
            letter = cipher_text[i]
            if (letter.isupper()):
                plain_text += chr((ord(letter)-key-65)%26+65)
            else:
                plain_text += chr((ord(letter)-key-97)%26+97)
        
        self.decryptTxt.SetLabel(plain_text)

    def onClose(self,event):
        self.Destroy()

def main():
    app = wx.App(False)
    frame = EncryptFrame(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()