# Warning overly complicated code for a calculator ahead.

import time
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def division(a, b):
    return a / b
def multiply(a, b):
    return a * b
def start_addition():
    x = int(input("Please enter number: "))
    y = int(input("Please enter number: "))
    # asking for result from add function
    res = add(x, y)
    print(res)
    time.sleep(10)
def start_subtraction():
    x = int(input("Please enter number: "))
    y = int(input("Please enter number: "))
    # asking for result from subtract function
    res = subtract(x, y)
    print(res)
    time.sleep(10)
def start_division():
    x = int(input("Please enter number: "))
    y = int(input("Please enter number: "))
    # asking for result from division function
    res = division(x, y)
    print(res)
    time.sleep(10)
def start_multiplication():
    x = int(input("Please enter number: "))
    y = int(input("Please enter number: "))
    # asking for result from multiplication function
    res = multiply(x, y)
    print(res)
    time.sleep(10)
def start():
    # Beginning to decide which function to access
    g = input("""Please enter
    1 for addition
    2 for subtraction
    3 for division
    4 for multiplication
    5 to exit

""")
    if g == "1":
        start_addition()
    if g == "2":
        start_subtraction()
    if g == "3":
        start_division()
    if g == "4":
        start_multiplication()
    elif g == "5":
        exit()
start()
