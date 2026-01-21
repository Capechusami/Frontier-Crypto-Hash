# ===========================================================
# PART (v): Verify Message Recovery
# ===========================================================

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("PART (v): Verification of Correct Decryption")
print("=" * 60)

# Generate keys
key = RSA.generate(2048)
public_key = key.publickey()

# Original message
original_message = "Confidential"

# Complete RSA process
encrypt_cipher = PKCS1_OAEP.new(public_key)
ciphertext = encrypt_cipher.encrypt(original_message.encode())

decrypt_cipher = PKCS1_OAEP.new(key)
decrypted_message = decrypt_cipher.decrypt(ciphertext).decode()

print("VERIFICATION PROCESS:")
print("-" * 40)

# Comparison
print(f"Original message:  '{original_message}'")
print(f"Decrypted message: '{decrypted_message}'")

print("\nCOMPARISON CHECK:")
print("-" * 40)

# Check 1: String equality
if original_message == decrypted_message:
    print("OK String content: MATCH")
else:
    print("X String content: DIFFERENT")

# Check 2: Length comparison
if len(original_message) == len(decrypted_message):
    print("OK String length: MATCH")
else:
    print(f"X String length: Original={len(original_message)}, Decrypted={len(decrypted_message)}")

# Check 3: Character-by-character comparison
all_match = True
for i, (orig_char, dec_char) in enumerate(zip(original_message, decrypted_message)):
    if orig_char != dec_char:
        print(f"X Character mismatch at position {i}: '{orig_char}' vs '{dec_char}'")
        all_match = False
        break

if all_match and len(original_message) == len(decrypted_message):
    print("OK All characters match")

print("\nVERIFICATION RESULT:")
print("-" * 40)
if original_message == decrypted_message:
    print("SUCCESS: Original message successfully recovered!")
    print("   The RSA encryption/decryption process worked correctly.")
else:
    print("FAILURE: Decrypted message does not match original!")

print("\nSECURITY CONFIRMATION:")
print("-" * 40)
print("OK Only the private key holder can decrypt the message")
print("OK Public key encryption ensures confidentiality")
print("OK RSA with OAEP padding provides security against attacks")

print("=" * 60)