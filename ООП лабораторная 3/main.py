class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def author(self) -> str:
        '''Возвращает имя автора'''
        return self._author

    @property
    def name(self) -> str:
        '''Возвращает название книги'''
        return self._name

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property
    def pages(self) -> int:
        '''Возвращает кол-во старниц'''
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        '''Устанавливает кол-во страниц'''
        if not isinstance(new_pages, int):
            raise TypeError('Количество страниц должно быть целым')
        if new_pages <= 0:
            raise ValueError('Количество страниц должно быть положительным')
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Кол-во страниц {self.pages}."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self) -> float:
        '''Возвращает длительность'''
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        '''Устанавливает кол-во страниц'''
        if not isinstance(new_duration, float):
            raise TypeError('Введите длительность в формате float')
        if new_duration <= 0:
            raise ValueError('Длительность должна быть положительной')
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}."