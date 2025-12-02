from tkinter import Tk, Entry, Button, StringVar

class Calculator:
  def __init__(self, root):
    root.title("Calculator POO")
    root.geometry("327x420")
    root.resizable(False, False)
    root.config(bg="#ffff3f")

    self.equation=StringVar()
    self.entry_value = ''
    Entry(width=17, bg='white', font=('arial', 30, 'bold'), textvariable=self.equation).place(x=0, y=0)

    Button(width=11, height=4, text='', relief='flat', bg='white', command=lambda:self.show()).place(x=1, y=10)

root = Tk()
run = Calculator(root)