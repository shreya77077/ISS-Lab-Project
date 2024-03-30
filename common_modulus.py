from Crypto.Util.number import long_to_bytes
import gmpy2

def common_modulus_attack(ciphertext_alice, ciphertext_bob, e_alice, e_bob, n):
    gcd, s, t = gmpy2.gcdext(e_alice, e_bob)
    if gcd != 1:
        return None  # Keys not found

    x = pow(ciphertext_alice, s, n)
    y = pow(ciphertext_bob, t, n)

    plaintext = (x * y) % n
    return long_to_bytes(plaintext)

# Example usage:
ciphertext_alice = 1234567890  # Intercepted ciphertext encrypted with Alice's public key
ciphertext_bob = 9876543210  # Intercepted ciphertext encrypted with Bob's public key
e_alice = 65537  # Alice's public exponent
e_bob = 65539  # Bob's public exponent
n = 1234567890123456789012345678901234567890  # Common modulus

plaintext = common_modulus_attack(ciphertext_alice, ciphertext_bob, e_alice, e_bob, n)
print("Decrypted plaintext:", plaintext)
