# Задание 1,2

import time
class Auto:
    def __init__(self, brand, age, mark, color='blue', weight=2300):
        self.brand = brand
        self.age = age
        self.mark = mark
    def move(self):
        print('move')
    def stop(self):
        print('stop')
    def birthday(self):
        self.age += 1
        print(self.age)

Opel = Auto('Opel', 2020, 'Tigra')
Opel.move()
Opel.stop()
Opel.birthday()

class Track(Auto):
    def __init__(self, max_load, brand, age, mark, color='blue', weight=2300):
        self.max_load = max_load
    def move(self):
        print('attention')
        super().move()
    def load(self):
        time.sleep(1)
        print('sleep')
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed, brand, age, mark, color='blue', weight=2300):
        self.max_speed = max_speed
    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')

Ford = Track(5000, 'Ford', 2013, 'Gigant')
Ford.move()
Ford.load()

BMW = Car(290, 'BMW', 2021, 'm5')
BMW.move()


