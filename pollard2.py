from math import gcd

def pollard_rho(n):
    def f(x):
        return (x ** 2 + 1) % n

    x = 2
    y = 2
    d = 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d == n:
        return None  # Pollard's rho algorithm failed
    else:
        return d

def factorize(n):
    factors = []
    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        factor = pollard_rho(n)
        if factor is None:
            return None  # Pollard's rho algorithm failed to factorize
        factors.append(factor)
        n //= factor
    return factors

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
number_to_factorize = 1234567890123456789012345678901234567890
factors = factorize(number_to_factorize)
if factors is None:
    print("Pollard's rho algorithm failed to factorize the number.")
else:
    print("Factors:", factors)