from tensorflow.keras.models import load_model
import tkinter as tk
from tkinter import *
import numpy as np
import win32gui
from PIL import ImageGrab, Image, ImageOps

model = load_model('mnist.h7')
def prediction(img):
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape((1, 28, 28, 1))
    img = img/255.0
    res = model.predict([img])
    res = res[0]
    return np.argmax(res), max(res)
class App(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.x = self.y = 0
    self.Canvas=tk.Canvas(self, width=300, height=300.,bg='white', cursor ='cross')
    self.label = tk.Label(self, text='draw any thing using the cursor', font=('hervetical', 50))
    self.classification_button = tk.Button(self,text='click here for classify', command=self.classify_hand_written)
    self.clear_button = tk.Button(self,text='clear', command=self.clear)
    self.Canvas.grid(row=0, column=0, pady=0, sticky=W)
    self.label.grid(row=0, column=1, pady=2, padx=2)
    self.classification_button.grid(row=1, column=1, pady=2, padx=2)
    self.clear_button.grid(row=1, column=0, pady=2)
    self.Canvas.bind("<B1-Motion>", self.draw)
  def classify_hand_written(self):
    HWND = self.Canvas.winfo_id()
    rect = win32gui.GetWindowRect(HWND)
    im = ImageGrab.grab(rect)
    im = im.convert('L')
    im = ImageOps.invert(im)
    im = im.convert('1')
    digit, acc = prediction(im)
    self.label.configure(text=str(digit) + ',' + str(int(acc *100)) + "%")
  def clear(self):
    self.Canvas.delete('all')
  def draw(self,event):
    self.x = event.x
    self.y = event.y
    r = 8
    self.Canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black')
app = App()
mainloop()












