from Crypto.Util.number import inverse 
#modular multiplicative inverse

def common_modulus_attack(ciphertext1, ciphertext2, exponent1, exponent2, modulus):
    gcd, s, t = extended_gcd(exponent1, exponent2)
    
    if s < 0:
        s = -s
        ciphertext1 = inverse(ciphertext1, modulus)
    elif t < 0:
        t = -t
        ciphertext2 = inverse(ciphertext2, modulus)

    plaintext1 = pow(ciphertext1, s, modulus)
    plaintext2 = pow(ciphertext2, t, modulus)

    plaintext = (plaintext1 * plaintext2) % modulus
    return plaintext

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Example usage:
ciphertext1 = 123456789
ciphertext2 = 987654321
exponent1 = 17
exponent2 = 13
modulus = 253481
plaintext = common_modulus_attack(ciphertext1, ciphertext2, exponent1, exponent2, modulus)
print("Decrypted plaintext:", plaintext)