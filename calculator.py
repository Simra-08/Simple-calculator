def calc():
    num1 = int(input("enter the first number: "))
    op = input("enter the operation: ")
    num2 = int(input("enter the second number: "))
    if op == "+":
        return (num1 + num2)
    elif op == "-":
        return (num1 - num2)
    elif op == "*":
        return (num1 * num2)
    elif op == "/":
        if num2 == 0:
            return "error: division by zero"
        else:
            return (num1 / num2)

    else:
        return ("invalid operation ")

result = calc()
print("the result of the calculation  is: ", result)