def calculations(num1, num2):
    sum = int(num1) + int(num2)
    multiple = int(num1) * int(num2) 
    return sum, multiple 
sum, multiple = calculations((input("Please enter a number: ")), ((input("Please enter another number: "))))
