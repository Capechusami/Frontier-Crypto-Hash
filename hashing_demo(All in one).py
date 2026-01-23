

import hashlib
import time

def main():
    print("=" * 80)
    print("QUESTION 2: SHA-256 HASHING DEMONSTRATION")
    print("=" * 80)
    
    # ========================================================================
    # PART (i): Hash the string "mydata123" using SHA-256 
    # ========================================================================
    print("\n" + "=" * 60)
    print("PART (i): SHA-256 HASH OF 'mydata123'")
    print("=" * 60)
    
    original_string = "mydata123"
    hash_original = hashlib.sha256(original_string.encode()).hexdigest()
    
    print(f"Input String: '{original_string}'")
    print(f"SHA-256 Hash: {hash_original}")
    print(f"Hash Length: {len(hash_original)} characters")
    print(f"Bit Length: {len(hash_original) * 4} bits")
    
    # ========================================================================
    # PART (ii): Print original string and its SHA-256 hash 
    # ========================================================================
    print("\n" + "=" * 60)
    print("PART (ii): ORIGINAL STRING AND ITS HASH")
    print("=" * 60)
    
    print(f"Original String (Plaintext): '{original_string}'")
    print(f"SHA-256 Hash (Hex):          {hash_original}")
    print("\nComparison:")
    print(f"  String length: {len(original_string)} characters")
    print(f"  Hash length:   {len(hash_original)} hex characters")
    
    # ========================================================================
    # PART (iii): Change one character 
    # ========================================================================
    print("\n" + "=" * 60)
    print("PART (iii): MODIFYING ONE CHARACTER")
    print("=" * 60)
    
    modified_string = "mydata124"  # Changed '3' to '4'
    print(f"Original String: '{original_string}'")
    print(f"Modified String: '{modified_string}'")
    print("\nModification Details:")
    print("  Position changed: 9 (last character)")
    print(f"  Character change: '{original_string[8]}' → '{modified_string[8]}'")
    print(f"  Input change: 1 out of {len(original_string)} characters ({1/len(original_string)*100:.1f}%)")
    
    # ========================================================================
    # PART (iv): Hash of modified string 
    # ========================================================================
    print("\n" + "=" * 60)
    print("PART (iv): HASH OF MODIFIED STRING")
    print("=" * 60)
    
    hash_modified = hashlib.sha256(modified_string.encode()).hexdigest()
    
    print(f"Modified String: '{modified_string}'")
    print(f"SHA-256 Hash:    {hash_modified}")
    print(f"Hash Length:     {len(hash_modified)} characters")
    
    # ========================================================================
    # PART (v): Observations on the two hashes 
    # ========================================================================
    print("\n" + "=" * 60)
    print("PART (v): ANALYSIS AND OBSERVATIONS")
    print("=" * 60)
    
    # Calculate hash similarity
    matches = sum(1 for a, b in zip(hash_original, hash_modified) if a == b)
    similarity = (matches / len(hash_original)) * 100
    
    print("1. HASH COMPARISON:")
    print(f"   Original Hash: {hash_original}")
    print(f"   Modified Hash: {hash_modified}")
    print(f"   Are they identical? {'NO' if hash_original != hash_modified else 'YES'}")
    
    print("\n2. SIMILARITY ANALYSIS:")
    print(f"   Matching characters at same positions: {matches}/64")
    print(f"   Similarity percentage: {similarity:.2f}%")
    
    # Find first difference
    for i in range(len(hash_original)):
        if hash_original[i] != hash_modified[i]:
            print(f"\n3. FIRST DIFFERENCE:")
            print(f"   Position: {i + 1}")
            print(f"   Original: '{hash_original[i]}'")
            print(f"   Modified: '{hash_modified[i]}'")
            break
    
    print("\n4. CRYPTOGRAPHIC PROPERTIES DEMONSTRATED:")
    properties = [
        ("Avalanche Effect", "Small input change → Large output change"),
        ("Deterministic", "Same input → Same output always"),
        ("Fixed Length", "All outputs are 256 bits"),
        ("Pre-image Resistance", "Cannot derive input from hash"),
        ("Collision Resistance", "Hard to find two inputs with same hash"),
        ("One-way Function", "Easy to compute hash, hard to reverse")
    ]
    
    for i, (prop, desc) in enumerate(properties, 1):
        print(f"   {i}. {prop}: {desc}")
    
    print("\n5. SECURITY IMPLICATIONS:")
    print("   • Data Integrity: Any tampering changes the hash")
    print("   • Password Storage: Store hashes, not plain passwords")
    print("   • Digital Signatures: Verify document authenticity")
    print("   • File Verification: Detect corrupted or modified files")
    
    print("\n" + "=" * 80)
    print("QUESTION 2 COMPLETE - ALL PARTS DEMONSTRATED")
    print("=" * 80)
    
    # Optional: Save results to file
    with open("hashing_results.txt", "w") as f:
        f.write("HASHING RESULTS\n")
        f.write("=" * 50 + "\n")
        f.write(f"Original String: {original_string}\n")
        f.write(f"Original Hash:   {hash_original}\n")
        f.write(f"Modified String: {modified_string}\n")
        f.write(f"Modified Hash:   {hash_modified}\n")
        f.write(f"Similarity:      {similarity:.2f}%\n")
    
    print("\n✓ Results saved to 'hashing_results.txt'")

if __name__ == "__main__":
    main()
