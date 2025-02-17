# Prints the welcome messege and the options the user can choose from
print("Welcome to the unit conversion tool. What would you like to convert?")
print("")
print("1. Temperature Conversion?")
print("2. Length Conversion?")
print("3. Weight Conversion?")
print("4. Binary/Decimal Conversion?")


# Get the users choice for what they would like to convert
choice = int(input("Enter your choice 1-4: "))
print("")
# Need this for the loop to run
choice2 = 0

# Loop until the user wants to quit
while choice2 != 4:
    if choice == 1:
        # Temperature Conversion
        print("You chose Temperature Conversion")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Choose a different conversion type")
        print("4. Quit")
        print("")

        # Get the users choice for what conversion they want
        choice2 = int(input("Enter your choice 1-4: "))
        print("")
        if choice2 == 1:
            # Fahrenheit to Celsius
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5.0 / 9.0
            print(fahrenheit, " is ", celsius, "C°")
            print("")
        elif choice2 == 2:
            # Celsius to Fahrenheit
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9.0 / 5.0) + 32
            print(celsius, " is ", fahrenheit, "F°")
            print("")
        elif choice2 == 3:
            # Lets the user choose a different conversion type if they want
            print("Where would you like to go instead?")
            print("1. Temperature Conversion?")
            print("2. Length Conversion?")
            print("3. Weight Conversion?")
            print("4. Binary/Decimal Conversion?")
            print("")
            choice = int(input("Enter your choice 1-4: "))
            print("")
        elif choice2 == 4:
            # Ends program
          break
        else:
            #Bruh
            print("bruh what, try again.")


    elif choice == 2:
        # Length Conversion
        print("You chose Length Conversion")
        print("1. Feet to Inches")
        print("2. Inches to Feet")
        print("3. Choose a different conversion type")
        print("4. Quit")
        print("")
        choice2 = int(input("Enter your choice 1-4: "))
        print("")
        if choice2 == 1:
            # Feet to Inches
            feet = float(input("Enter length in feet: "))
            inches = feet * 12
            print(feet, " is ", inches, "in")
            print("")
        elif choice2 == 2:
            # Inches to Feet
            inches = float(input("Enter length in inches: "))
            feet = inches / 12
            print(inches, " is ", feet, "ft")
            print("")
        elif choice2 == 3:
            # Lets the user choose a different conversion type if they want
            print("Where would you like to go instead?")
            print("1. Temperature Conversion?")
            print("2. Length Conversion?")
            print("3. Weight Conversion?")
            print("4. Binary/Decimal Conversion?")
            print("")
            choice = int(input("Enter your choice 1-4: "))
            print("")
        elif choice2 == 4:
            #ends program
            break
        else:
            #bruh2
            print("Bruh what, try again.")


    elif choice == 3:
        # Weight Conversion
        print("You chose Weight Conversion")
        print("1. Pounds to Kilograms")
        print("2. Kilograms to Pounds")
        print("3. Choose a different conversion type")
        print("4. Quit")
        print("")
        choice2 = int(input("Enter your choice 1-4: "))
        print("")
        if choice2 == 1:
            # Pounds to Kilograms
            pounds = float(input("Enter weight in pounds: "))
            kilograms = pounds * 0.453592
            print(pounds, " is ", kilograms, "kg")
            print("")
        elif choice2 == 2:
            # Kilograms to Pounds
            kilograms = float(input("Enter weight in kilograms: "))
            pounds = kilograms / 0.453592
            print(kilograms, "Weight in pounds: ", pounds, "lbs")
            print("")
        elif choice2 == 3:
            # Lets the user choose a different conversion type if they want
            print("Where would you like to go instead?")
            print("1. Temperature Conversion?")
            print("2. Length Conversion?")
            print("3. Weight Conversion?")
            print("4. Binary/Decimal Conversion?")
            print("")
            choice = int(input("Enter your choice 1-4: "))
            print("")
        elif choice2 == 4:
            #ends program
            break
        else:
            #bruh3
            print("Bruh what, try again.")


    elif choice == 4:
        # Binary/Decimal Conversion
        print("You chose Binary/Decimal Conversion")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Choose a different conversion type")
        print("4. Quit")
        print("")
        choice2 = int(input("Enter your choice 1-4: "))
        print("")
        if choice2 == 1:
            # Decimal to Binary
            decimal = int(input("Enter a decimal number: "))
            print("Binary: ", bin(decimal))
            print("")
        elif choice2 == 2:
            # Binary to Decimal
            binary = input("Enter a binary number: ")
            print("Decimal: ", int(binary, 2))
            print("")
        elif choice2 == 3:
            # Lets the user choose a different conversion type if they want
            print("Where would you like to go instead?")
            print("1. Temperature Conversion?")
            print("2. Length Conversion?")
            print("3. Weight Conversion?")
            print("4. Binary/Decimal Conversion?")
            print("")
            choice = int(input("Enter your choice 1-4: "))
            print("")
        elif choice2 == 4:
            #ends program
            break
        else:
            #burh4
            print("Beuh what, try again.")

    else:
        #bruh5
        print("ERROR",  sep="**")

#says bye to the user
print("k bye")
