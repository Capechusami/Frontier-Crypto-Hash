# ===========================================================
# PART (iv): Display All Stages
# ===========================================================

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("PART (iv): Complete RSA Encryption/Decryption Process")
print("=" * 70)

# Generate keys
key = RSA.generate(2048)
public_key = key.publickey()

# Original message
original_message = "Confidential"

# Encryption
encrypt_cipher = PKCS1_OAEP.new(public_key)
message_bytes = original_message.encode('utf-8')
ciphertext = encrypt_cipher.encrypt(message_bytes)

# Decryption
decrypt_cipher = PKCS1_OAEP.new(key)
decrypted_bytes = decrypt_cipher.decrypt(ciphertext)
decrypted_message = decrypted_bytes.decode('utf-8')

print("STAGE 1: ORIGINAL MESSAGE")
print("-" * 40)
print(f"Message: '{original_message}'")
print(f"Length: {len(original_message)} characters")
print(f"Bytes: {message_bytes}")

print("\nSTAGE 2: ENCRYPTED CIPHERTEXT")
print("-" * 40)
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Ciphertext length: {len(ciphertext)} bytes")
print("Note: Ciphertext is in byte format for transmission/storage")

print("\nSTAGE 3: DECRYPTED MESSAGE")
print("-" * 40)
print(f"Decrypted bytes: {decrypted_bytes}")
print(f"Decrypted message: '{decrypted_message}'")

print("\nSUMMARY:")
print("-" * 40)
print("Original -> Encryption -> Ciphertext -> Decryption -> Decrypted")
print(f"'{original_message}' -> RSA -> {ciphertext[:20]}... -> RSA -> '{decrypted_message}'")

print("\n" + "=" * 70)