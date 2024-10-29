# Fence cost calculator in python
# Author: Kurt Medina
# Date: 30/10/2024
# Version: 1

def num_check(question):
    error_1 = "Please enter a number that is more that 0"
    error_2 = "Please enter a number"

    while True: 
        try:
            response = float(input(question))

            if response and response > 0:
                return response
            else:
                print(error_1)

        except ValueError:
            print(error_2)

keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    length = num_check("Length: ")
    cpm = num_check("Cost per meter: ") # cpm = cost per meter

    perimeter = 2 * (width + length)
    cost = perimeter * cpm

    print()
    print(f"Perimeter: {perimeter}m")
    print(f"Cost: ${cost}")

    keep_going = input("press enter to keep going or press any key to quit")
    print()

print("thanks for using the fence cost calculator! :D")