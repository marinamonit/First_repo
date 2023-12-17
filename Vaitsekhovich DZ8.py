
# Задание 1
import codecs
b = b'r\xc3\xa9sum\xc3\xa9'
print(type(b)) # это я для себя практикуюсь
b = codecs.decode(b)
print(b)
b = b.encode('latin-1')
print(b)
print(type(b)) # это я для себя практикуюсь
b = b.decode('latin1').encode('utf-8')
print(b)

# Задание 2

a = 'Shokolad, arbuz, kartoha'
b = 'Tsvetok, derevo, reka'
c = 'Andrey, Kristina, Gena'
d = '3, 4, 7, 9'
with open('new.txt', 'r+') as file:
    file.write(a)
    file.write('\n')
    file.write(b)
    file.write('\n')
with open('new.txt', 'a+') as file:
    file.write(c)
    file.write('\n')
    file.write(d)
    file.write('\n')

# Задание 3
import json
slovar = {123456 : ('Volodya', 33),
          456789 : ('Gena', 25),
          789654 : ('Lena', 64),
          654321 : ('Katya', 44),
          654987 : ('Pasha', 18),
          258963 : ('Karina', 36)}
with open('my.json', 'x+') as file:
    json.dump(slovar, file)

# Задание 4  не сделано, нашла информацию, но верно применить не могу.
# Пыталась сослаться на файл или присвоить переменной путь, но все-равно не работает.
# Просьба разъяснить на следующем уроке.
import csv
info = ['id', 'name', 'age', 'phone number']

with open('my.csv', 'r+') as file:
    wr = csv.DictWriter(file, fieldnames=info)
    wr.writeheader()
    wr.writerows()



