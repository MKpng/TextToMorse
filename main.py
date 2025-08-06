from morse import morse_dict

user_input = str(input("Covert the follow sentence to MORSE: ")).upper()

morsed = []
for char in user_input:
    if char in morse_dict:
        morsed.append(morse_dict[char])

print("".join(morsed).rstrip(" "))