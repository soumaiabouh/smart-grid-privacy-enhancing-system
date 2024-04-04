from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random key and nonce
key = get_random_bytes(16)  # AES key should be 16, 24, or 32 bytes
nonce = get_random_bytes(16)

# Initialize cipher object
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

# Assume meter_reading is your data to encrypt, e.g., b"12345.678 kWh"
meter_reading = b"0.68415"
ciphertext, tag = cipher.encrypt_and_digest(meter_reading)

# To decrypt:
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
print(type(cipher))
plaintext = cipher.decrypt_and_verify(ciphertext, tag)
print(plaintext)  # This should output your original meter reading
