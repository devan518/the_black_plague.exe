from PIL import Image, ImageTk
import time
import threading
import multiprocessing
import os
import tkinter as tk
from tkinter import ttk, messagebox

def receive_the_plague():
    def spawn_window(img):
        win = tk.Toplevel()
        win.attributes("-fullscreen", True)
        win.configure(background="black")

        label = tk.Label(win, image=img, bg="black")
        label.pack(expand=True, fill="both")

    def spam_windows():
        root = tk.Tk()
        root.withdraw()  # hide main window

        # load pic once
        pic = ImageTk.PhotoImage(Image.open("plague.jpg"))

        while True:
            spawn_window(pic)
            time.sleep(0.1)

    threading.Thread(target=spam_windows).start()
    tk.mainloop()

if __name__ == "__main__":
    def open_main_window():
        main = tk.Toplevel()
        
        
        main.title("t̶̢̅͆̆̄́̈́h̸̛̠̭̮̖̖̥̱͙̺͖̿̏̀̐͌̑͝e̶̡̞͉͇̯͚̙̪̓̉̀̆̓͐̈̕̕ ̸̛̘̀́̏̔͘b̷͎̬̰̮̠̞͓̲́̎ĺ̶̰̞̜͎̬̼̭͆̉̀̌̄̓̈́̚͜ȁ̵̞̬͖͔̬̽̌̈́͆̿͂͝c̶̦̹͈͖̤͚̖̪̪̑k̵̛͓͚͗̏̍̿̽̈́̓́͝ ̴̢̃̅͒͘p̸̢̛̜̰̱̬̹̻͖̞͆̊͂̔͐̄̓̀̚͜l̶̲̰̫̊͊͛̒̉̿͐̈́̀͘ã̴̲͈͠ģ̴͔̮͉̜͖̞̂͐̀͗̒̆͂̚ͅu̶̠̺̱͇̱̝̝͔̘̓̋͒̒̕ͅe̷̛̥̖͙̮̙͖͐̈́͂̌̽͂̌̚͜͠")
        
        
        main.geometry("400x200")

        frame = ttk.Frame(main, padding="20")
        frame.pack(expand=True, fill='both')

        label = ttk.Label(frame, text="Press the button below to receive the black plague...")
        label.pack(pady=10)

        button = ttk.Button(frame, text="i choose to receive the black plague", command=receive_the_plague)
        button.pack(pady=20)

    root = tk.Tk()
    root.title("Terms & Conditions Agreement")
    root.geometry("500x400")

    frame = ttk.Frame(root, padding=10)
    frame.pack(expand=True, fill='both')

    #i swear bro on god  this is the only part where i use ai
    terms_text = """
    TERMS & CONDITIONS — Experimental CPU Stress Test
    Last Updated: 11/28/25

    This program is an experimental system test for educational purposes only.
    By clicking "I Agree", you acknowledge:

    • You understand this program may behave unpredictably.
    • You take full responsibility for running it.
    • You are using this program willingly and on a device you own.

    If you do NOT accept these terms, press "I Do Not Agree" and the program will close.
    """
    #phew ok thats it

    text_box = tk.Text(frame, wrap='word', height=15)
    text_box.insert('1.0', terms_text)
    text_box.config(state='disabled')
    text_box.pack(fill='both', expand=True)

    scroll = ttk.Scrollbar(frame, command=text_box.yview)
    text_box['yscrollcommand'] = scroll.set
    scroll.pack(side='right', fill='y')

    button_frame = ttk.Frame(frame)
    button_frame.pack(pady=10)

    def agree():
        root.withdraw()
        open_main_window()


    def disagree():
        messagebox.showinfo("Terms Not Accepted", "You must accept the terms to continue.")
        root.destroy()

    agree_button = ttk.Button(button_frame, text="I Agree", command=agree)
    agree_button.grid(row=0, column=0, padx=10)

    disagree_button = ttk.Button(button_frame, text="I Do Not Agree", command=disagree)
    disagree_button.grid(row=0, column=1, padx=10)

    root.mainloop()


    
