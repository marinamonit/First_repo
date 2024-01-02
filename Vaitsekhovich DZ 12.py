# Реализуйте итератор колоды карт (52 шт) CardDeck. Каждая карта представлена в виде строки типа 2 Пик.
# При вызове ункции next() будет представлена следующая карта. По окончании перебора всех элементов
# возникнет ошибка StopIteration

class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']

    def __next__(self):
        if self.index < self.length:
            suit = self.__SUITS[self.index // len(self.__RANKS)]
            rank = self.__RANKS[self.index % len(self.__RANKS)]
            self.index += 1
            return f'{rank} {suit}'
        else:
            raise StopIteration
    def __iter__(self):
        return self

deck = CardDeck()
while True:
    print(next(deck))


# Задача 2
#Числа Фибоначчи представляют последовательность, получаемую в результате сложения двух предыдущих элементов.
#Начинается коллекция с чисел 1 и 1.
#Она достаточно быстро растет, поэтому вычисление больших значений занимает немало времени.
#Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов.
#Для реализации этой функции потребуется обратиться к инструкции yield.
#Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать”
# промежуточные результаты по одному.

def fib(n):
    num1 = 1
    yield num1
    num2 = 1
    yield num2
    for i in range(n):
        num1, num2 = num2, num1 + num2
        yield num1

for num in fib(123):
    pass
print(num)
