import random
from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
# password = ""
# for i in range(0, nr_letters):
#     counter1 = random.choice(letters)
#     password += counter1
# for i in range(0, nr_symbols):
#     counter2 = random.choice(symbols)
#     password += counter2
# for i in range(0, nr_numbers):
#     counter3 = random.choice(numbers)
#     password += counter3
# print(f"Your password is: {password}")

#Hard Level
password = []
for i in range(0, nr_letters):
    counter1 = random.choice(letters)
    password.append(counter1)
for i in range(0, nr_symbols):
    counter2 = random.choice(symbols)
    password.append(counter2)
for i in range(0, nr_numbers):
    counter3 = random.choice(numbers)
    password.append(counter3)
random.shuffle(password)
final_password = ""
for i in password:
    final_password += i
print(f"Your password is: {final_password}")