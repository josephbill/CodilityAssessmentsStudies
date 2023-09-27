#  a mathematical algorithm that takes an input (or "key") and produces a fixed length string (hash value).
# Maps data to a fixed size values (hashes) : making it easier and more efficient to store and retrieve data 
import hashlib

def hash_function(data):
    # Using SHA-256 hash function
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    return hash_value

# Example usage
data_to_hash = "Hello, world!"
hashed_data = hash_function(data_to_hash)
print("Hashed data:", hashed_data)