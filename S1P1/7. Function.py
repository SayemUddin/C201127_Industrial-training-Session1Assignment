def factorial(n):
    """Calculates the factorial of a number."""
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    except Exception as e:
        print(f"Error: {e}")

# Test the function
print(factorial(5))  # Output: 120
print(factorial(-1))  # Output: Error: Factorial is not defined for negative numbers.
