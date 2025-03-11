print("Welcome to your Calculator")
print("Enter the first number")
first_number = input()
print("Enter the second number")
second_number = input()
print("Enter the operation")
operation = input(["+", "-", "*", "/"])
if operation == "+":
    print(int(first_number) + int(second_number))
elif operation == "-":
    print(int(first_number) - int(second_number))
elif operation == "*":
    print((first_number) * (second_number))
elif operation == "/":
    print(float(first_number) / float(second_number))
else:
    print("Invalid operation")
print("Thank you for using your Calculator")