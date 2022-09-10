#!/usr/local/bin/python3
import tkinter as tk
import time

curtime = ""

def main():
  root = tk.Tk()
  root.title("Clock")
  lable = tk.Label(root, text="None", bg="black", fg="white", padx=40, pady=20)
  lable.pack()
  def tick():
    global curtime
    newtime = time.strftime("%H:%M:%S")
    if newtime != curtime:
      curtime = newtime
      lable.config(text=curtime)
    root.after(200,tick)
  tick()
  root.mainloop()

if __name__ == "__main__":
  main()
