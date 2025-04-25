num_one = float(input("Enter first number: "))
num_two = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter operation: ")

if op == '+':
    print("Result:", num_one + num_two)
elif op == '-':
    print("Result:", num_one - num_two)
elif op == '*':
    print("Result:", num_one * num_two)
elif op == '/':
    if num_two != 0:
        print("Result:", num_one / num_two)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation")
