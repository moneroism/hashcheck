import hashlib
import sys

def hash(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

downloadedhash = hash(sys.argv[1])

filehash = input("Enter the hash to compare with: ")

if filehash == downloadedhash:
    print("""
=======================================================================================
    ✓ | Hash matches
    Entered hash is | """, filehash, """
    File hash is | """, downloadedhash, """
=======================================================================================
    """)
else:
    print("""
=======================================================================================
    X | Hash doesnt match
    Entered hash is | """, filehash, """
    File hash is | """, downloadedhash, """
    Contents may have been tampered with or changed.
=======================================================================================
    """)
