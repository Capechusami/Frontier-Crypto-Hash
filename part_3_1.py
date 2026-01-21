# ===========================================================
# PART (i): Generate RSA Key Pair (Public and Private Keys)
# ===========================================================

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

print("PART (i): RSA Key Generation")
print("=" * 60)

# Generate RSA key pair (2048-bit for security)
key = RSA.generate(2048)

# Extract public key
public_key = key.publickey()

# Display key information
print("RSA Key Pair Generated Successfully")
print("\nKEY DETAILS:")
print("-" * 40)
print(f"Key Size: {key.size_in_bits()} bits")
print(f"Modulus (n): {key.n}")
print(f"Public Exponent (e): {key.e}")
print(f"Private Exponent (d): {key.d}")
print(f"Prime 1 (p): {key.p}")
print(f"Prime 2 (q): {key.q}")

print("\nPUBLIC KEY (for encryption):")
print(f"n (modulus): {public_key.n}")
print(f"e (exponent): {public_key.e}")

print("\nPRIVATE KEY (for decryption):")
print(f"d (private exponent): {key.d}")

print("\nNote: In practice, keys are stored securely, not printed in full.")
print("=" * 60)

# ===========================================================
# PART (ii): Encrypt and Decrypt a Message with RSA
# ===========================================================

from Crypto.Cipher import PKCS1_OAEP

message = b"Confidential"

# Encrypt with public key
encrypt_cipher = PKCS1_OAEP.new(public_key)
ciphertext = encrypt_cipher.encrypt(message)

# Decrypt with private key
decrypt_cipher = PKCS1_OAEP.new(key)
decrypted = decrypt_cipher.decrypt(ciphertext)

print("PART (ii): RSA Encryption/Decryption Demo")
print("=" * 60)
print(f"Original Message:  {message.decode('utf-8')}")
print(f"Ciphertext (bytes): {ciphertext}")
print(f"Decrypted Message: {decrypted.decode('utf-8')}")

is_recovered = decrypted == message
print(f"Recovered matches original? {'YES' if is_recovered else 'NO'}")
print("=" * 60)

# Save keys for later use (optional)
with open('private_key.pem', 'wb') as f:
    f.write(key.export_key())
with open('public_key.pem', 'wb') as f:
    f.write(public_key.export_key())