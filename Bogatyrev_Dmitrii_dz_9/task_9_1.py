from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = "Red"

    def running(self):
        # создадим словарь в котором ключи - цвета, значения - продолжительность в секундах
        colors_dict = {"Red": 4, "Yellow": 2, "Green": 3}
        # переберем словарь
        for key, value in colors_dict.items():
            # поменяем ключ
            self.__color = key
            # выведем на экран
            self.__print_color(value)

    def __print_color(self, time):
        # выведем сообщение
        print(f'{self.__color} {time}')
        # заснем на нужное количество секунд
        sleep(time)


if __name__ == '__main__':
    traffic = TrafficLight()

    traffic.running()
