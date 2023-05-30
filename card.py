def Cardcod(first_day, first_data, first_temperature, second_day, second_data ,second_temperature, 
        third_day , third_data, third_temperature,first_night_temperature,second_night_temperature,third_night_temperature ):
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
    import sys
    from PyQt6.QtGui import QDesktopServices
    from PyQt6.QtCore import QUrl

    class Card(QWidget):
        def __init__(self, title, description):
            super().__init__()
            self.title = title
            self.description = description
            self.initUI()

        def initUI(self):
            vbox = QVBoxLayout()

            # Добавляем заголовок
            title_label = QLabel(self.title)
            title_label.setStyleSheet("font-size: 30px; font-weight: bold;")
            vbox.addWidget(title_label)

            # Добавляем описание
            desc_label = QLabel(self.description)
            desc_label.setStyleSheet("font-size: 40px;")
            vbox.addWidget(desc_label)

            # Добавляем кнопку
            button = QPushButton('Прогноз на сайте')
            button.clicked.connect(self.open_url)
            button.setStyleSheet("QPushButton { background-color: #555555; color: #FFFFFF; }")
            vbox.addWidget(button)

            self.setLayout(vbox)

        def open_url(self):
            # Открываем URL-адрес в браузере
            url = 'https://www.gismeteo.ru/weather-barnaul-4720'
            QDesktopServices.openUrl(QUrl(url))

    def Cardcod(first_day, first_data, first_temperature, second_day, second_data ,second_temperature, 
        third_day , third_data, third_temperature,first_night_temperature,second_night_temperature,third_night_temperature ):
        # Создаем экземпляры карточек и заполняем их данными
        global cards
        cards = []
        card1 = Card("Сегодня"f"{first_day} {first_data}", f"{first_temperature} " f"{first_night_temperature}")
        cards.append(card1)
        card2 = Card("Завтра"f"{second_day} {second_data}", f"{second_temperature} " f"{second_night_temperature}" )
        cards.append(card2)
        card3 = Card("После завтра"f"{third_day} {third_data}", f"{third_temperature} "f"{third_night_temperature}" )
        cards.append(card3)

        # Размещаем карточки на странице
        hbox = QHBoxLayout()
        hbox.addWidget(card1)
        hbox.addWidget(card2)
        hbox.addWidget(card3)

        # Создаем главное окно и устанавливаем макет
        widget = QWidget()
        widget.setLayout(hbox)

        widget.setFixedSize(800, 600)
        # Возвращаем объект окна
        return widget

    # Создаем приложение и главное окно в глобальной области видимости
    app = QApplication(sys.argv)

    # Установка темной темы
    app.setStyleSheet("QWidget { background-color: #333333; color: #FFFFFF; }"
                    "QPushButton { background-color: #555555; color: #FFFFFF; }")
    widget = Cardcod(first_day, first_data, first_temperature, second_day, second_data ,second_temperature, 
        third_day , third_data, third_temperature,first_night_temperature,second_night_temperature,third_night_temperature )


    # Отображаем главное окно и запускаем приложение
    widget.show()
    
    sys.exit(app.exec())
    print("Hellow")