if __name__ == "__main__":
    class Book():
        def __init__(self, author: str, name: str, pages: int, your_pages: int = 0):
            '''
            Создание и подготовка к работе обьекта 'Книга'
            :param author: автор книги
            :param name: название книги
            :param pages: количество страниц
            :your pages: количество страниц, которые вы уже прочли
            Примеры:
            book_1 = Book('Ф.М. Достоевский', 'Преступление и наказание', 95, 41)
            '''
            if not isinstance(author, str):
                raise TypeError("Must be str!")
            self._author = author

            if not isinstance(name, str):
                raise TypeError("Must be str!")
            self._name = name

            if not isinstance(pages, int):
                raise TypeError("Must be int!")
            if pages <= 0:
                raise ValueError("Pages > 0!")
            self._pages = pages

            if not isinstance(your_pages, int):
                raise TypeError("Must be int!")
            if your_pages < 0 or your_pages >= pages:
                raise ValueError("You couldn't read more pages than there are in the book/Your peges >= 0!")
            self._your_pages = your_pages

        @property
        def author(self) -> str:
            '''Возврашает автора книги'''
            return self._author

        @property
        def name(self) -> str:
            '''Возврашает название книги'''
            return self._name

        @property
        def pages(self) -> int:
            '''Возврашает количество страниц в книге'''
            return self._pages

        @property
        def your_pages(self) -> int:
            '''Возврашает количество страниц в книге, которое вы уже прочли'''
            return self._your_pages

        def increase_number_of_pages_read(self, read_pages: int) -> None:
            '''
            Увеличение количества прочитанных страниц
            :param read_pages: Количество прочитанных страниц
            Пример:
            book_1 = Book('Достоевский Ф.М', 'Преступление и наказание', 500)
            book_1.number_of_pages_read(200)
            '''
            if not isinstance(read_pages, int):
                raise TypeError('Number of pages read must be int')
            if read_pages < 0:
                raise ValueError('Number of pages read can"t be < 0')
            if self.your_pages + read_pages > self.pages:
                raise ValueError('You couldn"t read that much pages')
            self._your_pages += read_pages

        def __str__(self):
            return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

        def __repr__(self):
            return f"{self.__class__.__name__}(author={self.author!r}, name={self.name!r}, pages={self.pages!r})"


    class PaperBook(Book):
        def __init__(self, author: str, name: str, pages: int, cover: str, publishing_house: str, your_pages: int = 0):
            '''
            Созадние и подготовка к работе объекта 'Бумажная книга', наследующего объект 'Книга'
            :param author: автор книги
            :param name: название книги
            :param pages: количество страниц
            :param cover: обложка книги
            :param publishing_house: издательство
            Примеры:
            paper_book_1 = PaperBook('Ф.М. Достоевский', 'Преступление и наказание', 95, 'Твердая обложка', 'Московский книжный дом')
            '''
            super().__init__(name, author, pages, your_pages)
            if not isinstance(cover, str):
                raise TypeError("Must be str!")
            self._cover = cover
            if not isinstance(publishing_house, str):
                raise TypeError("Must be str!")
            self._publishing_house = publishing_house

        @property
        def cover(self) -> str:
            return self._cover

        @property
        def publishing_house(self) -> str:
            return self._publishing_house

        def __repr__(self):
            return f"{self.__class__.__name__}(author={self.author!r}, name={self.name!r}, pages={self.pages!r}, cover={self.cover!r}, publishing_house={self.publishing_house!r})"


    class EBook(Book):
        def __init__(self, author: str, name: str, pages: int, brand: str, your_pages: int = 0):
            '''
            Созадние и подготовка к работе объекта 'Электронная книга', наследующего объект 'Книга'
            :param author: автор книги
            :param name: название книги
            :param pages: количество страниц
            :param brand: бренд книги
            :param publishing_house: издательство
            Примеры:
            e_book_1 = Ebook('Ф.М. Достоевский', 'Преступление и наказание', 95, 'Apple')
            '''
            super().__init__(name, author, pages, your_pages)
            if not isinstance(brand, str):
                raise TypeError("Must be str!")
            self._brand = brand
            self._charge = 0

        @property
        def brand(self) -> str:
            '''Возвращает бренд книги'''
            return self._brand

        @property
        def charge(self) -> str:
            '''Возвращает зарядку'''
            return self._charge

        @charge.setter
        def charge(self, charge: int) -> None:
            '''Устанавливает зарядку'''
            if not isinstance(charge, int):
                raise TypeError('Must be int')
            if charge < 0 or charge > 100:
                raise ValueError('0<=charge<=100')
            self._charge = charge

        def charge_ebook(self, new_charge: int) -> None:
            '''
            Зарядка электронной книги
            :param new_charge: на сколько процентов хотим зарядить(в добавок к уже имеющимся)
            Примеры:
            e_book_1 = PaperBook('Ф.М. Достоевский', 'Преступление и наказание', 95, 'Apple')
            e_book_1.charge_ebook(100)
            '''
            if not isinstance(new_charge, int):
                raise TypeError('Must be int!')
            if new_charge < 0 or new_charge > 100 or new_charge + self.charge > 100:
                raise ValueError('Incorrect value for param new_charge')
            book1._charge += new_charge

        def __repr__(self):
            return f"{self.__class__.__name__}(author={self.author!r}, name={self.name!r}, pages={self.pages!r}, brand={self.brand!r})"


    pass
