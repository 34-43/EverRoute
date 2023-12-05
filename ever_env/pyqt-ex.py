from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
import sys
import bruteforce

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.radio_button_1 = QRadioButton("옵션 1", self)
        self.radio_button_2 = QRadioButton("옵션 2", self)
        self.result_button = QPushButton("결과 보기", self)
        self.result_button.clicked.connect(self.on_result_button_click)

        self.graphics_view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.scene)

        layout = QVBoxLayout(self)
        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)
        layout.addWidget(self.result_button)
        layout.addWidget(self.graphics_view)

    def on_result_button_click(self):
        selected_option = "옵션 1" if self.radio_button_1.isChecked() else "옵션 2"
        print(f"선택한 옵션: {selected_option}")

        # 여기에서 내부 프로그램 실행 및 결과를 가져와서 처리
        # 예제로 좌표 데이터를 받아 시각화
        self.visualize_coordinates([(50, 50), (100, 100)])

    def visualize_coordinates(self, coordinates):
        self.scene.clear()
        for x, y in coordinates:
            ellipse = QGraphicsEllipseItem(x, y, 10, 10)
            self.scene.addItem(ellipse)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
