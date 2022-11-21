import sys

if len(sys.argv) != 2:
    sys,exit("Don't forget your file!")

file = open(sys.argv[1], "r")
rawdata = file.readlines()
passwords = []
lettercounter = 0
counter = 0
firstlocation = 0
secondlocation = 0
letter = "a"
minmax = ""
for password in rawdata:
    passwords.append(password.split())

for user in range(len(passwords)):
    minmax = passwords[user][0].split("-")
    firstlocation = int(minmax[0]) - 1
    secondlocation = int(minmax[1]) - 1
    letter = passwords[user][1][0]
    if passwords[user][2][firstlocation] == passwords[user][1][0] and passwords[user][2][secondlocation] != passwords[user][1][0] or passwords[user][2][firstlocation] != passwords[user][1][0] and passwords[user][2][secondlocation] == passwords[user][1][0]:
        counter = counter + 1

    lettercounter = 0

print("Total Valid Passwords:", counter)