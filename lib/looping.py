#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i <= 10 and i >= 0:
        if i == 0:
            print("Happy New Year!")
        else:
            print(i)
        i -= 1

def square_integers(int_list):
    squared_int_list = []
    for int in int_list:
        squared_int_list.append(int * int)
    # print(squared_int_list)
    return squared_int_list

def fizzbuzz():
    i = 1
    while i >= 1 and i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1

# happy_new_year()
# square_integers([1, 2, 3, 4, 5])
fizzbuzz()

