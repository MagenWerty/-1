class Car:
    """Класс Автомобиль

    Является базовым для классов автомобилей разных видов

    number - государственный номер автомобиля; устанавливается один раз при создании автомобиля
    и в последствии не изменяется

    wheels - количество колкс автомобиля; неизменная характеристика

    max_fuel - объем топливного бака автомобиля; неизменная характеристика

    fuel - текущее количество топлива; изменяется от 0 до max_fuel"""

    def __init__(self, wheels: int, max_fuel: int, number: str):
        """Конструктор класса"""

        self._number = number
        self._wheels = wheels
        self._max_fuel = max_fuel
        self._fuel = 0

    def __str__(self):
        """'Сырые' данные класса"""

        return f"Автомобиль. Номер {self.number}"

    def __repr__(self):
        """Текстовое представление класса"""

        return f"{self.__class__.__name__}(type=N/A, number={self.number!r}, wheels={self.wheels!r}, max_fuel={self.max_fuel!r}, fuel={self.fuel!r})"

    def refuel(self, add_fuel: int) -> None:
        """Метод для дозаправки автомобиля на величину add_fuel"""
        ...

    def drive_1_km(self) -> None:
        """Метод, позволяющий проехать 1 км с соответствующим расходом топлива"""
        ...

    @property
    def number(self) -> str:
        """getter для номера автомобиля"""
        return self._number

    @property
    def wheels(self) -> int:
        """getter для количества колес автомобиля"""
        return self._wheels

    @property
    def max_fuel(self) -> int:
        """getter для объема топливного бака автомобиля"""
        return self._max_fuel

    @property
    def fuel(self) -> int:
        """getter для текущего уровня топлива"""
        return self._fuel

    @fuel.setter
    def fuel(self, new_fuel: int) -> None:
        """setter для текущего уровня топлива"""
        ...  # все необходимые проверки
        self._fuel = new_fuel


class Truck(Car):
    """Класс Грузовик

    Производный от класса Автомобиль
    Расширен конструктор класса. Исходные атрибуты сохранены, добавлены новые:

    capacity - грузоподъёмность грузовика; неизменная характеристика

    current_load - текущая загрузка грузовика; изменяется от 0 до capacity

    Унаследованы getter и setter для базовых атрибутов
    Унаследован метод refuel
    """

    def __init__(self, wheels: int, max_fuel: int, number: str, capacity: int):
        """Конструктор класса

        Конструктор расширен, добавлены новые атрибуты"""
        super().__init__(wheels, max_fuel, number)
        self._capacity = capacity
        self._current_load = 0

    def __str__(self):
        """Текстовое представление класса

        Метод перегружен, так как изменен тип автомобиля"""

        return f"Грузовик. Номер {self.number}"

    def __repr__(self):
        """'Сырые' данные класса

        Метод перегружен, так как изменен тип автомобиля"""

        return f"{self.__class__.__name__}(type=N/A, number={self.number!r}, wheels={self.wheels!r}, max_fuel={self.max_fuel!r}, fuel={self.fuel!r}), capacity={self.capacity!r}, current_load={self.current_load}"

    def drive_1_km(self) -> None:
        """Метод, позволяющий проехать 1 км с соответствующим расходом топлива

        Метот перегружен, так как изменен тип автомобиля, и теперь расход топлива расчитывается инымм способом"""
        ...

    @property
    def capacity(self) -> int:
        """getter для грузоподъёмности грузовика"""
        return self._capacity

    @property
    def current_load(self) -> int:
        """getter для текущей загрузки грузовика"""
        return self._current_load

    @current_load.setter
    def current_load(self, new_load) -> None:
        """setter для текущей загрузки грузовика"""
        ...  # все необходимые проверки
        self._current_load = new_load


if __name__ == "__main__":
    basicCar = Car(4, 50, "е634ср")
    childTruck = Truck(8, 720, "дбр596", 2500)

    print(basicCar, childTruck, sep="\n")
