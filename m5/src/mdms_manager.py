from Crypto.PublicKey import RSA


class MdmsManager:
    def __init__(self, key_size=2048):
        self.rsa_key_pair = RSA.generate(key_size)
        self.rsa_public_key = self.rsa_key_pair.publickey().export_key()
    
    def get_public_key(self):
        # The public key will be used by the PES to encrypt the aggregates
        return self.rsa_public_key