from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_rsa_keypair():
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

def hybrid_encrypt(plaintext, public_key):
    aes_key = get_random_bytes(16)  # AES-128
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher_aes.iv
    ciphertext = iv + cipher_aes.encrypt(pad(plaintext.encode(), AES.block_size))

    rsa_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    encrypted_key = cipher_rsa.encrypt(aes_key)

    return ciphertext + encrypted_key

def hybrid_decrypt(ciphertext, private_key):
    aes_ciphertext = ciphertext[:-256]  # Assuming RSA key size is 2048 bits
    encrypted_key = ciphertext[-256:]
    
    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    aes_key = cipher_rsa.decrypt(encrypted_key)

    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv=aes_ciphertext[:AES.block_size])
    plaintext = unpad(cipher_aes.decrypt(aes_ciphertext[AES.block_size:]), AES.block_size).decode()
    
    return plaintext
