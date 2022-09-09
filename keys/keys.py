#!/usr/local/bin/python3

import tkinter as tk

def main():
   root = tk.Tk()
   root.configure(background="grey")
   root.title("Keyboard")

   hello = tk.Label(root,text="None", bg="black",fg="white")
   hello.pack(pady=20,padx=20)
   root.bind("<Key>", lambda e:hello.config(text=e.char+"<"+e.keysym+">"))
   root.mainloop()

if(__name__=="__main__"):
   main()
