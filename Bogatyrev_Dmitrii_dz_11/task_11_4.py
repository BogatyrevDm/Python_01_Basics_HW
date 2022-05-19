# В этом файле сделаю задания 4-6, потому что они продолжают друг друга
from abc import ABC, abstractmethod


class Storage():
    def __init__(self, name):
        # Имя склада
        self.name = name
        # Словарь с оборудованием
        self.storage_list = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @staticmethod
    def check_data(number):
        """
        Процедура проверяет, передано число или строка
        :param number: переданное значение
        """
        try:
            if not str(number).isdigit():
                raise TypeError("Переданное значение не является числом!")
        except TypeError as err:
            print(err)
            return False
        else:
            return True

    def put_into_storage(self, office_equipment, number):
        """
        Процедура помещает переданное оборудование на склад
        :param office_equipment: Офисное оборудование
        :param number: Количество оборудования
        """
        if not Storage.check_data(number):
            return

        # Поищем оборудование в словаре, вернем количество, если нашли, 0 - если нет
        result = self.storage_list.get(office_equipment, 0)
        # Увеличим результат на переданное количество
        result += number
        # Поместим в словарь
        self.storage_list[office_equipment] = result
        # Выведем информационное сообщение
        print(f'На склад {self.name} поступило {number} шт. {office_equipment.name}')
        print(f'Всего {office_equipment.name} на складе: {result} шт. ')

    def remove_from_storage(self, office_equipment, number):
        """
        Процедура удаляет оборудование со склада
        :param office_equipment: Офисное оборудование
        :param number: Количество оборудования
        """
        result = self.storage_list.get(office_equipment)
        # Оборудование есть на складе
        if result is not None:
            # Списываем все оборудование
            if result == number:
                self.storage_list.pop(office_equipment)
                print(f'Со склада {self.name} списано {number} шт. {office_equipment.name}')
            # Списываем только требуемое количество
            elif result > number:
                self.storage_list[office_equipment] -= number
                print(f'Со склада {self.name} списано {number} шт. {office_equipment.name}')
            # Сообщаем, что количества не достаточно
            else:
                print(f'На складе {self.name} не достаточно {office_equipment.name}')
        # Оборудования нет на складе, сообщим об этом
        else:
            print(f'На складе {self.name} отсутствует {office_equipment.name}')

    def show_content(self):
        """
        Процедура выводит на экран содержимое склада
        """
        print(f'Список офисного оборудования на складе {self.name} :')
        for key, value in self.storage_list.items():
            print(f'{key}: {value} шт')


class OfficeEquipmentAbs(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass


class OfficeEquipment(OfficeEquipmentAbs):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.name}'


class Printer(OfficeEquipment):
    def __init__(self, name, printer_type, is_color_avaliable):
        super().__init__(name)
        self.printer_type = printer_type
        self.is_color_avaliable = is_color_avaliable


class Scanner(OfficeEquipment):

    def __init__(self, name, scanner_type, scanning_speed):
        super().__init__(name)
        self.scanner_type = scanner_type
        self.scanning_speed = scanning_speed


class CopyMachine(OfficeEquipment):
    def __init__(self, name, number_of_copies):
        super().__init__(name)
        self.number_of_copies = number_of_copies


# Эмуляция работы пользователя
first_scanner = Scanner("HP ScanJet Pro 3000 s4", "Протяжный", 40)
second_scanner = Scanner("HP ScanJet Pro 4500 fn1", "Планшетный", 30)
first_printer = Printer("Canon Pixma TS304", "Струйный", True)
second_printer = Printer("HP M111a", "Лазерный", False)
first_copy_machine = CopyMachine("Canon imageRUNNER 2206", 999)

first_storage = Storage("First storage")
first_storage.put_into_storage(first_scanner, 5)
first_storage.put_into_storage(second_scanner, 10)
first_storage.put_into_storage(first_scanner, 7)

first_storage.show_content()

first_storage.remove_from_storage(first_printer, 5)
first_storage.remove_from_storage(first_scanner, 9)
first_storage.remove_from_storage(second_scanner, 15)

first_storage.show_content()

# Передана строка - будет сообщение об ошибке
first_storage.put_into_storage(first_scanner, "ffddfdf")
