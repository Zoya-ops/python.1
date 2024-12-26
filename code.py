#password generator
import random
import string
pass_len = int(input("enter the length of your password you want : "))
char_values = string.ascii_letters + string.digits

password = ""
for i in range(pass_len):
    passw = random.choice(char_values)
    password += passw

print("your password is =",password)