from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


if __name__ == '__main__':
    app = QApplication([])
    
    window = QMainWindow()
    window.setWindowTitle("Category Theory : Identity Morphisms Are Unique")
    window.show()
    
    home = QLabel("Home Test")
    definition = QLabel(r"An \\textbf{identity morphism} $\text{id} = \text{id}_A : A \to A$ is defined... An identity morphism exists for any object $A$ of a category $C$ by definition of category.")
    
    stacked = QStackedWidget()
    stacked.addWidget(home)
    stacked.addWidget(definition)
    
    window.setCentralWidget(stacked)
    
    window.menuBar().addAction("Home").triggered.connect(lambda: stacked.setCurrentWidget(home))
    window.menuBar().addAction("Definition").triggered.connect(lambda: stacked.setCurrentWidget(definition))
    
    sys.exit(app.exec_())