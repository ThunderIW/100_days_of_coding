import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def hard_level(nr_letters, nr_symbols, nr_numbers):
    password = []
    shuffled_password=""
    for i in range(0, nr_letters + 1):
        password.append(random.choice(letters))


    for j in range(0, nr_symbols + 1):
        password.append(random.choice(symbols))

    for k in range(0, nr_numbers + 1):
        password.append(random.choice(numbers))
    random.shuffle(password)
    for i in password:
        shuffled_password += i

    return shuffled_password



def easy_level(nr_letters, nr_symbols, nr_numbers):
    password = ""
    for i in range(0, nr_letters + 1):
        password += random.choice(letters)

    for j in range(0, nr_symbols + 1):
        password += random.choice(symbols)

    for k in range(0, nr_numbers + 1):
        password += random.choice(numbers)
    return password


#print(f"{}"easy_level(nr_letters, nr_symbols, nr_numbers))
print(f"Your new password is: {hard_level(nr_letters, nr_symbols, nr_numbers)}")
