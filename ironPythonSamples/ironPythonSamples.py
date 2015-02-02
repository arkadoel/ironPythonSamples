import wpf

from System.Windows import Application, Window
from forUserControls import myWindow
from forPages import pagesSample

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'ironPythonSamples.xaml')
        self.btn1.Click += self.btn1_click
        self.btn2.Click += self.btn2_click

    def btn1_click(self, sender, e):
        myWindow.myWindow().Show()  
        
    def btn2_click(self, sender, e):  
        pagesSample.pagesSample().Show()

if __name__ == '__main__':
    Application().Run(MyWindow())
