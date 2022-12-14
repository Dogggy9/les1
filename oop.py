class Building:
    def __init__(self, w, c, n=0):
        self.what = w
        self.color = c
        self.numbers = n
        self.mwhere(n)

    def mwhere(self, n):
        if n <= 0:
            self.__where = "отсутствуют"
        elif 0 < n < 100:
            self.__where = "малый склад"
        else:
            self.__where = "основной склад"

    def where(self):
        return self.__where, self.what, self.color, self.numbers

    def __str__(self):
        return f'{self.__where}, {self.what}, {self.color}, {self.numbers}'

    def plus(self, p):
        self.numbers = self.numbers + p
        self.mwhere(self.numbers)

    def minus(self, m):
        self.numbers = self.numbers - m
        self.mwhere(self.numbers)


m1 = Building("доски", "белые", 50)
m2 = Building("доски", "коричневые", 300)
m3 = Building("кирпичи", "белые")

print(m1.what, m1.color, m1.where())
print(m2.what, m2.color, m2.where())
print(m3.what, m3.color, m3.where())

m1.plus(500)
print(m1.where())
