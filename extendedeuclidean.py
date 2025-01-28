def extended_euclidean(a, b):
    """
    Extended Euclidean Algorithm
    Returns gcd(a, b), x, y such that ax + by = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

if __name__ == "__main__":
    try:
        # Take input from the user
        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))

        # Compute the Extended Euclidean Algorithm
        gcd, x, y = extended_euclidean(a, b)

        # Display the results
        print(f"GCD of {a} and {b} is: {gcd}")
        print(f"Coefficients x and y such that {a}x + {b}y = {gcd} are: x = {x}, y = {y}")
    except ValueError:
        print("Please enter valid integers.")
