#!/usr/local/bin/python3

import tkinter as tk

def main():
   root = tk.Tk()
   root.configure(background="grey")
   root.title("Hello, World!")

   hello = tk.Label(root,text="Hello, World!",bg="black",fg="white")
   hello.pack(pady=20,padx=20)

   root.mainloop()

if(__name__=="__main__"):
   main()
