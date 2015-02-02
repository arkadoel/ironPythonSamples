import wpf

from System.Windows import Window
from forUserControls import theControl

class myWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'forUserControls/myWindow.xaml')

        
        the_control = theControl.theControl(parent=self)
        self.Contenedor.Children.Add(the_control)

