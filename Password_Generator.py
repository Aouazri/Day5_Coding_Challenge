#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pwd=""
for char in range(nr_letters):
  pwd+= random.choice(letters)
for char in range(nr_symbols):
  pwd+=random.choice(symbols)
for char in range(nr_numbers):
  pwd+=random.choice(numbers)
print(f"Your non-randomised(weak) password would be: {pwd}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list=[]

for i in range(nr_letters):
  password_list.append(random.choice(letters))
for i in range(nr_numbers):
  password_list.append(random.choice(numbers))
for i in range(nr_symbols):
  password_list.append(random.choice(symbols))

#get the list in random order 
random.shuffle(password_list)

password=""
for character in password_list:
  password+= character
print(f"Your randomised(strong) password would be: {password}")