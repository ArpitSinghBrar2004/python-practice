# Function to generate Fibonacci sequence
def fibonacci(n):
    fibonacci_sequence = []  # List to store the sequence
    a, b = 0, 1  # Initialize the first two terms

    # Generate the sequence
    for _ in range(n):
        fibonacci_sequence.append(a)  # Add the current term to the list
        a, b = b, a + b  # Update the terms for the next iteration

    return fibonacci_sequence

# Input: Number of terms
num = int(input("Enter the number of terms: "))

# Generate and print the Fibonacci sequence
if num <= 0:
    print("Please enter a positive integer.")
else:
    fib_sequence = fibonacci(num)
    print("Fibonacci sequence:")
    print(", ".join(map(str, fib_sequence)))