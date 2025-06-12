import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from sonic import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(lambda: self.alterar_imagem("Sonic"))
        self.ui.pushButton_3.clicked.connect(lambda: self.alterar_imagem("Amy Rose"))
        self.ui.pushButton_4.clicked.connect(lambda: self.alterar_imagem("Metal Sonic"))
        self.ui.pushButton_5.clicked.connect(lambda: self.alterar_imagem("Shadow"))
        self.ui.pushButton_6.clicked.connect(lambda: self.alterar_imagem("Silver"))
       
    def alterar_imagem(self, nome_do_personagem):
        caminho_imagem = {
            "Sonic": "img/sonic.png",
            "Amy Rose": "img/amy.png",
            "Metal Sonic": "img/metal.png",
            "Shadow": "img/shadow.png",
            "Silver": "img/silver.png",
        }

        if nome_do_personagem in caminho_imagem:
            pixmap = QPixmap(caminho_imagem[nome_do_personagem])
            self.ui.label_2.setPixmap(pixmap)
            self.ui.label_2.setScaledContents(True)
        else:
            print(f"Imagem para {nome_do_personagem} não encontrada!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())