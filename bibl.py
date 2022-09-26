import os  # Импортируем библиотку для работы с ОС

class Book:
    total = 0
    def __init__(self):
        self.title = input('Название: ')
        self.year = input('Год: ')
        self.author = input('Автор: ')
        self.total += 1

    def __str__(self):
        return f'{self.total} - {self.title}, {self.year}, {self.author}'

class Library(Book):
    super(Library, self).()
    books = {}

    # def __init__(self):
    #     self.books = {}

    # def __str__(self):
    #     result = ''
    #     for item in self.books.values():
    #         item_list = str(item[1]).split(',')
    #         result += (f'{item[0]} - {item_list[0]}\n')
    #         # result.append(f'{str(item[0])} - {str(item[1])} экз.')
    #     return str(result)

    def add(self, book):
        self.books[super().total] = f'{super().title}'

    def removeAt(self, num):
        pass

    def printAll(self):
        pass

    def printAt(self, num):
        pass

if __name__ == '__main__':
    # book = Book()
    lib = Library()
    select = None
    b = {}
    i = 0
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
        print()

        clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Назначили ссылку на метод в поле clear
        clear()  # Вызываем при необходимости очистки консоли

        # exit
        if select == '0':
            print('Пока.')

        # добавить
        elif select == '1':
            i += 1

            b[i] = Book()
            lib.add(b[i])

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

        print(lib)

