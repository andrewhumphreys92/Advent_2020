import sys


if len(sys.argv) != 2:
    sys.exit("Include the Text, Dummy!")

file = open(sys.argv[1], "r")
numbertext = file.readlines()
numbers = []

for text in numbertext:
    numbers.append(int(text))

for number1 in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if (number1 + number2 + number3 == 2020):
                print(number1,"+", number2, "+", number3,  "=", "2020")
                print(number1,"x", number2, "x", number3,  "=", number1*number2*number3)
                with open('Answer.txt' , 'w') as f:
                    f.write(str(number1*number2*number3))


                sys.exit()