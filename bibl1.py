import os  # Импортируем библиотку для работы с ОС

class Book:
    total = 0
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
        self.total += 1

    def __str__(self):
        return f'{self.total} - {self.title}, {self.year}, {self.author}'


class Library(Book):
    def __init__(self, title, year, author):
        Book.__init__(self, title, year, author)

    books = []

    def add(self, title, year, author):

        Book(title, year, author)





if __name__ == '__main__':
    # book = Book()
    # lib = Library()
    select = None
    b = {}
    i = 0
    books = 0
    while select != '0':
        print('''
        Что будем делать?
        0 - Выйти
        1 - Добавить книгу
        2 - Посмотреть список
        3 - Удалить книгу
        4 - Информация о книге
        ''')
        select = input(">>: ")

        clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Назначили ссылку на метод в поле clear
        clear()  # Вызываем при необходимости очистки консоли

        # exit
        if select == '0':
            print('Пока.')

        # добавить
        elif select == '1':
            books += 1
            title = input('Название: ')
            year = input('Год: ')
            author = input('Автор: ')
            b[books] = Library(title, year, author)

        # список
        elif select == '2':
            pass

        # найти
        elif select == '3':
            pass

        # удалить
        elif select == '4':
            pass

        # неправильный ввод
        else:
            print('\nНеправильный ввод!')

        # print(lib)
