try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid age.")
else:
    greeting_message = f"Hello, {name}! You are {age} years old."
    print(greeting_message)
