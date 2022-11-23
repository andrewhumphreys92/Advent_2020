import csv
import sys

if len(sys.argv) != 2:
    sys.exit("PASSPORTS?!?!")

passports = []

with open(sys.argv[1], "r") as f:
    reader = f.readlines()
    for x in range(0, len(reader)):
        passports.append({})
        for line in reader:
            if line != '\n':
                datalist = line.split()
                for i in range(0, len(datalist)):
                    tuple = datalist[i].split(":")
                    passports[x] = dict(tuple)

print(passports)