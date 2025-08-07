import time

from morse import morse_dict
import winsound

user_input = str(input("Covert the follow sentence to MORSE: ")).upper()

morsed = []
for char in user_input:
    if char in morse_dict:
        morsed.append(morse_dict[char])

morsed = "".join(morsed).rstrip(" ")

for code in morsed:
    if code == "○":
        winsound.Beep(700, 150)
    elif code == "▭":
        winsound.Beep(700, 450)
    elif code == "/":
        time.sleep(1.05)
print(morsed)

