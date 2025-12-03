from tkinter import Tk, Entry, Button, StringVar

class Calculator():
  def __init__(self, root):
    root.title("Calculator POO")
    root.geometry("506x558")
    root.resizable(False, False)
    root.config(bg="gray")

    self.equation=StringVar()
    self.entry_value = ''
    Entry(width=500, bg='gray',bd=4, font=('arial', 50, 'bold'), textvariable=self.equation).place(x=0, y=0)

    Button(width=12, height=4, text='(',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show('(')).place(x=0, y=82)
    Button(width=12, height=4, text=')',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show(')')).place(x=123, y=82)
    Button(width=12, height=4, text='%',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show('%')).place(x=240, y=82)
    Button(width=12, height=4, text='/',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show('/')).place(x=363, y=82)

    Button(width=12, height=4, text='1',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('1')).place(x=0, y=172)
    Button(width=12, height=4, text='2',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('2')).place(x=123, y=172)
    Button(width=12, height=4, text='3',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('3')).place(x=240, y=172)
    Button(width=12, height=4, text='*',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show('*')).place(x=363, y=172)

    Button(width=12, height=4, text='4',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('4')).place(x=0, y=262)
    Button(width=12, height=4, text='5',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('5')).place(x=123, y=262)
    Button(width=12, height=4, text='6',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('6')).place(x=240, y=262)
    Button(width=12, height=4, text='-',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show('-')).place(x=363, y=262)

    Button(width=12, height=4, text='7',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('7')).place(x=0, y=352)
    Button(width=12, height=4, text='8',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('8')).place(x=123, y=352)
    Button(width=12, height=4, text='9',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('9')).place(x=240, y=352)
    Button(width=12, height=4, text='+',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show('+')).place(x=363, y=352)

    Button(width=12, height=4, text='C',bd=4,font=(20), relief='flat', bg='blue', fg='white', command=lambda:self.clear()).place(x=0, y=442)
    Button(width=12, height=4, text='0',bd=4,font=(20), relief='flat', bg='black', fg='white', command=lambda:self.show('0')).place(x=123, y=442)
    Button(width=12, height=4, text='.',bd=4,font=(20), relief='flat', bg='orange', fg='white', command=lambda:self.show('.')).place(x=240, y=442)
    Button(width=12, height=4, text='=',bd=4,font=(20), relief='flat', bg='blue',fg='white', command=lambda:self.solve()).place(x=363, y=442)

  def show(self, value):
    self.entry_value += str(value)
    self.equation.set(self.entry_value)

  def clear(self):
    self.entry_value = ''
    self.equation.set(self.entry_value)

  def solve(self):
    result = eval(self.entry_value)
    self.equation.set(result)

root = Tk()
run = Calculator(root)
root.mainloop()