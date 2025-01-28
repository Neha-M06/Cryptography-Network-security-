def extended_euclidean(a, b):
    """
    Implements the Extended Euclidean Algorithm to find gcd(a, b)
    and coefficients x, y such that ax + by = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0  # Base case: gcd is 'a', x = 1, y = 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)  # Recursive call
        # Update x and y based on the results of the recursion
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


# Example usage:
a = 30
b = 50
gcd, x, y = extended_euclidean(a, b)
print(f"GCD: {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
print(f"Verification: {a}*{x} + {b}*{y} = {gcd}")
