#This is a comment
import random
password = ""
while True:
    password_length = input("How long you want password: ")
    if int(password_length) > 0 and int(password_length) <= 10:
        break
for i in range(10):
    random_integer = random.randint(33,126)
    password += chr(random_integer)
print(password, len(password))
