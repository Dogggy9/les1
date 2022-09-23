class Book():
    '''книга'''

    def __init__(self):
        self.titl = input('Название? ')
        self.year = input('Год издания? ')
        self.autor = input('Автор? ')
        Library(self.titl, self.year, self.autor)

class Library():
    '''библиотека'''

    total = 0
    dic = {}

    @staticmethod
    def count():
        print(f'Всего книг {Library.total}')

    def __init__(self, titl, year, autor):
        print('Добавили новую книгу!')
        Library.total += 1
        self.dic[Library.total] = titl, year, autor


    def __setitem__(self, key, value):
        '''присвоение по индексу self[key] = value'''
        pass

    def __getitem__(self, item):
        '''доступ по индексу self[item]'''
        pass

    def __delitem__(self, key):
        '''удаление по индексу del self[key]'''
        pass

    def __str__(self):
        print(self.dic)


def main():
    book = Book()
    select = None
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

        # exit
        if select == '0':
            print('Пока.')

        # добавить
        elif select == '1':
            Book()

        # список
        elif select == '2':
            print(Library.dic)

        # найти
        elif select == '3':
            Library.find()

        # удалить
        elif select == '4':
            pass

        # неправильный ввод
        else:
            print('\nНеправильный ввод!')



main()
