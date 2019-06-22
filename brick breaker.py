from tkinter import *
import random
import time
class ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts=[-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.current_score = self.canvas.create_text(250, 10, fill="#808080", font="Arial 12", text="Score:")
        self.canvas.pack()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2

class paddle:
        def  __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(5, 5, 100, 20 , fill=color)
            self.canvas.move(self.id, 200, 300)
            self.x = 0
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            elif pos[2] >= self.canvas_width:
                self.x = 0

        def turn_left(self, evt):
            self.x = -3
        def turn_right(self, evt):
            self.x = 3
class bricks:
        def  __init__(self, canvas, color):
        
            self.canvas = canvas
            canvas.create_rectangle(95, 50, 40, 70, fill=color)
            canvas.create_rectangle(150, 50, 100, 70, fill=color)
            canvas.create_rectangle(205, 50, 155, 70, fill=color)
            canvas.create_rectangle(260, 50, 210, 70, fill=color)
            canvas.create_rectangle(315, 50, 265, 70, fill=color)
            canvas.create_rectangle(370, 50, 320, 70, fill=color)
            canvas.create_rectangle(425, 50, 375, 70, fill=color)
            canvas.create_rectangle(485, 50, 430, 70, fill=color)
class metals:
        def __init__(self, canvas, color):
            self.metal = canvas
            canvas.create_rectangle(95, 80, 40, 100, fill=color)
            canvas.create_rectangle(150, 80, 100, 100, fill=color)
            canvas.create_rectangle(205, 80, 155, 100, fill=color)
            canvas.create_rectangle(260, 80, 210, 100, fill=color)
            canvas.create_rectangle(315, 80, 265, 100, fill=color)
            canvas.create_rectangle(370, 80, 320, 100, fill=color)
            canvas.create_rectangle(425, 80, 375, 100, fill=color)
            canvas.create_rectangle(485, 80, 430, 100, fill=color)
class normal:
        def __init__(self, canvas, color):
            self.metal = canvas
            canvas.create_rectangle(95, 110, 40, 130, fill=color)
            canvas.create_rectangle(150, 110, 100, 130, fill=color)
            canvas.create_rectangle(205, 110, 155, 130, fill=color)
            canvas.create_rectangle(260, 110, 210, 130, fill=color)
            canvas.create_rectangle(315, 110, 265, 130, fill=color)
            canvas.create_rectangle(370, 110, 320, 130, fill=color)
            canvas.create_rectangle(425, 110, 375, 130, fill=color)
            canvas.create_rectangle(485, 110, 430, 130, fill=color)
class exploding:
        def __init__(self, canvas, color):
            self.metal = canvas
            canvas.create_rectangle(95, 140, 40, 160, fill=color)
            canvas.create_rectangle(150, 140, 100, 160, fill=color)
            canvas.create_rectangle(205, 140, 155, 160, fill=color)
            canvas.create_rectangle(260, 140, 210, 160, fill=color)
            canvas.create_rectangle(315, 140, 265, 160, fill=color)
            canvas.create_rectangle(370, 140, 320, 160, fill=color)
            canvas.create_rectangle(425, 140, 375, 160, fill=color)
            canvas.create_rectangle(485, 140, 430, 160, fill=color)
tk = Tk()
tk.title('MSM')
tk.resizable(width=False, height=False)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400)
canvas.pack()


tk.update()
bricks = bricks(canvas, '#0080ff')
metals = metals(canvas, '#808080')
normal = normal(canvas, '#00ff00')
exploding = exploding(canvas, '#ff0000')
paddle = paddle(canvas, '#808080')
ball = ball(canvas, paddle, '#0080ff')


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


tk.mainloop()
