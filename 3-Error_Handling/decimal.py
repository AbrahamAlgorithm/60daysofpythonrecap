try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    formatted_result = "{:.2f}".format(result)
    print(f"Result of {num1} divided by {num2}: {formatted_result}")
