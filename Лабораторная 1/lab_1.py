import doctest


class Chair:
    def __init__(self, material: str, number_of_legs: int, taken: bool):
        """
        Создание и подготовка к работе объекта "Стул"

        :param material: Материал стула
        :param number_of_legs: Количество ножек стула
        :param taken: Занят ли стул

        Пример:
        >>> chair = Chair("wood", 4, False)  #инициализация экземпляра класса
        """

        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.material = material

        if not isinstance(number_of_legs, int):
            raise TypeError("Количество ножек должно быть типа int")
        if number_of_legs < 3:
            raise ValueError("У стула не может быть меньше 3 ножек")
        self.number_of_legs = number_of_legs

        if not isinstance(taken, bool):
            raise TypeError("Занятость стула должна быть типа bool")
        self.taken = taken

    def is_chair_taken(self) -> bool:
        """
        Функция проверяет занят ли стул

        :return: Является ли стул занятым

        Пример:
        >>> chair = Chair("wood", 4, False)
        >>> chair.is_chair_taken()
        """
        ...

    def exterminate_chair(self) -> None:
        """
        Функция экстерминирует стул и его возможного владельца

        Пример:
        >>> chair = Chair("wood", 4, False)
        >>> chair.exterminate_chair()
        """
        self.material = None
        self.number_of_legs = None
        self.taken = None


class Friend:
    def __init__(self, age: int, candies: int, imaginary: bool):
        """
        Создание и подготовка к работе объекта "Друг"

        :param age: Возраст друга
        :param candies: Количество конфет у друга
        :param imaginary: Воображаемый ли друг

        Пример:
        >>> friend = Friend(21, 7, False)  # инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

        if not isinstance(candies, int):
            raise TypeError("Количество конфет должно быть типа int")
        if candies < 5:
            raise ValueError("Не жадничай. Дай 5 или больше конфет")
        self.candies = candies

        if not isinstance(imaginary, bool):
            raise TypeError("Друг либо воображаемый, либо нет")
        self.imaginary = imaginary

    def give_candies(self, num_of_candies: int) -> None:
        """
        Функция даёт другу конфеты

        :param num_of_candies: Количество даваемых конфет

        Пример:
        >>> friend = Friend(21, 7, False)
        >>> friend.give_candies(2)
        """
        if not isinstance(num_of_candies, int):
            raise TypeError("Количество конфет должно быть типа int")
        if num_of_candies < 1:
            raise ValueError("Дай хотя бы одну конфету")
        self.candies += num_of_candies

        ...

    def ask_candy(self) -> int:
        """
        Функция просит у друга конфету
        Если у друга есть конфеты, он отдаёт одну с шансом 50%

        :return: Количество конфет, которые отдал друг (1 или 0)

        Пример:
        >>> friend = Friend(21, 7, False)
        >>> friend.ask_candy()
        """
        ...


class Cat:
    def __init__(self, name: str, breed: str):
        """
        Создание и подготовка к работе объекта "Кот"

        :param name: Кличка кота
        :param breed: Порода кота

        Пример:
        >>> cat = Cat("Charly", "cat")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть типа str")
        if name == "":
            raise ValueError("Имя не должно быть пустым")
        self.name = name

        if not isinstance(breed, str):
            raise TypeError("Порода кота должна быть типа str")
        if breed == "":
            raise ValueError("Порода не должна быть пустым")
        self.breed = breed

    def feed(self) -> None:
        """
        Функция кормящая кота

        Пример:
        >>> cat = Cat("Charly", "cat")
        >>> cat.feed()
        """
        ...

    def play(self, minutes: int) -> None:
        """
        Функция для игры с котом

        :param minutes: Количество минут игры с котом

        Пример:
        >>> cat = Cat("Charly", "cat")
        >>> cat.play(5)
        """
        if not isinstance(minutes, int):
            raise TypeError("Время игры должно быть типа int")
        if not minutes > 0:
            raise ValueError("Поиграй хотя бы минутку!")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров из документации
