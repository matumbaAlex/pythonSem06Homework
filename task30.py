# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def userInput(text):
    return int(input(f"{text}: "))



def main():
    first = userInput("enter first number")
    step = userInput("enter step")
    quantity = userInput("enter quantity elements")
    arrayBilder(first, step, quantity)

def arrayBilder(first, step, quantity):
    list = [first]
    for i in range(quantity-1):
        list.append(list[i]+step)
    print(list)
main()