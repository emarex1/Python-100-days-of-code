#!/usr/bin/python3
"""Defining add, sub, div and mul functions"""


def add():
    return num1 + num2


def sub():
    return num1 - num2


def div():
    return num1 / num2


def mul():
    return num1 * num2


try:
    """Catching an exception if a user inputs invalid value"""

    num1 = int(input("please input your first number:"))

    operations = {"+": add, "-": sub, "/": div, "*": mul}
    # loop through dictionary to keys
    for symbol in operations:
        print(f"{symbol}")

    sign = input("please select symbol:")

    num2 = int(input("please select second number:"))
    """Use dictionary keys to get function value"""
    get_symbol_value = operations[sign]
    answer = get_symbol_value()

except (ValueError, KeyError):
    print("invalid value")

finally:
    print(f"{num1}  {sign}  {num2}  =  {answer}")
