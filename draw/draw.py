import tkinter as tk
from tkinter import colorchooser

class SketchBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sketchbook")
        
        # Set up canvas
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Variable to track the drawing color
        self.current_color = "black"
        
        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Add color button
        self.color_button = tk.Button(self.root, text="Choose Color", command=self.change_color)
        self.color_button.pack()

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self.current_color, outline=self.current_color)

    def reset(self, event):
        # Reset drawing state (optional)
        pass
    
    def change_color(self):
        color_code = colorchooser.askcolor(title="Choose Color")[1]
        if color_code:
            self.current_color = color_code

# Set up the main window
root = tk.Tk()
app = SketchBookApp(root)
root.mainloop()
