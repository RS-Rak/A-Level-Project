def multiples(name, table, start, end):
    print("Hi, " + name + " ... here is your times table.")
    for i in range(start, end + 1):
        print(str(table) + " * " + str(i) + " = " + str(table * i))
        # This looks a little complicated. What it does is write out a calculation for times table in the form x * y = z. start and end mark the upper and lower limit for y. 

pupilName = str(input("What is your name? "))
print("Please enter times table, start number and end number.")
table = int(input())
startnum = int(input())
endnum = int(input())
multiples(pupilName, table, startnum, endnum)

