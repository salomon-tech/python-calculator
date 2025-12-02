from tkinter import *



root = Tk()
root.config(bg="black")
root.geometry("800x500+1+1")
root.title("calculator")
root.resizable(False, False)



labe1 = Entry(root, bd=4, font=("sans serif", 30))
labe1.place(x=0,y=0, widt=800, height=100)

# futures of this soft

# b1 = Button(root, text="V", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=0, y=100, width=200)
# b1 = Button(root, text="¶", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=200, y=100, width=200)
# b1 = Button(root, text="^", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=400, y=100, width=200)
# b1 = Button(root, text="!", bd=3, bg="blue", font=("sans serif", 20), command="")
# b1.place(x=600, y=100, width=200)


# b1 = Button(root, text="Deg", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=0, y=150, width=200)
# b1 = Button(root, text="sin", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=200, y=150, width=200)
# b1 = Button(root, text="cos", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=400, y=150, width=200)
# b1 = Button(root, text="tan", bd=3, bg="blue", font=("sans serif", 20), command="")
# b1.place(x=600, y=150, width=200)

# b1 = Button(root, text="Inv", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=0, y=200, width=200)
# b1 = Button(root, text="e", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=200, y=200, width=200)
# b1 = Button(root, text="In", bd=3, bg='blue', font=("sans serif", 20), command="")
# b1.place(x=400, y=200, width=200)
# b1 = Button(root, text="log", bd=3, bg="blue", font=("sans serif", 20), command="")
# b1.place(x=600, y=200, width=200)

b1 = Button(root, text="AC", bd=3, bg="blue",font=("sans serif", 20), command="")
b1.place(x=0, y=250, width=200)
b1 = Button(root, text="()", bd=3, background="blue",font=("sans serif", 20), command="")
b1.place(x=200, y=250, width=200)
b1 = Button(root, text="%", bd=3,background="blue", font=("sans serif", 20), command="")
b1.place(x=400, y=250, width=200)
b1 = Button(root, text="÷", bd=3,background="blue", font=("sans serif", 20), command="")
b1.place(x=600, y=250, width=200)

b1 = Button(root, text="7", bd=3, bg='black', fg='white', font=("sans serif", 20), command="")
b1.place(x=0, y=300, width=200)
b1 = Button(root, text="8", bd=3,bg='black', fg='white', font=("sans serif", 20), command="")
b1.place(x=200, y=300, width=200)
b1 = Button(root, text="9", bd=3,bg='black',fg='white', font=("sans serif", 20), command="")
b1.place(x=400, y=300, width=200)
b1 = Button(root, text="x", bd=3,background="blue", font=("sans serif", 20), command="")
b1.place(x=600, y=300, width=200)

b1 = Button(root, text="4", bd=3, bg='black',fg='white', font=("sans serif", 20), command="")
b1.place(x=0, y=350, width=200)
b1 = Button(root, text="5", bd=3, bg='black', fg='white', font=("sans serif", 20), command="")
b1.place(x=200, y=350, width=200)
b1 = Button(root, text="6", bd=3, bg='black', fg='white',font=("sans serif", 20), command="")
b1.place(x=400, y=350, width=200)
b1 = Button(root, text="-", bd=3, background="blue", font=("sans serif", 20), command="")
b1.place(x=600, y=350, width=200)

b1 = Button(root, text="1", bd=3, bg='black',fg='white' ,font=("sans serif", 20), command="")
b1.place(x=0, y=400, width=200)
b1 = Button(root, text="2", bd=3, bg='black', fg='white', font=("sans serif", 20), command="")
b1.place(x=200, y=400, width=200)
b1 = Button(root, text="3", bd=3, bg='black', fg='white',font=("sans serif", 20), command="")
b1.place(x=400, y=400, width=200)
b1 = Button(root, text="+", bd=3, bg="blue", font=("sans serif", 20), command="")
b1.place(x=600, y=400, width=200)

b1 = Button(root, text="0", bd=3, bg='black', fg='white',font=("sans serif", 20), command="")
b1.place(x=0, y=450, width=200)
b1 = Button(root, text=".", bd=3, bg='black',fg='white', font=("sans serif", 20), command="")
b1.place(x=200, y=450, width=200)
b1 = Button(root, text="suppr", bd=3, bg='black',fg='white', font=("sans serif", 20), command="")
b1.place(x=400, y=450, width=200)
b1 = Button(root, text="=", bd=3, bg="blue", font=("sans serif", 20), command="")
b1.place(x=600, y=450, width=200)

root.mainloop()