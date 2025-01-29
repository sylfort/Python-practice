import tkinter as tk
import random

class Ball:
    def __init__(self,x,y,dx,dy,color):
        self.x = x 
        self.dx = dx
        self.y = y 
        self.dy = dy 
        self.color = color 
        self.mae = None 
        
    def color_change(self, canvas):  
        new_color = "#{:02x}{:02x}{:02x}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.color = new_color
        canvas.itemconfig(self.mae, fill=new_color)
        
    def move(self, canvas):
        if self.mae is not None:
            canvas.delete(self.mae)
    
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        self.draw(canvas)
        
        if self.x >= canvas.winfo_width() - 20:
            self.dx = -1
            self.color_change(canvas)
        
        if self.x <= 20:
            self.dx = +1
            self.color_change(canvas)
            
        if self.y >= canvas.winfo_height() - 20:
            self.dy = -1
            self.color_change(canvas)
            
        if self.y <= 20:
            self.dy = +1
            self.color_change(canvas)
            
    def draw(self, canvas):
        self.mae = canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)
        
class Rectangle(Ball):
    def draw(self, canvas):
                self.mae = canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)
                
class Triangle(Ball):
    def draw(self, canvas):
                self.mae = canvas.create_polygon(self.x, self.y - 20, self.x + 20, self.y + 20, self.x - 20, self.y + 20, fill = self.color, width = 0)
                
balls = [Ball(400, 10, 1, 1, "red"),
Ball(300, 131, 1, 1, "green"),
Triangle(200, 282, 1, 1, "orange"),
Rectangle(100, 303, 1, 1, "blue")]

def loop():
    for b in balls:
        b.move(canvas)
    root.after(10, loop)

root=tk.Tk()
root.geometry("600x400")
    
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x=0, y=0)

root.after(10, loop)

root.mainloop()
