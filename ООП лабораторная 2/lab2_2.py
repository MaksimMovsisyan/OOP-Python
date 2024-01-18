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

# TODO написать класс Library
class Library:
    def __init__(self, books = []):
        self.books = books
        self.count_of_books = len(books)
    def get_next_book_id(self):
        self.count_of_books += 1
        return self.count_of_books

    def get_index_by_book_id(self, id_ : int):
        for i,k in enumerate(self.books):
            if id_ == i+1:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")






if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
