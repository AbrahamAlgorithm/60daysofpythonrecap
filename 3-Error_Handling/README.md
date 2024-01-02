# Day 3: Exception Handling, Do-While, Math Operations, Floats, Strings, and More

Welcome to Day 3 of my 60 Days of Python Recap journey! 🚀 On this day, I explored a diverse set of topics, including exception handling, do-while (or similar constructs), math operations, float manipulation, and string handling.

## Key Concepts Covered

### 1. Exception Handling

Exception handling is crucial for writing robust and error-tolerant code. I delved into how to use `try`, `except`, `finally`, and `else` blocks to handle exceptions gracefully.

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No exceptions occurred.")
finally:
    print("This block always executes.")
```

### 2. Do-While (or Similar Constructs)

In Python, there isn't a built-in `do-while` loop, but I explored similar constructs to achieve the same functionality.

Example:
```python
while True:
    # Code block
    if condition:
        break
```

### 3. Math Operations

Python provides a rich set of mathematical operations. I covered basic arithmetic operations, as well as some advanced functions from the `math` module.

Example:
```python
import math

result = math.sqrt(25)
print(result)
```

### 4. Float Manipulation

Understanding how to work with floating-point numbers is essential. I explored concepts like rounding, formatting, and precision control.

Example:
```python
num = 3.14159
rounded_num = round(num, 2)
print(rounded_num)
```

### 5. String Handling

String manipulation is a fundamental skill. I covered string concatenation, formatting, slicing, and explored various string methods.

Example:
```python
name = "John"
greeting = f"Hello, {name}!"
print(greeting)
```

## Coding Exercises

To reinforce my learning, I tackled coding exercises related to the concepts covered on Day 3. The solutions are available in the "code" directory.

1. **Exception Handling Exercise:**
   - Handle a specific exception and provide a meaningful message.

2. **Do-While Simulation Exercise:**
   - Simulate the behavior of a `do-while` loop using a `while` loop.

3. **Math and Float Exercise:**
   - Perform a mathematical operation involving floats and format the result.

4. **String Manipulation Exercise:**
   - Create a formatted string using variables.

Feel free to explore the code and provide feedback or suggestions!

## Resources

- [Python Documentation on Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python `math` Module Documentation](https://docs.python.org/3/library/math.html)
