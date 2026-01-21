# ====================================================
# PART (ii): Print Original String and Its Hash
# ====================================================

import hashlib

# Original string
original_string = "mydata123"

# Calculate SHA-256 hash
hash_original = hashlib.sha256(original_string.encode('utf-8')).hexdigest()

# Print both original string and hash
print("PART (ii): Original String and Its SHA-256 Hash")
print("=" * 60)
print(f"ORIGINAL STRING: '{original_string}'")
print(f"SHA-256 HASH:    {hash_original}")
print("=" * 60)