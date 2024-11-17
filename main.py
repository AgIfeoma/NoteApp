import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
