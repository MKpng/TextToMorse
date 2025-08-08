from morse import morse_dict
import winsound
import time
from tkinter import *
from tkinter import ttk
import sv_ttk

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
root.title("ToMorse")
frame = ttk.Frame(root)
window_width = 500
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
frame.grid(column=3, row=3)

input_label = ttk.Label(frame, text="Covert your sentence to MORSE", font=("Helvetica", 12, "bold"))
input_label.grid(column=2, row=0, pady=(50, 30), padx=130)
morsed = ttk.Entry(width=35)
morsed.grid(column=3, row=4, pady=(0, 30))
click = ttk.Button(text="PLAY", command=get_morse)
click.grid(column=3, row=5)

sv_ttk.set_theme("dark")
root.mainloop()