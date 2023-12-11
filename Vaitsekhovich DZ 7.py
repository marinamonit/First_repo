from datetime import datetime
#Задание 1
def decor_working_hours_only(func):
    def wrapper():
        if 9 <= int(datetime.now().strftime('%H')) <= 18:
            func()
        else:
            print('Работать нельзя')
    return wrapper

@decor_working_hours_only
def work():
        print('Работаем')

work()


#Задание 2
def type_chek(correct_type):
    def func2(func):
        def wrapper(arg):
            if type(arg) == correct_type:
                return func(arg)
            else:
                return 'Bad type'
        return wrapper
    return func2

@type_chek(int)
def times2(num):
    return num * 2

print(times2(2))
print(times2(True))

@type_chek(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(1.5))

print(first_letter(1.5))



