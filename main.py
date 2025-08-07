from morse import morse_dict
import winsound
import time
from tkinter import *
from tkinter import ttk

def get_morse():
    value = morsed.get()

    morse = []
    for char in value.upper():
        if char in morse_dict:
            morse.append(morse_dict[char])

    morse = "".join(morse).rstrip(" ")

    for code in morse:
        if code == "○":
            winsound.Beep(700, 150)
        elif code == "▭":
            winsound.Beep(700, 450)
        elif code == "/":
            time.sleep(1.05)

root = Tk()
frame = ttk.Frame(root)
window_width = 600
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
frame.grid()

ttk.Label(frame, text="Covert the follow sentence to MORSE").grid(columnspan=3, row=0)
morsed = ttk.Entry()
morsed.grid(column=2, row=1)
click = ttk.Button(text="Convert", command=get_morse)
click.grid(column=2, row=2)
root.mainloop()