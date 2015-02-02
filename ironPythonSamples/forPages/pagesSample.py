import wpf

from System.Windows import Window
from forPages import myPages

class pagesSample(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'forPages/pagesSample.xaml')
        self.btnLoad.Click += self.btnLoad_click

    def btnLoad_click(self, sender, e):
        self.navegador.Navigate(myPages.myPages())