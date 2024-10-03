def Cardcod(first_day, first_data, first_temperature, second_day, second_data, second_temperature,
            third_day, third_data, third_temperature, first_night_temperature, second_night_temperature, third_night_temperature):
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
    import sys
    from PyQt6.QtGui import QDesktopServices
    from PyQt6.QtGui import QDesktopServices, QIcon  # Импортируем QIco
    from PyQt6.QtCore import QUrl

    class Card(QWidget):
        def __init__(self, title, description, description2):
            super().__init__()
            self.title = title
            self.description = description
            self.description2 = description2
            self.initUI()

        def initUI(self):
            vbox = QVBoxLayout()

            # Добавляем заголовок
            title_label = QLabel(self.title)
            title_label.setStyleSheet("font-size: 15px; font-weight: bold;")
            vbox.addWidget(title_label)

            # Добавляем описание
            desc_label = QLabel(self.description)
            desc_label.setStyleSheet("font-size: 15px;")
            vbox.addWidget(desc_label)

            desc_label = QLabel(self.description2)
            desc_label.setStyleSheet("font-size: 12px;")
            vbox.addWidget(desc_label)

            self.setLayout(vbox)

    def Cardcod(first_day, first_data, first_temperature, second_day, second_data, second_temperature,
                third_day, third_data, third_temperature, first_night_temperature, second_night_temperature, third_night_temperature):
        # Создаем экземпляры карточек и заполняем их данными
        global cards
        cards = []
        card1 = Card(f"Сегодня {first_day} {first_data}", f"{first_temperature}", f"{first_night_temperature}")
        cards.append(card1)
        card2 = Card(f"Завтра {second_day} {second_data}", f"{second_temperature}", f"{second_night_temperature}")
        cards.append(card2)
        card3 = Card(f"После завтра {third_day} {third_data}", f"{third_temperature}", f"{third_night_temperature}")
        cards.append(card3)

        # Размещаем карточки на странице
        hbox = QHBoxLayout()
        for card in cards:
            hbox.addWidget(card)

        # Создаем длинную кнопку
        button = QPushButton('Прогноз на сайте')
        button.clicked.connect(open_url)
        button.setStyleSheet("QPushButton { background-color: #555555; color: #FFFFFF; }")
        button.setFixedHeight(20)  # Установите фиксированную высоту для кнопки
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(button)

        # Создаем главное окно и устанавливаем макет
        widget = QWidget()
        widget.setLayout(vbox)
        widget.setWindowTitle("Погода")  # Устанавливаем заголовок окна
        widget.setWindowIcon(QIcon("img/sun.JPG"))  # Устанавливаем иконку окна
        widget.setFixedSize(500, 200)  # Увеличьте размер окна, если необходимо

        # Возвращаем объект окна
        return widget

    def open_url():
        # Открываем URL-адрес в браузере
        url = 'https://www.gismeteo.ru/weather-barnaul-4720'
        QDesktopServices.openUrl(QUrl(url))

    # Создаем приложение и главное окно в глобальной области видимости
    app = QApplication(sys.argv)

    # Установка темной темы
    app.setStyleSheet("QWidget { background-color: #333333; color: #FFFFFF; }"
                      "QPushButton { background-color: #555555; color: #FFFFFF; }")
    widget = Cardcod(first_day, first_data, first_temperature, second_day, second_data, second_temperature,
                     third_day, third_data, third_temperature, first_night_temperature, second_night_temperature, third_night_temperature)

    # Отображаем главное окно и запускаем приложение
    widget.show()

    sys.exit(app.exec())
