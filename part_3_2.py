# ===========================================================
# PART (ii): Encrypt Message Using Public Key
# ===========================================================

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("PART (ii): Message Encryption with Public Key")
print("=" * 60)

# Message to encrypt
original_message = "Confidential"

# Load public key (from previous step or generate new)
key = RSA.generate(2048)
public_key = key.publickey()

# Create cipher object for encryption
cipher = PKCS1_OAEP.new(public_key)

# Convert message to bytes and encrypt
message_bytes = original_message.encode('utf-8')
ciphertext = cipher.encrypt(message_bytes)

print(f"Original Message: '{original_message}'")
print(f"Message as bytes: {message_bytes}")
print(f"Message length: {len(message_bytes)} bytes")

print("\nENCRYPTION PROCESS:")
print("-" * 40)
print("1. Message converted to bytes: OK")
print("2. Padding applied (OAEP): OK")
print("3. Encrypted using public key: OK")

print(f"\nCiphertext (hex): {ciphertext.hex()}")
print(f"Ciphertext (bytes): {ciphertext}")
print(f"Ciphertext length: {len(ciphertext)} bytes")

print("\nNote: Ciphertext is randomized - same message produces different ciphertext each time.")
print("=" * 60)