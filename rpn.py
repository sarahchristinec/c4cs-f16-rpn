#!/usr/bin/env python3

import tkinter
from tkinter import *
from tkinter import ttk


def clear(*args):
    arg1.set(0)
    arg2.set(0)
    result.set(0)

def add(*args):
    try:
        value1 = float(arg1.get())
        value2 = float(arg2.get())

        result.set(value1 + value2) 
    except ValueError:
        pass


def sub(*args):
    try:
        value1 = float(arg1.get())
        value2 = float(arg2.get())

        result.set(value1 - value2) 
    except ValueError:
        pass


def mult(*args):
    try:
        value1 = float(arg1.get())
        value2 = float(arg2.get())

        result.set(value1 * value2) 
    except ValueError:
        pass


def div(*args):
    try:
        value1 = float(arg1.get())
        value2 = float(arg2.get())

        result.set(value1 / value2) 
    except ValueError:
        pass


def exp(*args):
    try:
        value1 = float(arg1.get())
        value2 = float(arg2.get())

        result.set(value1 ^ value2) 
    except ValueError:
        pass

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

arg1 = StringVar()
arg2 = StringVar()
result = StringVar()

first_entry = ttk.Entry(mainframe, width=5, textvariable=arg1)
first_entry.grid(column=2, row=1, sticky=(W, E))

second_entry = ttk.Entry(mainframe, width=5, textvariable=arg2)
second_entry.grid(column=4, row=1, sticky=(W, E))

ttk.Button(mainframe, text="+", command=add).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="-", command=sub).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="*", command=mult).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="/", command=div).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="^", command=exp).grid(column=4, row=3, sticky=W)

ttk.Button(mainframe, text="Clear", command=clear).grid(column=4, row=4, sticky=W)

ttk.Label(mainframe, text="arg1:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="arg2:").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="result:").grid(column=2, row=6, sticky=E)

ttk.Label(mainframe, textvariable=result).grid(column=3, row=6, sticky=(W, E))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#first_entry.focus()
#second_entry.focus()
#root.bind('<Return>', calculate)

root.mainloop()

##################
import readline
import operator

operators = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    '^':operator.pow,
    '%':operator.mod,
}

def calculate(string):
    stack = list()
    for token in string.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = operators[token]
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError
    return stack.pop()
####################

def main():
    while True:
        calculate(input("rpn calc>"))

if __name__ == '__main__':
    main()
