class Book():
    '''книга'''

    def __init__(self):
        self.titl = input('Название? ')
        self.year = input('Год издания? ')
        self.autor = input('Автор? ')
        self.__nomer = Book.total
        # self.__w = 300
        # self.hunger = 1

    def __str__(self):
        res = f'Книга\n номер: {self.nomer}\n название: {self.titl}'
        return res

    def add(self):
        print(self.name, ': Мяу')

    @property
    def weight(self):
        return self.__w

    def find(self):
        if self.hunger == 5:
            print('Кошка не голодная')
        else:
            self.hunger += 1
            self.__w += 30
            print('Мур!')

    def look_list(self):
        self.add()
        self.__w -= 5
        if self.hunger > 0:
            self.hunger -= 1
        else:
            self.hunger = 1

class Library():
    '''библиотека'''

    total = 0

    @staticmethod
    def count():
        print(f'Всего книг {Library.total}')

    def __init__(self):
        print('Добавили новую книгу!')
        Library.total += 1


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
            book.add()

        # найти
        elif select == '3':
            book.find()

        # список
        elif select == '2':
            book.look_list()
        elif select == '4':
            print('Вес: ', book.weight, ' гр.')

        # неправильный ввод
        else:
            print('\nНеправильный ввод!')

main()
