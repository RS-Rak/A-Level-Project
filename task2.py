def getPword(attempt):
    #function for entering the password.
    if attempt == 1:
        #checks if its on the first attempt or not
        print("Enter password:")
        password = str(input())
        while (len(password) < 6) or (len(password) > 8):
            #Checks that the password length is between 6 and 8 inclusive
            print("Error. password must be 6 to 8 characters long.")
            password = str(input())
        attempt = 2
    if attempt == 2:
        print("Enter password again:")
        password2 = str(input())
        #Since we're comparing the two soon, we don't need to check the length now 
        return password, password2

attempt = 1
pass1, pass2 = getPword(attempt)
while pass1 != pass2:
    #If the passwords don't match, it repeats the function untill they do. 
    print("Error - passwords do not match.")
    attempt = 1
    pass1, pass2 = getPword(attempt)
print("Password change successful.")