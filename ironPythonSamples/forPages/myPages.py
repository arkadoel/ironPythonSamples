import wpf

from System.Windows import Window
from System.Windows.Controls import Page

class myPages(Page):
    def __init__(self):
        self.contador = 0
        wpf.LoadComponent(self, 'forPages/myPages.xaml')
    
    def Button_Click(self, sender, e):
        self.lbl.Content = str(self.contador)
        self.contador +=1
        
