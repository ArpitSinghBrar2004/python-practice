num = int(input("Enter the number you want to check: "))
print(f"Number you entered: {num}")

if num > 1:
    is_prime = True  # Assume the number is prime initially
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            is_prime = False
            break  # Exit the loop as soon as we find a divisor
    if is_prime:
        print(f"{num} is a prime number.")
elif num == 1:
    print("1 is not a prime number.")
else:
    print("Please enter a positive integer greater than 1.")