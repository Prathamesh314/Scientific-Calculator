from tkinter import *
from math import *
from tkinter import messagebox


prev = []

operators = ['+', '-', '/', '*', '%', '^']

calculator = Tk(className="Scientific Calculator")

calculator.resizable(width=False, height=False)

frame1 = Frame(calculator)

# label1 = Label(calculator)

v = StringVar()


e1 = Entry(frame1, width=18, font=("Arial", 20, "bold"), bg="black", fg="white", bd=30, textvariable=v)


def write(word):
    wd = v.get()
    v.set(wd+word)


def del_last():
    wrd = v.get()
    v.set(wrd[:len(wrd)-1])


def apply_math_func(func, is_rad=False):
    try:
        val = float(v.get())
        if is_rad:
            val = radians(val)
        v.set(str(round(func(val), 8)))
    except (ValueError, TclError):
        messagebox.showerror("Error", "Invalid Input Provided")

def apply_simple_func(func):
    try:
        val = v.get()
        v.set(func(val))
    except (ValueError, TclError):
        messagebox.showerror("Error", "Invalid Input Provided")

def pie():
    apply_simple_func(lambda val: val + str(round(pi, 8)))

def pie2():
    apply_simple_func(lambda val: val + str(round(2 * pi, 8)))

def natural_log():
    apply_math_func(lambda val: log(val, e))

def log10():
    apply_math_func(lambda val: log(val, 10))

def log2():
    apply_math_func(lambda val: log(val, 2))

def cose():
    apply_math_func(cos, is_rad=True)

def coseh():
    apply_math_func(cosh, is_rad=True)

def exponent():
    apply_math_func(exp)

def factorial():
    try:
        val = int(v.get())
        ans = 1
        while val > 0:
            ans *= val
            val -= 1
        v.set(str(ans))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input Provided")

def degree():
    apply_math_func(lambda val: (180 * val) / pi)

def tangent():
    apply_math_func(tan, is_rad=True)

def tangenth():
    apply_math_func(tanh, is_rad=True)

def inverse():
    apply_math_func(lambda val: 1 / val)

def arccos():
    apply_math_func(lambda val: degrees(acos(val)))

def sine():
    apply_math_func(sin, is_rad=True)

def sineh():
    apply_math_func(sinh)

def eee():
    apply_simple_func(lambda wd: wd + str(round(exp(1), 8)))

def gammaa():
    apply_math_func(gamma)

def asine():
    apply_math_func(lambda val: degrees(asin(val)))
#defining operators


def result():
    try:
        expr = v.get()
        # Replace custom symbols with Python equivalents
        expr = expr.replace('^', '**').replace('√', 'sqrt')

        # Define a safe dictionary of allowed functions and constants
        safe_dict = {
            "sqrt": sqrt, "pi": pi, "e": e,
            "sin": sin, "cos": cos, "tan": tan, "sinh": sinh, "cosh": cosh, "tanh": tanh,
            "asin": asin, "acos": acos, "atan": atan,
            "log": log, "log10": log10, "log2": log2,
            "exp": exp, "gamma": gamma, "degrees": degrees, "radians": radians
        }

        # Evaluate the expression
        res = eval(expr, {"__builtins__": None}, safe_dict)
        v.set(str(round(res, 10)))

    except (SyntaxError, NameError):
        messagebox.showerror("Error", "Invalid Expression")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def change_sign():
    try:
        number = float(v.get())
        v.set(str((-1)*number))
    except ValueError:
        messagebox.showinfo("Info","Provide a number not expression")

def iExit():
    calculator.destroy()


def cut():
    prev1 = v.get()
    prev.append(prev1)
    e1.delete(0, END)


def copy():
    prev.append(v.get())


def paste():
    e1.insert(END, prev[0])
    prev.pop()


def scientific_mode():
    # e1.config(width=36)
    calculator.config(bg = "#76D7C4")
    menubar.config(bg = "#3498DB")
    #pi button
    pi_button = Button(text="Pi", width=4, font=("Arial", 20, "bold"), bg = "black", fg = "white", command = pie)
    pi_button.grid(row = 1, column = 7, padx = 1, pady = 1)

    #2pi_button
    pi2_button = Button(text = "2Pi" ,width = 4, font = ("Arial", 20, "bold"), bg = "black", fg = "white", command =pie2)
    pi2_button.grid(row=2,column=7,padx=1,pady=1)

    #ln_button
    ln_button = Button(text="ln",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=natural_log)
    ln_button.grid(row=3,column=7,pady=1,padx=1)

    #log10_button
    log10_button = Button(text="log10",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=log10)
    log10_button.grid(row=4,column=7,padx=1,pady=1)

    #log2_button
    log2_button = Button(text="log2",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=log2)
    log2_button.grid(row=5,column=7,padx=1,pady=1)

    #cos button
    cos_button = Button(text="Cos",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=cose)
    cos_button.grid(row=1,column=8,padx=1,pady=1)

    #cos button
    cosh_button = Button(text="Cosh",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=coseh)
    cosh_button.grid(row=2,column=8,padx=1,pady=1)

    #cosh
    exp_button = Button(text="exp", width=4, font=("Arial", 20, "bold"), bg="black", fg="white",command=exponent)
    exp_button.grid(row=3, column=8, padx=1, pady=1)

    #factorial button
    fact_button = Button(text="!",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=factorial)
    fact_button.grid(row=4,column=8,padx=1,pady=1)

    #def button
    power_button = Button(text="^", width=4, font=("Arial", 20, "bold"), bg="black", fg="white",command=lambda:write('^'))
    power_button.grid(row=5, column=8, padx=1, pady=1)

    # tan button
    tan_button = Button(text="Tan",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=tangent)
    tan_button.grid(row=1,column=9)

    # tanh button
    tanh_button = Button(text="Tanh", width=4, font=("Arial", 20, "bold"), bg="black", fg="white",command=tangenth)
    tanh_button.grid(row=2, column=9)

    #mod button
    mod_button = Button(text="Mod",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=lambda: write("%"))
    mod_button.grid(row=3,column=9,padx=1,pady=1)

    #exp button
    inverse_button = Button(text="1/x",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=inverse)
    inverse_button.grid(row=4,column=9,padx=1,pady=1)

    # acosh button
    acos_button = Button(text="acos",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=arccos)
    acos_button.grid(row=5,column=9,padx=1,pady=1)

    #sin button
    sin_button = Button(text="Sin",width=4,font=("Arial",20,"bold"),bg="Black",fg="white",command=sine)
    sin_button.grid(row=1,column=10,padx=1,pady=1)

    #sinh button
    sinh_button = Button(text="Sinh",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=sineh)
    sinh_button.grid(row=2,column=10,padx=1,pady=1)

    # e button
    e_button = Button(text="e",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=eee)
    e_button.grid(row=3,column=10,padx=1,pady=1)

    # gamma button
    gamma_button = Button(text="Γ",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=gammaa)
    gamma_button.grid(row=4,column=10,padx=1,pady=1)

    # asin button
    asin_button = Button(text="asin",width=4,font=("Arial",20,"bold"),bg="black",fg="white",command=asine)
    asin_button.grid(row=5,column=10,padx=1,pady=1)


def create_button():
    #Clear button
    C_button = Button(text='C',bg="light blue",width=4,font=("Arial",20,"bold"),command=del_last)
    C_button.grid(row=1,column=1,padx=1,pady=5)

    #Clear all button
    CE_button = Button(text="CE",bg="light blue",width=4,font=("Arial",20,"bold"),command=lambda:e1.delete(0,END))
    CE_button.grid(row=1,column=2,padx=1,pady=5)

    #Button to calculate Square root
    sq_button = Button(text="√",bg="light blue",width=4,font=("Arial",20,"bold"),command=lambda   :write("√"))
    sq_button.grid(row=1,column=3,padx=1,pady=5)

    #Addition button
    plus_button = Button(text="+",bg="light blue",width=4,font=("Arial",20,"bold"),command=lambda  :write("+"))
    plus_button.grid(row=1,column=4,padx=1,pady=3)

    # Creating buttons
    for i in range(9):
        bt = Button(text=f"{i+1}",fg="white",bg="black",width=4,font=("Arial",20,"bold"),command=lambda  j = i :write(f"{j+1}"))
        bt.grid(row=(i)//3+2,column=(i)%3+1,padx=1,pady=3)

    #subtract button
    sub_button = Button(text="-",bg="light blue",width=4,font=("Arial",20,"bold"),command=lambda   :write("-"))
    sub_button.grid(row=2,column=4,padx=1,pady=5)

    #multiply button
    mult_button = Button(text="x",bg="light blue",width=4,font=("Arial",20,"bold"),command=lambda   :write("*"))
    mult_button.grid(row=3,column=4,padx=1,pady=3)

    #division button
    div_button = Button(text="/",bg="light blue",width=4,font=("Arial",20,"bold"),command=lambda   :write("/"))
    div_button.grid(row=4,column=4,padx=1,pady=5)

    #Zero button
    zero_button = Button(text="0",bg="black",fg="white",width=4,font=("Arial",20,"bold"),command=lambda   :write("0"))
    zero_button.grid(row=5,column=1,padx=1,pady=5)

    #decimal button
    decimal_button = Button(text=".",bg="light blue",width=4,font=("Arial",20,"bold"),command=lambda   :write("."))
    decimal_button.grid(row=5,column=2,padx=1,pady=5)

    #sign button
    sign_button = Button(text="±",bg="light blue",width=4,font=("Arial",20,"bold"),command=change_sign)
    sign_button.grid(row=5,column=3,padx=1,pady=5)

    # result_button
    result_button = Button(text="=",bg="light blue",width=4,font=("Arial",20,"bold"),command=result)
    result_button.grid(row=5,column=4,padx=1,pady=5)

if __name__=="__main__":
    frame1.grid(row=0,column=1,columnspan=4,padx=10,pady=1)
    create_button()

    e1.grid(row=0,column=1,columnspan=4,pady=1,padx=5)

    menubar = Menu(calculator,bg="#3498DB")

    #File menu
    file_menu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=file_menu,font=("Arial",20,"bold"))
    file_menu.add_command(label="Standard")
    file_menu.add_command(label="Scientific",command=scientific_mode)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=iExit)

    #Edit menu
    editmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=editmenu,font=("Arial",20,"bold"))
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    calculator.config(menu=menubar)
    calculator.mainloop()
