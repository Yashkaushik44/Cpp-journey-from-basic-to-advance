''' Our goal is to take two numbers and the action they want us to perform from user
and perform the calculation on the two numbers and give them the result'''

#menu
print("Enter 1 to perform addition")
print("Enter 2 to perfrom subtraction")
print("Enter 3 to perform multiplication")
print("Enter 4 to perfrom divide")

choice = int(input("Enter your choice: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))

match choice:

    case 1:

        print("The addition is: ", num1 + num2)

    case 2:

        print("The subtraction is:", num1 - num2)

    case 3:

        print("The multiplication is: ", num1 * num2)

    case 4:

        print("The quotent is: ", num1 / num2)
