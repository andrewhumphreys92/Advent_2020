import sys

if len(sys.argv) != 2:
    sys,exit("Don't forget your file!")

file = open(sys.argv[1], "r")
rawdata = file.readlines()
passwords = []
lettercounter = 0
counter = 0
minimum = 0
maximum = 0
letter = "a"
minmax = ""
for password in rawdata:
    passwords.append(password.split())

for user in range(len(passwords)):
    minmax = passwords[user][0].split("-")
    minimum = int(minmax[0])
    maximum = int(minmax[1])
    letter = passwords[user][1][0]
    #print(passwords[user], minimum, maximum, letter)
    for letters in range(len(passwords[user][2])):
        if letter in passwords[user][2][letters]:
            lettercounter = lettercounter + 1

    if lettercounter in range(minimum, maximum + 1):
        counter = counter + 1

    lettercounter = 0

print("Total Valid Passwords:", counter)