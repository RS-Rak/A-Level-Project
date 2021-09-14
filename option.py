option = input("Please choose a number between 1 and 3.")
while int(option) > 3 or int(option) < 1:
    option = input("Invalid choice. Please choose a number between 1 and 3.")
print("You have chosen option " + str(option))

#Keep choosing a number till you choose 1 between 1 and 3