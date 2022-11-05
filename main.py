import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

len_password = nr_letters + nr_symbols + nr_numbers

total_letters = 0
total_symbols = 0
total_numbers = 0
password = ""

while total_letters + total_numbers + total_symbols != len_password:
  order = random.randint(1,3)
  
  if order == 1 and total_letters < nr_letters :
    random_letter = random.randint(0,51)
    password += letters[random_letter]
    total_letters += 1
  
  if order == 2 and total_numbers < nr_numbers:
    random_number = random.randint(0,9)
    password += numbers[random_number]
    total_numbers += 1
  
  if order == 3 and total_symbols < nr_symbols:
    random_symbol = random.randint(0,8)
    password += symbols[random_symbol]
    total_symbols += 1

print(f"Your password is : {password}")
