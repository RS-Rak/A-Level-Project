num = int(input("Please enter a number between 1 and 10"))
while num > 10 or num < 0:
    num = int(input("Invalid number. Please enter a number between 1 and 10."))
for x in range(10):
    print(num * (x + 1))

#Gives the times table of a number
