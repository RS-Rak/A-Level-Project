import os, time, sys

def clear():
    os.system('cls')

def menu():
    print("Please select what you'd like to do. 1-5")
    while True:
        numbers = ["1","2","3","4","5","6"]
        print("1. Place a car")
        print("2. Remove a car")
        print("3. Display the grid")
        print("4. Reset the grid")
        print("5. Exit")
        print("6. Change the delay times")
        choice = str(input())
        if choice in numbers:
            clear()
            break
        else:
            clear()
            print("Invalid choice!")
            print("")
    return choice

def chooseSpace():
    reg = input("Please enter your car's reg number.")
    row = int(input("Please enter the row you'd like your car to be in, 1 to 10. "))
    col = int(input("Please enter the column you'd like to be in, 1 to 6."))
    clear()
    return reg, row, col 

def setUpPark():
    park = []
    park = [[None for i in range(6)] for j in range(10)]
    #Little complex. What it does is fill in the entire list with None values, so that I can then assign the value positions to be "empty" instead. 

    for i in range(0, 10):
        for x in range(0,6):
            park[i][x] = "empty"
    #This fills the parking grid with empty spaces as none of them are occupied. 

    clear()
    return park

def placeCar(park):
    while True:
        reg, row, col = chooseSpace()
        # Calls the function. 

        if ((row <= 10) and (row >= 1)) and ((col <= 6) and (col >= 1)):
            #Error checking. Makes sure the row,col selection is within acceptable values.

            if park[row -1][col-1] == "empty":
                #If it is, it checks if it is empty. If that is also true, it assigns the space to the car and then breaks from the loop.
                park[row - 1][col -1] = reg
                print("Successful!")
                time.sleep(4)
                return park
            else:
                print("This space is occupied!")
                time.sleep(sleepTime)
                clear()
        else:
            print("Invalid space! Please re-enter.")
            clear()

def removeCar(park):
    while True:
        print("Please enter the row of the car you would like to remove. ")
        row = int(input())
        print("Please enter the column of the car you'd like to remove.")
        col = int(input())
        if ((row <= 10) and (row >= 1)) and ((col <= 6) and (col >= 1)):
                #Error checking. Makes sure the row,col selection is within acceptable values.

                if park[row -1][col-1] == "empty":
                    print("This space is empty!")
                    time.sleep(sleepTime)
                    clear()
                else:
                    park[row-1][col-1] = "empty"
                    print("Successful!")
                    time.sleep(sleepTime)
                    clear()
                    return park
        else:
            print("Invalid space! Please re-enter.")#
            time.sleep(sleepTime)
            clear()
def printGrid(park):
    for i in range(0,10):
            print(str(park[i]) + " ") 
    time.sleep(1.5 * sleepTime)
    #Prints the grid. 

sleepTime = 4
park = setUpPark()
while True:
    choice = menu()
    if int(choice) == 1:
        #This calls the function for placing a car
        park = placeCar(park)
        clear()
    elif int(choice) == 2:
        printGrid(park)
        park = removeCar(park)
        clear()
    elif int(choice) == 3:
        printGrid(park)
        clear()
    elif int(choice) == 4:
        park = setUpPark
        print("Grid has been reset.")
        time.sleep(delay)
        clear()
    elif int(choice) == 5:
        break  
    else:
        print("Enter the number of seconds you'd like delays to be")
        delay = int(input())
        sleepTime = delay
        clear()
sys.exit()
