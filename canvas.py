#animation of four colored squares that will start from the middle 

import tkinter as tk

root = tk.Tk()
WIDTH = 300
HEIGHT = 300

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

x = WIDTH / 2 
y = HEIGHT / 2 


square = canvas.create_rectangle(x, y, x - 30, y - 30, outline="white", fill="green")
square2 = canvas.create_rectangle(x, y, x + 30, y + 30, outline="white", fill="blue")
square3 = canvas.create_rectangle(x, y, x + 30, y - 30, outline="white", fill="yellow")
square4 = canvas.create_rectangle(x, y, x - 30, y + 30, outline="white", fill="red")

def redraw_square():
    canvas.after(50, redraw_square)
    canvas.move(square, 5, 5)

def redraw_square2():
    canvas.after(50, redraw_square2)
    canvas.move(square2, -5, -5)

def redraw_square3():
    canvas.after(50, redraw_square3)
    canvas.move(square3, -5, 5)
    
def redraw_square4():
    canvas.after(50, redraw_square4)
    canvas.move(square4, 5, -5)

redraw_square()
redraw_square2()
redraw_square3()
redraw_square4()
root.mainloop()