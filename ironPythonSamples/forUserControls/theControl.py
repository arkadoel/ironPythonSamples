import wpf

from System.Windows.Controls import *
from System.Windows.Media import *
from System.Windows import Window
from forUserControls import myWindow


class theControl(UserControl):
    def __init__(self, parent=None):
        wpf.LoadComponent(self, 'forUserControls/theControl.xaml')
        self.parent_window = parent
        self.btn_do.Click += self.btnDo_Click

    def btnDo_Click(self, sender, e):

        self.parent_window.etiqueta.Content = 'Cambio'
        self.parent_window.Background = Brushes.AliceBlue

