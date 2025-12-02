from tkinter import Tk, Entry, Button, StringVar

class Calculator():
  def __init__(self, root):
    root.title("Calculator POO")
    root.geometry("327x420")
    root.resizable(False, False)
    root.config(bg="gray")

    self.equation=StringVar()
    self.entry_value = ''
    Entry(width=17, bg='white', font=('arial', 30, 'bold'), textvariable=self.equation).place(x=0, y=0)

    Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda:self.show(')')).place(x=1, y=10)
    Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.show('(')).place(x=1, y=10)
    Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda:self.show('%')).place(x=1, y=10)
    Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda:self.show('1')).place(x=1, y=10)
    Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda:self.show('2')).place(x=1, y=10)
  
    Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda:self.show('3')).place(x=1, y=10)
    Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda:self.show('4')).place(x=1, y=10)
    Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda:self.show('5')).place(x=1, y=10)
    Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda:self.show('6')).place(x=1, y=10)
    Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda:self.show('7')).place(x=1, y=10)

    Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda:self.show('8')).place(x=1, y=10)
    Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda:self.show('9')).place(x=1, y=10)
    Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda:self.show('0')).place(x=1, y=10)
    Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda:self.show('.')).place(x=1, y=10)
    Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda:self.show('+')).place(x=1, y=10)

    Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda:self.show('-')).place(x=1, y=10)
    Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda:self.show('/')).place(x=1, y=10)
    Button(width=11, height=4, text='*', relief='flat', bg='white', command=lambda:self.show('*')).place(x=1, y=10)
    Button(width=11, height=4, text='=', relief='flat', bg='white', command=lambda:self.solve).place(x=1, y=10)
    Button(width=11, height=4, text='C', relief='flat', bg='white', command=lambda:self.clear).place(x=1, y=10)

  def show(self, value):
    self.entry_value += str(value)
    self.equation.set(self.entry_value)
    
  def clear(self):
    self.entry_value = ''
    self.equation.set(self.entry_value)

  def solve(self):
    result = eval.set(self.entry_value)
    self.equation.set(result)

root = Tk()
run = Calculator(root)