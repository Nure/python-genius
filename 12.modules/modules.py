def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient. Handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def remainder(a, b):
    """Returns the remainder (modulus)."""
    if b == 0:
        return "Error: Cannot calculate remainder of zero"
    return a % b


name = 'Nure'