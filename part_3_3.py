# ===========================================================
# PART (iii): Decrypt Ciphertext Using Private Key
# ===========================================================

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("PART (iii): Ciphertext Decryption with Private Key")
print("=" * 60)

# Generate keys
key = RSA.generate(2048)
public_key = key.publickey()

# Original message
original_message = "Confidential"

# Encrypt the message
cipher = PKCS1_OAEP.new(public_key)
message_bytes = original_message.encode('utf-8')
ciphertext = cipher.encrypt(message_bytes)

print("BEFORE DECRYPTION:")
print(f"Ciphertext (hex): {ciphertext.hex()[:50]}...")

# Create cipher object for decryption (using private key)
decrypt_cipher = PKCS1_OAEP.new(key)

# Decrypt the ciphertext
try:
    decrypted_bytes = decrypt_cipher.decrypt(ciphertext)
    decrypted_message = decrypted_bytes.decode('utf-8')
    
    print("\nDECRYPTION PROCESS:")
    print("-" * 40)
    print("1. Ciphertext received: OK")
    print("2. Decrypted using private key: OK")
    print("3. Padding removed (OAEP): OK")
    print("4. Converted back to string: OK")
    
    print(f"\nDecrypted bytes: {decrypted_bytes}")
    print(f"Decrypted message: '{decrypted_message}'")
    
except ValueError as e:
    print(f"\nDecryption failed: {e}")
except Exception as e:
    print(f"\nError: {e}")

print("=" * 60)