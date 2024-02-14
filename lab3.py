class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name        # Базовая инициализация name и autor
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
        # текстовое представление книги

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
        # 'сырые' параметры книги

    @property                               # getter для name
    def name(self):
        return self._name

    @property                               # getter для author
    def author(self):
        return self._author


class PaperBook(Book):
    """ Класс бумажной книги. """
    MAX_PAGES = 1000    # максимальное число страниц в бумажной книге

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)   # Базовая инициализация name и autor
        self.pages = pages              # Производная инициализация pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, type=paper, pages={self.pages!r})"
        # к параметрам бумажной книги добавляем количество страниц

    @property                           # getter для pages
    def pages(self):
        return self._pages

    @pages.setter                       # setter для pages
    def pages(self, pages_value):
        if not isinstance(pages_value, int):
            raise ValueError("Число страниц должно быть целым числом")
        if pages_value < 0 or pages_value > self.MAX_PAGES:
            raise ValueError(f"Число страниц должно быть в диапазоне от '0' до '\f{self.MAX_PAGES}'")

        self._pages = pages_value


class AudioBook(Book):
    """ Класс аудиокниги. """
    MAX_DURATION = 512      # максимальная продолжительность аудиокниги

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Базовая инициализация name и autor
        self.duration = duration        # Производная инициализация duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, type=audio, duration={self.duration!r})"
        # к параметрам аудиокниги добавляем продолжительность

    @property                           # getter для duration
    def duration(self):
        return self._duration

    @duration.setter                    # setter для duration
    def duration(self, duration_value):
        if not isinstance(duration_value, float):
            raise ValueError("Продолжительность должна быть типа 'float'")
        if duration_value < 0 or duration_value > self.MAX_DURATION:
            raise ValueError(f"Продолжительность должна быть от '0' до '\f{self.MAX_DURATION}'")

        self._duration = duration_value


"""
# пример создания книг всех трех классов

book = Book("One", "JohnSmithFirst")
paper_book = PaperBook("Two", "JohnSmithSecond", 753)
audio_book = AudioBook("Three", "JohnSmithThird", 84.36)

print(book, paper_book, audio_book, sep='\n')
print(repr(book), repr(paper_book), repr(audio_book), sep='\n')
"""