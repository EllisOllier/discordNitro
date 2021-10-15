import time
import os
import random
import string
print("Welcome to Discord Nitro Generator!")
print()
print("Developed by Fuze#8337")

amountCodes = int(input("Please enter how many discord nitro codes you want to generate: "))

for i in range(amountCodes):
    code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16))
    url = "https://discord.gift/" + code
    print(url)
    time.sleep(0.25)