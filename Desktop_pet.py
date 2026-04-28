import tkinter as tk
import time
import sys
import os

class pet():
    def __init__(self):
        self.window = tk.Tk()
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        gif_path = os.path.join(base_path, 'assets', 'Anissa.gif')

        self.walking_right = []
        for i in range(120):
            try:
                frame = tk.PhotoImage(file=gif_path, format=f'gif -index {i}')
                self.walking_right.append(frame)
            except tk.TclError:
                break

        if not self.walking_right:
            raise Exception("No se pudieron cargar los frames del GIF.")
        
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        self.timestamp = time.time()

        self.window.config(highlightbackground='black')

        self.window.overrideredirect(True)

        self.window.attributes('-topmost', True)

        self.window.wm_attributes('-transparentcolor', 'black')

        self.label = tk.Label(self.window, bd=0, bg='black')

        self.x = 0
        self.y = 0

        self.width = self.walking_right[0].width()
        self.height = self.walking_right[0].height()

        self.window.geometry(f'{self.width}x{self.height}+{int(self.x)}+0')

        self.label.configure(image=self.img)

        self.label.pack()

        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):

        mouse_x = self.window.winfo_pointerx()
        mouse_y = self.window.winfo_pointery()

        dx = mouse_x - (self.x + self.width // 2)
        dy = mouse_y - (self.y + self.height // 2)
 
        self.x += dx * 0.01
        self.y += dy * 0.01
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            self.frame_index = (self.frame_index + 1) % len(self.walking_right)
            self.img = self.walking_right[self.frame_index]

        self.window.geometry(
            f'{self.width}x{self.height}+{int(self.x)}+{int(self.y)}'
        )

        self.label.configure(image=self.img)

        self.label.pack()

        self.window.after(10, self.update)

pet()