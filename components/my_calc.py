import tkinter 
from tkinter import *

root = Tk()

root.geometry("500x600")
root.resizable(0, 0)
root.title("Calculator(Tanishq Gupta)")

root.configure(background = "black")

def btn_clicked(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def btn_AC():
	e.delete(0, END)

def button_percent():
	first_number = e.get()
	e.delete(0, END)
	global f_num
	global op
	op = "percentage"
	f_num = int(first_number)

def button_add():
	first_number = e.get()
	e.delete(0, END)
	global f_num
	global op
	op = "addition"
	f_num = int(first_number)

def button_subtract():
	first_number = e.get()
	e.delete(0, END)
	global f_num
	global op
	op = "subtraction"
	f_num = int(first_number)


def button_multiply():
	first_number = e.get()
	e.delete(0, END)
	global f_num
	global op
	op = "multiplication"
	f_num = int(first_number)

def button_divide():
	first_number = e.get()
	e.delete(0, END)
	global f_num
	global op
	op = "division"
	f_num = int(first_number)

def button_exp():
	first_number = e.get()
	e.delete(0, END)
	global f_num
	global op
	op = "exponent"
	f_num = int(first_number)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	s_num = int(second_number)

	if op == "addition":
		e.insert(0, (f_num + s_num))
	if op == "subtraction":
		e.insert(0, (f_num - s_num))
	if op == "multiplication":
		e.insert(0, (f_num * s_num))
	if op == "division":
		e.insert(0, (f_num / s_num))
	if op == "exponent":
		e.insert(0, (f_num ** s_num))
	if op == "percentage":
		e.insert(0, (f_num % s_num))								


e = Entry(
	root,
	font = ("Verdana", 35),
	width = 50,
	border = 0,
	bg = "#000000",
	fg = "#ffffff",
	
    )

e.pack(pady = 10)

row1 = Frame(root)
row1.pack(expand = True, fill = "both")

row2 = Frame(root)
row2.pack(expand = True, fill = "both")

row3 = Frame(root)
row3.pack(expand = True, fill = "both")

row4 = Frame(root)
row4.pack(expand = True, fill = "both")

row5 = Frame(root)
row5.pack(expand = True, fill = "both")

btn1 = Button(
	row1,
	text = "AC",
	font = ("sans-serif", 22),
	command = btn_AC,
	bg = "#FFD700",
	border = 0)
btn1.pack(side = LEFT, expand = True, fill = "both")	

btn2 = Button(
	row1,
	text = "**",
	font = ("sans-serif", 22),
	command = button_exp,
	bg = "#000000",
	fg = "#FFD700",
	border = 0
	)
btn2.pack(side = LEFT, expand = True, fill = "both")	

btn3 = Button(
	row1,
	text = "%",
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	border = 0,
	command = button_percent)
btn3.pack(side = LEFT, expand = True, fill = "both")	

btn4 = Button(
	row1,
	text = "/",
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = button_divide,
	border = 0)
btn4.pack(side = LEFT, expand = True, fill = "both")



btn1 = Button(
	row2,
	text = "7",
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(7),
	border = 0)
btn1.pack(side = LEFT, expand = True, fill = "both")	

btn2 = Button(
	row2,
	text = "8",
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(8),
	border = 0)
btn2.pack(side = LEFT, expand = True, fill = "both")	

btn3 = Button(
	row2,
	text = "9",
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	border = 0,
	command = lambda: btn_clicked(9))
btn3.pack(side = LEFT, expand = True, fill = "both")	

btn4 = Button(
	row2,
	text = "*",
	font = ("sans-serif", 22),
	command = button_multiply,
	bg = "#000000",
	fg = "#FFD700",
	border = 0)
btn4.pack(side = LEFT, expand = True, fill = "both")



btn1 = Button(
	row3,
	text = "4",
	font = ("sans-serif", 22),
	bg = "#000000",
	border = 0,
	fg = "#FFD700",
	command = lambda: btn_clicked(4))
btn1.pack(side = LEFT, expand = True, fill = "both")	

btn2 = Button(
	row3,
	text = "5",
	border = 0,
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(5))
btn2.pack(side = LEFT, expand = True, fill = "both")	

btn3 = Button(
	row3,
	text = "6",
	border = 0,
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(6))
btn3.pack(side = LEFT, expand = True, fill = "both")	

btn4 = Button(
	row3,
	text = "-",
	font = ("sans-serif", 22),
	command = button_subtract,
	bg = "#000000",
	fg = "#FFD700",
	border = 0)
btn4.pack(side = LEFT, expand = True, fill = "both")	



btn1 = Button(
	row4,
	text = "1",
	border = 0,
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(1))
btn1.pack(side = LEFT, expand = True, fill = "both")	

btn2 = Button(
	row4,
	text = "2",
	border = 0,
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(2))
btn2.pack(side = LEFT, expand = True, fill = "both")	

btn3 = Button(
	row4,
	text = "3",
	border = 0,
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(3))
btn3.pack(side = LEFT, expand = True, fill = "both")	

btn4 = Button(
	row4,
	text = "+",
	font = ("sans-serif", 22),
	command = button_add,
	bg = "#000000",
	fg = "#FFD700",
	border = 0)
btn4.pack(side = LEFT, expand = True, fill = "both")

btn1 = Button(
	row5,
	text = ".",
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	border = 0)
btn1.pack(side = LEFT, expand = True, fill = "both")	

btn3 = Button(
	row5,
	text = "0",
	border = 0,
	font = ("sans-serif", 22),
	bg = "#000000",
	fg = "#FFD700",
	command = lambda: btn_clicked(0))
btn3.pack(side = LEFT, expand = True, fill = "both")	

btn4 = Button(
	row5,
	text = "=",
	font = ("sans-serif", 22),
	command = button_equal,
	bg = "#000000",
	fg = "#FFD700",
	border = 0
	)
btn4.pack(side = LEFT, expand = True, fill = "both")

root.mainloop()
