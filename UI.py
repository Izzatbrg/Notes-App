import sys
import requests
import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw


class Window(qtw.QWidget):
    def __init__(self, *argv):
        super().__init__()
        self.url = "http://127.0.0.1:5000/"
        self.setStyleSheet("background-color: #333333;")
        self.title_label = qtw.QLabel("title:")
        self.read_style("label.css", self.title_label)
        self.title_input = qtw.QLineEdit()
        self.read_style("LineEdit.css", self.title_input)
        self.text_label  = qtw.QLabel("text:")
        self.read_style("label.css", self.text_label)
        self.text_input = qtw.QTextEdit()
        self.read_style("TextEdit.css", self.text_input)
        self.enter = qtw.QPushButton()
        self.enter.setText("Enter")
        self.read_style("button.css", self.enter)
        self.enter.clicked.connect(self.post_note)
        self.discard = qtw.QPushButton()
        self.discard.setText("discard")
        self.discard.clicked.connect(self.disc)
        self.read_style("button.css", self.discard)
        self.layout = qtw.QFormLayout()
        self.layout.addRow(self.title_label, self.title_input)
        self.layout.addRow(self.text_label, self.text_input)
        self.layout.addRow(self.discard, self.enter)
        self.setLayout(self.layout)
        

        self.error_msg = qtw.QMessageBox()
        self.error_msg.setIcon(qtw.QMessageBox.Critical)
        self.error_msg.setWindowTitle("Error occured!")
        
        self.success_completed = qtw.QMessageBox()
        self.success_completed.setIcon(qtw.QMessageBox.Information)
        self.success_completed.setWindowTitle("successfully completed")
        self.success_completed.setText("mission completed")

    def post_note(self):
        title = self.title_input.text()
        text = self.text_input.toPlainText()
        if not title or not text:
            self.error_msg.setText("Please enter the title and the text to continue")
            return self.error_msg.exec()
        data ={
            "title": title,
            "text": text
            }
        try:
            responce = requests.post(self.url+"notes", data=data)
            if responce.status_code ==201 :
                self.title_input.clear()
                self.text_input.clear()
                return self.success_completed.exec()
            else:
                self.error_msg.setText("Some thing occurred Please try later!")
                return self.error_msg.exec()
        except :
            raise 
    def disc(self):
        self.title_input.clear()
        self.text_input.clear()





    def read_style(self, stylename, wid):
        with open(stylename, "r") as f:
            wid.setStyleSheet(f.read())

def main():
    app = qtw.QApplication(sys.argv)
    mainwindow = Window()
    mainwindow.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()

