num = input("Please input a number between 100 and 999.")
while len(num) != 3:
    num = input("Invalid selection. Please input a number between 100 and 999.")
hundred = int(num)//100
tens = int(num)//10 - (hundred * 10)
units = int(num)//100 - (hundred * 100) - (tens * 10)
print(str(hundred) + ' hundreds,' + str(tens) + ' tens and ' + str(units) + ' units.')
