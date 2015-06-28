import clr
import System

clr.AddReference('Microsoft.Office.Interop.Excel')
from Microsoft.Office.Interop import Excel
import Microsoft.Office.Interop.Excel
import os
FILE = os.path.join(os.getcwd(), 'Libro1.xlsx')


if __name__ == "__main__":

    print('Directorio actual= ' + FILE)
    #raw_input('-->colo')
    
    """
    xlapp = Excel.ApplicationClass()
    xlapp.Visible = True
    xlapp.DisplayAlerts = False
       
    libro = xlapp.Workbooks.Open(FILE)
    
    print('Abierto')
    hoja = libro.Sheets[1]
    #assert isinstance(hoja,  Excel.Worksheet)
    celda = hoja.Range['A:2']
    #assert isinstance(celda, Excel.Range)
    celda.Value2 = 'hola'
    print('Asignado valor')

    #libro.Save()
    #libro.Close(True, System.Type.Missing, System.Type.Missing)
    #xlapp.Quit()

    #l = raw_input('-->Pausa')
    """
    m = System.Type.Missing
    # Instantiate the Excel Application
    ex = Excel.ApplicationClass()

    # Make it Visiable for us all to see
    ex.Visible = True

    # Disable Alerts - Errors Ignore them, they're probably not important
    ex.DisplayAlerts = False

    # Create a new Workbook = Spreadsheet file
    #workbooks = ex.Workbooks.Add( Excel.XlWBATemplate.xlWBATWorksheet)
    wb = ex.Workbooks.Open(FILE)

    #Create a new Worksheet within our new Workbook
    ws = wb.Worksheets[1]  # Arrays of Object Start 1 in the MS Office World

    #creamos una nueva hoja
    nueva = wb.Worksheets.Add()
    nueva.Name = 'hoja nueva'

    # Put Hello World in Cell A1
    cell = ws.Range["A1"]
    cell.Value2 = 33

    wb.Save()
    wb.Close(SaveChanges=True)
    ex.Quit()
    

    
    
    print('fin')

    #end
