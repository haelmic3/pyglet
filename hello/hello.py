import tkinter as tk

root = tk.Tk()

#FIXME uses system background but not system text color so black on black is possible

hello = tk.Label(root, text="Hello, World!").pack()

root.mainloop()
