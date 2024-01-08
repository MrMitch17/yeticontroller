#!/usr/bin/env python

import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


if __name__ == '__main__':
    if len(sys.argv) == 4:
        first_operand = int(sys.argv[1])
        operation = sys.argv[2]
        second_operand = int(sys.argv[3])
        if operation == '+':
            print(add(first_operand, second_operand))
        elif operation == '-':
            print(subtract(first_operand, second_operand))
        elif operation == '*':
            print(multiply(first_operand, second_operand))
        else:
            sys.exit('Unsupported operation!')
    else:
        sys.exit('Usage: ./calculator.py <x> <operation> <y>')
