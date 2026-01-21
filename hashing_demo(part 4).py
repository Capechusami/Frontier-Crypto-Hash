# ====================================================
# PART (iv): Hash of Modified String
# ====================================================

import hashlib

# Strings
original_string = "mydata123"
modified_string = "mydata124"

# Calculate hashes
hash_original = hashlib.sha256(original_string.encode('utf-8')).hexdigest()
hash_modified = hashlib.sha256(modified_string.encode('utf-8')).hexdigest()

print("PART (iv): SHA-256 Hash of Modified String")
print("=" * 70)
print(f"Original String: '{original_string}'")
print(f"Original Hash:   {hash_original}")
print()
print(f"Modified String: '{modified_string}'")
print(f"Modified Hash:   {hash_modified}")
print("=" * 70)
print(f"Hash Length Comparison: Both are {len(hash_original)} characters")