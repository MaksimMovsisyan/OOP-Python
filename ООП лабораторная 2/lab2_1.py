from typing import Union
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        '''
        Создание и подготовка к работе обьекта 'Книга'
        :param id: идентификатор книги
        :param name: название книги
        :param pages: количество страниц
        Примеры:
        book_1 = Book(1, "Азбука", 95)
        '''

        if not isinstance(id_, int):
            raise TypeError("Must be int!")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Must be str!")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Must be int!")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
