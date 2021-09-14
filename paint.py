###Write an algorithim that will calculate the amount of paint required to paint a room. The user will enter the dimensions of the room, the total dimensions of the unpaintable areas (such as windows, doors or brickwork) and the number of coats of paint required. Assume that 1 litre of paint covers 11sq m.

print("Welcome to Yusuf's painting services. Please enter the height, length and width of the room in metres.")
height = int(input())
length = int(input())
width = int(input())

print("Please enter the combined dimensions of any 'unpaintable' areas: i.e windows, doors or brickwork, assumed to be in sqm.")
unpaintable = int(input())
print("Please enter how many coats of paint you want.")
coats = int(input)
totalDimension = ((height * length)*2) + ((height * width)*2) + ((width*length)*2) #Calculates the total surface area of the room
totalPaintable = totalDimension - unpaintable #Calculates how much of the room is actually paintable
totalPaint = ((totalPaintable/11))*2 + 1 #  How much paint is actualy needed multiplied by how many coats of paint the user wants. 
