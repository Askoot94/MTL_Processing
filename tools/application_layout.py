from PyQt6.QtCore import QEvent, Qt, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QTextEdit, 
    QHBoxLayout, QVBoxLayout, QPushButton,
    QPlainTextEdit, QFileDialog, QScrollBar,
    QWidget
)
from PyQt6.QtGui import QFocusEvent, QTextDocument

from .glossary import createGlossary, replaceTerms

# This is the Qlabel that hold the title text for the application
class title(QLabel):
    def __init__(self):
        super().__init__()

        self.setText("Bulk Term Replacements")
        
        titleFont = self.font()
        titleFont.setUnderline(True)
        titleFont.setPointSize(26)
        self.setFont(titleFont)

        self.setMaximumSize(600, 400)

class glossaryInsert(QPlainTextEdit):
    glossary = []

    def focusOutEvent(self, e: QFocusEvent | None) -> None:
        self.updateGlossary()
        return super().focusOutEvent(e)

    def updateGlossary(self):
        plainText = self.toPlainText()

        # Need to implment faster iteration that checks if term already exists in list before adding.
        self.glossary.clear()
        self.glossary = createGlossary(plainText)

    def __init__(self):
        super().__init__()

        self.setBaseSize(360, 400)
        self.setMaximumHeight(800)

        self.setPlaceholderText("Insert glossary replacement terms here.\n" 
        "Format: {Find}={Replace} i.e Hello=World")

        self.addScrollBarWidget(QScrollBar(), Qt.AlignmentFlag(0x0002))

class TopLayer(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.glossaryWidget = glossaryInsert()
        capTitle = title()
        capTitle.setAlignment(Qt.AlignmentFlag(0x0021))

        # Consists of Title and Glossary Replacements
        self.addWidget(capTitle)
        self.addWidget(self.glossaryWidget)

# This is the TextEdit box that will receive the pre-replaced text
class inputText(QTextEdit):
    
    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Enter Text to perform replacement...")
        
        formatting = self.font()
        formatting.setPointSize(14)
        self.setFont(formatting)
        
        self.setBaseSize(960, 900)
        self.setMaximumHeight(1000)
    
class outputText(QTextEdit):
    
    def updateText(self, str):
        self.setText(str)

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.addScrollBarWidget(QScrollBar(), Qt.AlignmentFlag(0x0002))

        formatting = self.font()
        formatting.setPointSize(18)
        self.setFont(formatting)

        self.setMinimumHeight(200)
        self.setMinimumWidth(400)
        
        self.setPlaceholderText("Replaced Text will appear here...")

class TextLayer(QVBoxLayout):
    buttonClicked = pyqtSignal((str, ))

    @pyqtSlot()
    def startReplacement(self):
        document = self.textBox.toPlainText()
        self.buttonClicked.emit(document)

    def updateOutputText(self, text:str):
        self.output.updateText(text)

    def __init__(self):
        super().__init__()

        inputting = QHBoxLayout()
        
        self.textBox = inputText()
        inputting.addWidget(self.textBox)
        
        self.submit = QPushButton()
        self.submit.setText("Start Replacement")
        self.submit.clicked.connect(lambda: self.startReplacement())

        inputting.addWidget(self.submit)

        importGroup = QWidget()
        importGroup.setLayout(inputting)

        self.addWidget(importGroup)

        self.output = outputText()
        self.addWidget(self.output)

class FinalLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # Combine Top Layer with Text Layer
        top = QWidget()
        text = QWidget()
        self.layText = TextLayer()
        self.layInp = TopLayer()
        top.setLayout(self.layInp)
        text.setLayout(self.layText)

        self.layText.buttonClicked.connect(self.replacement)

        self.addWidget(top)
        self.addWidget(text)

    @pyqtSlot((str))
    def replacement(self, document:str):
        # Using Created Glossary and Given Plaintext perform call replacement and update Output Text
        # grab Glossary
        terms = self.layInp.glossaryWidget.glossary
        
        try:
            self.layText.updateOutputText(replaceTerms(document, terms))
        except Exception as e:
            print(e)
            self.layText.updateOutputText("An Error has occured.") 

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        parentWidget = QWidget()
        parentWidget.setLayout(FinalLayout())

        self.setCentralWidget(parentWidget)