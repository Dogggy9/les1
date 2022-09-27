import os


class Book():
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.title}, {self.year}, {self.author}'


class Library():
    # total = 0
    books = []

    def add(self, book):
        # self.total += 1
        self.books.append(f'{str(book)}')

    def removeAt(self, b):
        self.books.pop(b)

    def printAll(self):
        a = []
        for num, item in enumerate(self.books, 1):
            a.append(str(num) + ' - ' + item)
        self.books1 = '\n'.join(a)

        return self.books1

    def printAt(self, b):
        pass


if __name__ == '__main__':
    select = None
    b = {}
    lib = Library()
    books = [('Сам', '2022', 'Пушкин'), ('Ты', '2021', 'КР')]
    for n, book in enumerate(books, 1):
        b[n] = Book(*book)
        lib.add(b[n])
    i = len(books)
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
            i += 1
            title = input('название')
            year = input('год')
            author = input('автор')
            b[i] = Book(title, year, author)
            lib.add(b[i])
        # список
        elif select == '2':
            print(lib.printAll())
        # Информация о книге
        elif select == '4':
            num_book = input('Введите номер книги: ')  # printAt
            pass
        # удалить
        elif select == '3':
            num_book = int(input('Введите номер книги: '))  # removeAt
            if 0 < num_book <= len(b):
                del b[num_book]
                lib.removeAt(num_book - 1)
            else:
                print('Книги с таким номером нет')
        # неправильный ввод
        else:
            print('\nНеправильный ввод!')
