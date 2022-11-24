import csv
import sys

if len(sys.argv) != 2:
    sys.exit("PASSPORTS?!?!")

passports = [{}]
datalist = [[]]
datapairs = []
x = 0
totalpassports = 0
with open(sys.argv[1], "r") as f:
    reader = f.readlines()
    for line in reader:
        if line != '\n':
            datalist[x] = line.split()
            for i in range(0, len(datalist[x])):
                datapairs.append(datalist[x][i].split(":"))
            passports[x] = dict(datapairs)
        else:
            x += 1
            datapairs.clear()
            passports.append({})
            datalist.append([])

for i in range(0, len(passports)):
    if "byr" in passports[i] and "iyr" in passports[i] and "eyr" in passports[i] and "hcl" in passports[i] and "hgt" in passports[i] and "ecl" in passports[i] and "pid" in passports[i]:
        totalpassports += 1

print(totalpassports)