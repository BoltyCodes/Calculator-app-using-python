from tkinter import *

exp = ""

def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

#function for evalutating final expression.

def equalpress():
    try:
        global exp 
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set("error")
        exp = ""

#function to clear the content

def clear():
    global exp 
    exp = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background = "white")
    gui.title("Calculator App")

    #defines size
    gui.geometry("320x320")

    #Equation variable definition

    equation = StringVar()
    
    expression_feild = Entry(gui,textvariable = equation)
    expression_feild.grid(columnspan = 4, ipadx = 70)
    
    #row 1
    button1 = Button(gui, text = "1", fg = "black", bg = "red", command = lambda: press(1),height = 7, width = 9)
    button1.grid(row = 2, column = 0)
    button2 = Button(gui, text = "2",fg = "black", bg = "red", command = lambda: press(2),height = 7, width = 9)
    button2.grid(row = 2, column = 1)
    button3 = Button(gui, text = "3", fg = "black", bg = "red", command = lambda: press(3),height = 7, width = 9)
    button3.grid(row = 2, column = 2)
    
    plus = Button(gui, text = "+",fg = "black", bg = "blue", command = lambda: press("+"),height = 7, width = 9)
    plus.grid(row = 2, column = 3)

    

    #row 2
    button4 = Button(gui, text = "4", fg = "black", bg = "red", command = lambda: press(4),height = 7, width = 9)
    button4.grid(row = 3, column = 0)
    button5 = Button(gui, text = "5",fg = "black", bg = "red", command = lambda: press(5),height = 7, width = 9)
    button5.grid(row = 3, column = 1)
    button6 = Button(gui, text = "6", fg = "black", bg = "red", command = lambda: press(6),height = 7, width = 9)
    button6.grid(row = 3, column = 2)

    x = Button(gui, text = "x",fg = "black", bg = "blue", command = lambda: press("*"),height = 7, width = 9)
    x.grid(row = 3, column = 3)


    #row 3
    button7 = Button(gui, text = "7", fg = "black", bg = "red", command = lambda: press(7),height = 7, width = 9)
    button7.grid(row = 4, column = 0)
    button8 = Button(gui, text = "8",fg = "black", bg = "red", command = lambda: press(8),height = 7, width = 9)
    button8.grid(row = 4, column = 1)
    button9 = Button(gui, text = "9", fg = "black", bg = "red", command = lambda: press(9),height = 7, width = 9)
    button9.grid(row = 4, column = 2)

    div = Button(gui, text = "÷",fg = "black", bg = "blue", command = lambda: press("/"),height = 7, width = 9)
    div.grid(row = 4, column = 3)


    #row 4 (extra)

    button0 = Button(gui, text = "0", fg = "black", bg = "red", command = lambda: press(0),height = 7, width = 9)
    button0.grid(row = 5, column = 0)

    clear = Button(gui, text = "Clear", fg = "black", bg = "blue", command = clear, height = 7, width = 9)
    clear.grid(row = 5, column = 1)

    equalbutton = Button(gui, text = "=", fg = "black", bg = "blue", command = equalpress,height = 7, width = 9)
    equalbutton.grid(row = 5, column = 2)

    minus = Button(gui, text = "-",fg = "black", bg = "blue", command = lambda: press("-"),height = 7, width = 9)
    minus.grid(row = 5, column = 3)

    Decimal = Button(gui, text = ".", fg = "black", bg = "blue", command = lambda: press("."),height = 7, width = 9)
    Decimal.grid(row = 6, column = 0)






    
  


    gui.mainloop()
