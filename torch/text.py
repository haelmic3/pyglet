#!/usr/local/bin/python3
import tkinter as tk
import numpy as np

#TODO record keyboard input and append to content array and update the display. Maybe add a scroll.

def main():
  root = tk.Tk()
  label = tk.Label(root,text="None",bg="black",fg="white",padx=20,pady=20)
  # array = np.arange(256).reshape(32,8)
  text = "Hello, World!"
  label.config(text=text)
  label.pack()
  # root.bind("<Key>", lambda e:root.destroy())
  tk.Button(root,text="Exit",command=root.destroy).pack()
  root.mainloop()

if __name__ == "__main__":
  main()
