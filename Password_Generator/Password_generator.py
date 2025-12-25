import random
matrix="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
def passGenerator():
    password=""
    passFor=input("Password is for:-")
    passLength=int(input("Enter the length of password you want:-"))   
    for i in range(0,passLength):
        tem=random.choice(matrix)
        password+=tem
    with open("pass.txt","a") as file:
        file.write(passFor+":-" + password + "\n")
    return password
passGenerator()


