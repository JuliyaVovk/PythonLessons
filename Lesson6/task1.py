"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = 'Red'

    @property
    def color(self):
        return self.__color

    def running(self):
        if self.__color == 'Red':
            sleep(7)
            self.__color = 'Yellow'
        elif self.__color == 'Yellow':
            sleep(2)
            self.__color = 'Green'
        else:
            sleep(5)
            self.__color = 'Red'


traffic = TrafficLight()
expected_color = 'Red'
for _ in range(10):
    color = traffic.color
    if color != expected_color:
        print(f'Ошибка! Ожидался {expected_color}, получен {color}')
    print(color)
    traffic.running()
    if expected_color == 'Red':
        expected_color = 'Yellow'
    elif expected_color == 'Yellow':
        expected_color = 'Green'
    else:
        expected_color = 'Red'
