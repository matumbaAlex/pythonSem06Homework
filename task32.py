# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def userInput(text):
    return int(input(f"{text}: "))

def arrayBilder(len):
    array = list()
    for i in range(len):
        array.append(random.randint(-10, 10))
    return array

def searchIndex(list, min, max):
    for i in range(len(list)):
        if min <= list[i] <= max:
            print(i, end=" ")
def main():
    list = arrayBilder(userInput("enter quantity elements"))
    print(list)
    min = userInput("enter min value")
    max = userInput("enter max value")
    searchIndex(list, min, max)
main()