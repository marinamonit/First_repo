
# Задание 1
class Publication:
    izdatelstvo = 'Litres'
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def display(self):
        print(f'{self.title} {self.author} {self.year}')
    @classmethod
    def ya_iz(cls):
        print(f'Издательство {cls.izdatelstvo}')

Publikatsiya = Publication('Хроники Амбера','Роджер Желязны', 1985)
Publikatsiya.display()
class Book(Publication):
    def __init__(self, isbn, title, author, year):
        super().__init__(title, author, year)
        self.isbn = isbn
    def display(self):
        super().display()
        print(f'isbn: {self.isbn}')


Kniga = Book(23,'Хроники Амбера','Роджер Желязны',1986)
Kniga.display()
Kniga.ya_iz()
class Magazine(Publication):
    def __init__(self, issue_namber, title, author, year):
        super().__init__(title, author, year)
        self.issue_number = issue_namber
    def display(self):
        super().display()
        print(f'issue_number: {self.issue_number}')

Jurnal= Magazine(26,'Хроники Амбера', 'Роджер Желязны', 1987)
Jurnal.display()
Jurnal.ya_iz()

# Задание 2
class BankAccount:
    def __init__(self, balance, interest_rate, transactions):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []
    def depozit(self, amount):
        self.balance += amount
        self.transactions.append({amount})
        print(f'Остаток по счету {self.balance}')

    def withdrow(self, amount):
        self.balance -= amount
        self.transactions.append({amount})
        print(f'Осаток по счету {self.balance}')

    def add_interest(self):
        interest = self.balance * self.interest_rate/100
        self.balance += interest
        self.transactions.append({self.balance})
        print(f'Осаток по счету {self.balance}')

    def history(self):
        print(f'Выписка по счету {self.transactions}')

accouunt = BankAccount(25, 105, 0)

accouunt.depozit(80)
accouunt.withdrow(43)
accouunt.add_interest()
accouunt.history()