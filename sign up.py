__author__ = "Yusa Erenci"

import time

print("------------------------------------")
print("Rock, Paper, Scissors Sign Up Screen")
print("------------------------------------")
while True:
    username = input("pick a username: ")
    password = input("pick a password: ")
    passwordConfirmation = input("please confirm your password: ")

    if password != passwordConfirmation:
        print("The passwords don't match. Please try again")
    else:
        print("You have signed up.\nYou can now play Rock, Paper, Scissors")
        text_file = open("accounts.txt", "a")
        text_file.write(username)
        text_file.write(" , ")
        text_file.write(password)
        text_file.write("\n")
        text_file.close()
        break

time.sleep(3)
