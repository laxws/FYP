import random
import sys
import os

'''print("Hello World")

name = "Nabil Hakimi"
print(name)
name = "Nabil Hakimi Yusri"
print(name)
print('\n' * 5)

first = "Nabil"
last = "Hakimi"
msg = f'{first} {last} is a coder'
print(msg)


name = "Muhamad Nabil Hakimi Bin Yusri"
print('Nabil' in name)

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")

price = 1000000
has_a_good_credit = False

if has_a_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: {down_payment}")

has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

temp = 50
if temp != 30:
    print("Hot")
else:
    print("Cold")

name = "Jimmy"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 20:
    print("Name must be a maximum of 20 characters")
else:
    print("Name looks good !")

weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kg")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done!")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won !")
        break
else:
    print("Sorry, you failed!")

a = [3, 10, -1]
#print(a)
a.append(1)
#print(a)
a.append("Jimmy")
print(a)
a.append([1, 2])
print(a)
a.pop()
print(a)

a = ['banana', 'apple', 'kiwi']
for e in a:
    print(e)

a = [5, 10, 15]
total = 0
for numbers in a:
    total = total + numbers
print(total)

total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

given_list = [5, 4, 4, 3, 1]

total = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total += given_list[i]
    i += 1
print(total)

given_list = [5, 4, 4, 3, 1, -2, -3, -1]
total = 0
for numbers in given_list:
    if numbers <= 0:
        break
    total += numbers
print(total)

given_list = [5, 4, 4, 3, 1, -2, -3, -1]
total = 0
i = 0
while True:
    total += given_list[i]
    i += 1
    if given_list[i] <= 0:
        break
print(total)


def function(some_argument):
    print(some_argument)
    print("jimmy")


function(5)

a = [1, 2, 3, 4, 5]
c = []
for numbers in a:
    c.append(numbers * 2)
print(c)

d = [numbers * 2 for numbers in c]
print(d)

# [1, 4, 9, 16, 25, 36]
a = []
for x in range(1, 7):
    a.append(x ** 2)
print(a)

for x in range(6, 0, -1):
    print(x)

numbers = [5, 3, 4, 1, 2, 6, 7]
numbers.sort()
numbers.reverse()
print(numbers)

coordinates = [1, 2, 3]
x, y, z = coordinates
print(z)

phone = input("Phone:")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
for numbers in phone:
    output += digits_mapping.get(numbers, "!") + " "
print(output)

try:
    limit = 10
    name = input("Name: ")
    age = int(input("Age: "))
    unit = input("(MONTHS) or (YEAR): ")
    if unit.upper() == "MONTHS":
        age/12
    income = int(input("Income: "))
    calculation = income/age
    results = f'{name} has {calculation} risk'
    print(results)
except ZeroDivisionError:
    print("Age cannot be 0 !")
except ValueError:
    print("Invalid Value !")

i = 0
while i <= 10:
    print(i)
    i += 1
print("Done with loop !")

secret_word = "JIMMY"
secret_number = 3
word_guess = ""
number_guess = ""
guess_count = 0
guess_limit = 3
try:
    while guess_count < guess_limit:
        word_guess = input("Enter guess: ")
        number_guess = int(input("Enter guess: "))
        guess_count += 1
        if word_guess() == secret_word:
            print("You've won !")
            break
        #if number_guess() == secret_number:
            #print("You've won !")
    else:
        print("Sorry, you've failed !")
except ValueError:
    print("Please enter numbers only!")


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won !")
        break
else:
    print("Sorry, you failed!")


friend = ["Nabil", "Hakimi", "Yusri"]
for name in range(len(friend)):
    print(friend[name])


def raise_to_power(base_num, pow_num):
    results = 1
    for index in range(pow_num):
        results = results * base_num
    return results


print(raise_to_power(3, 6))'''

WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
word = random.choice(WORDS)
position = random.randrange(len(word))
jumble = ""
jumble += word[position]
print(jumble)
word = word[:position] + word[(position + 1):]
print(word)





























