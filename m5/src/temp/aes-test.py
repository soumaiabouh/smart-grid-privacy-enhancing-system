import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def test_performance(mode, data, key, nonce):
    start_time = time.time()
    if mode == AES.MODE_GCM:
        cipher = AES.new(key, mode, nonce=nonce)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        # To decrypt
        cipher = AES.new(key, mode, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    elif mode == AES.MODE_CTR:
        cipher = AES.new(key, mode, nonce=nonce)
        ciphertext = cipher.encrypt(data)
        # To decrypt
        cipher = AES.new(key, mode, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
    end_time = time.time()
    return end_time - start_time

# Configuration
key = get_random_bytes(16)  # AES key should be 16 bytes
gcm_nonce = get_random_bytes(12)  # Nonce for GCM 
ctr_nonce = get_random_bytes(12)  # Nonce for CTR
data_size_mb = 10
data = get_random_bytes(data_size_mb * 1024 * 1024 * 30)  # Generate 300MB of data

# Run performance test
gcm_time = test_performance(AES.MODE_GCM, data, key, gcm_nonce)
ctr_time = test_performance(AES.MODE_CTR, data, key, ctr_nonce)

print(f"GCM Encryption/Decryption time: {gcm_time} seconds")
print(f"CTR Encryption/Decryption time: {ctr_time} seconds")
