# ====================================================
# PART (i): SHA-256 Hashing of "mydata123"
# ====================================================

import hashlib

# Original string
data = "mydata123"

# Convert string to bytes (required by hashlib)
data_bytes = data.encode('utf-8')

# Create SHA-256 hash object
hash_object = hashlib.sha256(data_bytes)

# Get hexadecimal hash
hash_hex = hash_object.hexdigest()

# Display result
print("PART (i): SHA-256 Hash of 'mydata123'")
print("-" * 40)
print(f"Input: '{data}'")
print(f"SHA-256 Hash: {hash_hex}")
print(f"Hash Length: {len(hash_hex)} characters")
print("-" * 40)