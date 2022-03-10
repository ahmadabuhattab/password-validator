"""
Author: Ahmad Abu Hattab
Date: 03/09/2022
Password Validator
"""


run_once = 0  # Cool code I figured out
special_characters = "!@#$%^&*()-+?_=,<>/"
#input
password = input("Enter a password? ")

#proccess
while len(password) > 8 and len(password) < 32: #Checks for length
    while any(c in special_characters for c in password):  #Checks for special character
        while any(x.isupper() for x in password): # Checks if its upper case
            while any(x.islower() for x in password): # Checks if its lower case
                while any(x.isdigit() for x in password): # Checks if its a digit
                    if run_once == 0:
                        print("Creating account now...")
                        run_once = 1
                else:
                    # Output
                    if run_once == 0:
                        print('At least one number')
                        run_once = 1
            else:
                # Output
                if run_once == 0:
                    print('At least one lowercase letter')
                    run_once = 1
        else:
            # Output
            if run_once == 0:
                print('At least one uppercase letter')
                run_once = 1
    else:
        # Output
        if run_once == 0:
            print("At least one symbol")
            run_once = 1
else:
    # Output
    if run_once == 0:
        print("Password needs to be longer than 8 letters and shorter than 32 letters")
        run_once = 1
