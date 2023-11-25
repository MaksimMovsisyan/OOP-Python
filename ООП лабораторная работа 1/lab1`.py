# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class Book():
    def __init__(self, author: Union[str], pages: Union[int], raiting: Union[int, float]):
        '''
        Создание и подготовка к работе обьекта 'Книга'

        :param author: Автор книги
        :param pages: Кол-во страниц в книге
        :param raiting: Рейтинг книги(по 10-ти бальной шкале)

        Примеры:
        book_1 = Book('Достоевский Ф.М', 650, 9.5)
        '''

        if not isinstance(author, str):
            raise TypeError("Введите имя автора в формате строки")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым")
        self.pages = pages

        if not isinstance(raiting, (int, float)):
            raise TypeError("Рейтинг - действительное число ")
        if raiting < 0 or raiting > 10:
            raise ValueError("Рейтинг выставляется по 10ти бальной шкале")
        self.raiting = raiting

    def number_of_pages_read(self, read_pages: Union[int]) -> None:
        '''
        Увеличение количества прочитанных страниц
        :param read_pages: Количество прочитанных страниц
        Пример:
        book_1 = Book('Достоевский Ф.М', 650, 9.5)
        book_1.number_of_pages_read(200)
        '''
        if not isinstance(read_pages, int):
            raise TypeError("Введите целое кол-во страниц")
        if read_pages > self.pages:
            raise ValueError("Неверное количество прочтенных страниц")
        ...
    def raiting_change(self, your_rait: Union[int, float]) -> None:
        '''
        Изменение рейтинга книги по 10ти бальной шкале
        :param your_rait: Ваш рейтинг этой книге
        Пример
        book_1 = Book('Достоевский Ф.М', 650, 9.5)
        book_1.raiting_change(9.6)
        '''
        if not isinstance(your_rait, (int, float)):
            raise TypeError("Рейтинг - действительное число")
        if your_rait<0 or your_rait>10:
            raise ValueError("Рейтинг выставляется по 10ти бальной шкале")
        ...

class Car():
    def __init__(self, brand: Union[str], fuel: Union[int]):
        '''
        Создание и подготовка к работе обьекта 'Мащина'

        :param brand: Марка автомобиля
        :param fuel: Запас топлива автомобиля

        Примеры:
        car_1 = Car('Мерседес', 56)
        '''

        if not isinstance(brand, str):
            raise TypeError("Введите марку машины в формате строки")
        self.brand = brand

        if not isinstance(fuel, int):
            raise TypeError("Кол-во бензина должно быть целым")
        if fuel<0 or fuel>100:
            raise ValueError("Бензобак машины обьмомо до 100 литров")
        self.fuel = fuel

    def car_refueling(self, add_fuel: Union[int]) -> None:
        '''
        Заправка автомобиля

        :param add_fuel: Кол-во добавленного топлива
        Пример
        car_1 = Car('Мерседес', 56)
        car_1.car_refueling(34)
        '''
        if not isinstance(add_fuel, int):
            raise TypeError("Кол-во бензина должно быть целым")
        if self.fuel + add_fuel > 100:
            raise ValueError("Бензобак машины обьмом до 100 литров")
        ...

    def tire_change(self, number_of_tires: Union[int]) -> None:
        '''
        Замена шин

        :param number_of_tires: Количество шин, которые желаем заменить
        Пример
        car_1 = Car('Мерседес', 56)
        car_1.tire_change(4)
        '''
        if not isinstance(number_of_tires, int):
            raise TypeError("Кол-во шин должно быть целым")
        if number_of_tires < 0 or number_of_tires > 4:
            raise ValueError("Вы можете заменить от 0 до 4 шин")
        ...

class Phone():
    def __init__(self, brand: Union[str], chargin_amount: Union[str]):
        '''
        Создание и подготовка к работе обьекта "Телефон"

        :param brand: Бренд телефона
        :param chargin_amount: Количество зарядки на телефоне

        Пример
        phone1 = Phone('Samsung', 54)
        '''

        if not isinstance(brand, str):
            raise TypeError("Введите бренд телефона в формате строки")
        self.brand = brand

        if not isinstance(chargin_amount, int):
            raise TypeError("Кол-во зарядки должно быть целым")
        if chargin_amount<0 or chargin_amount>100:
            raise ValueError("Бензобак машины обьмомо до 100 литров")
        self.chargin_amount = chargin_amount

        def phone_recharging(self, number_: Union[int]) -> None:
            '''
            Подзарядка вашего телефона

            :param number_: Количество процентов, на которое хотите зарядить

            Пример
            phone1 = Phone('iphone', 24)
            phone1.phone_recharging(45)
            '''

            if not isinstance(number_, int):
                raise TypeError('Кол-во процентов должно быть целым')
            if self.chargin_amount + number_ > 100:
                raise ValueError('Кол-во суммарной зарядки телефона не должно превосходить 100%')
            ...
        def phone_restart(self) -> None:
            '''
            Перезагрузка вашего телефона

            Пример
            phone1 = Phone('Samsung', 55)
            phone1.restart()
            '''
            ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
