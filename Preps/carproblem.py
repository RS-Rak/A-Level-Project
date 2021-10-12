
def chooseSpace():
    row = int(input("Please enter the row you'd like your car to be in, 1 to 10. "))
    col = int(input("Please enter the column you'd like to be in, 1 to 6."))
    return row, col 

park = []
park = [[None for i in range(6)] for j in range(10)]
#Little complex. What it does is fill in the entire list with None values, so that I can then assign the value positions to be "empty" instead. 

for i in range(0, 10):
    for x in range(0,6):
        park[i][x] = "empty"
#This fills the parking grid with empty spaces as none of them are occupied. 

reg = str(input("Please enter your car's reg number."))
while True:
    row, col = chooseSpace()
    # Calls the function. 

    if ((row <= 10) and (row >= 1)) and ((col <= 6) and (col >= 1)):
        #Error checking. Makes sure the row,col selection is within acceptable values.

        if park[row -1][col-1] == "empty":
            #If it is, it checks if it is empty. If that is also true, it assigns the space to the car and then breaks from the loop.
            park[row - 1][col -1] = reg
            break
        else:
            print("This space is occupied!")
    else:
        print("Invalid space! Please re-enter.")

for i in range(0,10):
        print(str(park[i]) + " ") 
#Prints the grid. 

