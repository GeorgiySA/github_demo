# Напишем функцию, которая будет укладывать другие в словарь:
# registered = {}
# def func_1():
#     print("Давай начнем")
#
# def func_2():
#     print("Давай закончим")
#
# def register_func(another_func, name):
#     registered[name] = another_func
#
# register_func(func_1, "start")
# register_func(func_2, "end")
#
# user_input = input("Введите команду")
# function_to_call = registered.get(user_input)
# function_to_call()


''' А если пойти дальше и сделать маршрутизацию, как во Flask?' \
'Создадим пару функций и положим в словарь. Затем попросим пользователя ввести что-то с клавиатуры, ' \
'получим из словаря и вызовем нужную функцию.'''
# registered = {}
#
# def func_1():
#     print("Давай начнем")
#
# def func_2():
#     print("Давай закончим")
#
# def register_func(another_func, name):
#     registered[name] = another_func
#
# register_func(func_1, "start")
# register_func(func_2, "end")
#
# user_input = input("Введите команду")
# function_to_call = registered.get(user_input)
# function_to_call()


"""Используя полученные знания, мы можем написать такую функцию, которая, приняв функцию А, 
вернет не изначальную функцию, а функцию Б."""
# def hello():
#     """ изначальная функция """
#     print("hello")
#
# def angry_func():
#     """ новая функция """
#     print("grrrht!")
#
# def wrap(another_func):
#     """ функция, превращающая одну в другую """
#     print("Я получаю функцию и делаю ее злой")
#     return angry_func
#
# hello = wrap(hello)
# hello()

"""Например, декоратор @log может поменять функцию так, что та будет при каждом вызове «стучать» в консоль, 
базу данных или текстовый файл о том, что была вызвана."""
# def log(func):
#    def wrapper():
#        print("Я слежу за тобой, функция!")
#        func()
#    return wrapper
#
# @log
# def another_function():
#    print("Что-то выполняется")
#
# another_function()
""" ------------------------------------------- """

from flask import Flask

app = Flask(__name__)

@app.route("/test/")
def page_test():
    return "Приложение работает"

@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

@app.route('/users/<uid>')

def profile(uid):
   return f'<h1>Профиль {uid}</h1>'

@app.route('/catalog/items/<itemid>')
def profile(itemid):
   return f'<h1>Страничка товара {itemid}</h1>'

app.run(host='0.0.0.0', port=8000)
