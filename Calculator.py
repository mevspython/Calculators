#Present the user with the list of mathematical options.
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

#Gather user input/store them into variables.
choice = input("Enter your selection: ")
##we are converting to float, should user put in decimal and for functionality later
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

#Performing operation on numbers user inputs (known as entering logic)
#using if conditional statement

if choice == "1":
    print(num1, " + ", num2, "=", (num1+num2))

elif choice == "2":
    print(num1, " - ", num2, "=", (num1-num2))

elif choice == "3":
    print(num1, " * ", num2, "=", (num1*num2))

elif choice == "4":
    if num2 ==0.0:
        print("Divide by 0 Error")
    else:
        print(num1, " / ", num2, "=", (num1/num2))

else:
    print("Invalid Choice")