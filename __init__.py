from tkinter import *

# referal:  https://www.activestate.com/resources/quick-reads/how-to-create-a-calculator-in-python-tkinter/


root = Tk()

root.mainloop()
root.geometry("312x324")
root.resizable(0, 0)
root.title("CALCULATOR")


def button_click(item):
    global expression
    expression + str(item)
    input_text.set(expression)


def button_clear():
    global expression
    expression = ""
    input_text.set("")


def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

input_text= StringVar()
