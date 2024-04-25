import sys 
from PySide6.QtWidgets import QApplication
from login_page import login
from mainWindow_page import MainWindow_page
app = QApplication(sys.argv)
# window = login()
window= MainWindow_page()
window.show()
app.exec()