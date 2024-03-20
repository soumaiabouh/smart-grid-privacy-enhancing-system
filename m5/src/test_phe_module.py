from phe import paillier
# need to pip-install phe

public_key, private_key = paillier.generate_paillier_keypair(n_length = 1024)

secret_nums = [1, 44, 55, 100, 12, 332, 1212, 124, 2424, 35, 353, 1, 121]
encrypted_nums = [public_key.encrypt(x) for x in secret_nums]

add_one = []

for num in encrypted_nums:
    num += 1
    add_one.append(num)
    
decrypted = [private_key.decrypt(x) for x in add_one]
print(decrypted)