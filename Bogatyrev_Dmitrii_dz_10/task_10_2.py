from abc import ABC, abstractmethod


class ClothesAbs(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass


class CoatAbs(ClothesAbs):
    @property
    @abstractmethod
    def size(self):
        pass

    @size.setter
    @abstractmethod
    def size(self, size):
        pass


class SuitAbs(ClothesAbs):
    @property
    @abstractmethod
    def hight(self):
        pass

    @hight.setter
    @abstractmethod
    def hight(self, hight):
        pass


class Coat(CoatAbs):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise ValueError("Wrong size type!")
        self.__size = size

    @property
    def fabric_consumption(self):
        return f'{self.size / 6.5 + 0.5}'


class Suit(SuitAbs):
    def __init__(self, name, hight):
        self.name = name
        self.hight = hight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def hight(self):
        return self.__hight

    @hight.setter
    def hight(self, hight):
        if type(hight) is not int:
            raise ValueError("Wrong hight type!")
        self.__hight = hight

    @property
    def fabric_consumption(self):
        return f'{self.hight * 2 + 0.3}'


first_coat = Coat("Пальто демисезонное", 10)
print(first_coat.fabric_consumption)

first_suit = Suit("Костюм выходной", 15)
print(first_suit.fabric_consumption)

# выдаст ValueError: Wrong hight type!
first_suit = Suit("Костюм повседневный", "15")
print(first_suit.fabric_consumption)
