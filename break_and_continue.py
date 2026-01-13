terminate = False
while not terminate:
    number1 = input("Please enter a number: ")
    number1 = int(number1)
    number2 = input("Please enter another number: ")
    number2 = int(number2)

    while True:
        operation = input("Please enter add/sub/def/mul or  quite to exit: ")
        if operation == "quite":
            terminate = True
            break
        if operation not in ["add", "sub", "mul", "def"]:
            print("Unknown command!")
            continue
        if operation == "add":
            print("Result is", number1 + number2)
            break
        if operation == "sub":
            print("Result is", number1 - number2)
            break
        if operation == "def":
            print("Result is", number1 / number2)
            break
        if operation == "mul":
            print("Result is", number1 *  number2)
            break
