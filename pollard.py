import gmpy2

def pollard_rho_factorization(n):
    def f(x):
        return (x * x + 1) % n

    x = 2
    y = 2
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gmpy2.gcd(abs(x - y), n)
    if d == n:
        return None  # Factor not found
    return d

# Example usage:
modulus_n = 2027 * 2089  # Example RSA modulus (product of two primes)
factor = pollard_rho_factorization(modulus_n)
print("Factor found:", factor)
