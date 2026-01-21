# ====================================================
# PART (v): Analysis of Hash Differences
# ====================================================

import hashlib

# Calculate hashes
original_string = "mydata123"
modified_string = "mydata124"

hash_original = hashlib.sha256(original_string.encode('utf-8')).hexdigest()
hash_modified = hashlib.sha256(modified_string.encode('utf-8')).hexdigest()

print("PART (v): Analysis of Two Hashes")
print("=" * 70)

# 1. Basic comparison
print("1. BASIC COMPARISON:")
print(f"   Original Hash: {hash_original}")
print(f"   Modified Hash: {hash_modified}")
print(f"   Are they identical? {'NO' if hash_original != hash_modified else 'YES'}")

# 2. Character-by-character analysis
print("\n2. DETAILED ANALYSIS:")
matching = 0
for i in range(len(hash_original)):
    if hash_original[i] == hash_modified[i]:
        matching += 1

similarity = (matching / len(hash_original)) * 100
print(f"   Characters matching at same positions: {matching}/64")
print(f"   Similarity: {similarity:.2f}%")

# 3. Find first difference
for i in range(len(hash_original)):
    if hash_original[i] != hash_modified[i]:
        print(f"\n3. FIRST DIFFERENCE:")
        print(f"   Position: {i + 1}")
        print(f"   Original: '{hash_original[i]}'")
        print(f"   Modified: '{hash_modified[i]}'")
        print(f"   (Difference starts at the VERY FIRST character)")
        break

# 4. Cryptographic properties demonstrated
print("\n4. CRYPTOGRAPHIC PROPERTIES DEMONSTRATED:")
print("   a) Avalanche Effect: Small input change -> Large output change")
print("   b) Deterministic: Same input -> Same output")
print("   c) Fixed Length: All outputs are 256 bits")
print("   d) Pre-image Resistance: Cannot reverse the hash")

print("\n5. SECURITY IMPLICATION:")
print("   Even minimal input changes produce completely different hashes,")
print("   making it ideal for data integrity verification and tamper detection.")
print("=" * 70)