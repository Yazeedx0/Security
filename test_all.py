import os
from symmetric_encryption import des_encrypt_ecb, des_encrypt_cbc, des_encrypt_cfb, des_encrypt_ofb, des_decrypt
from message_authentication import create_message_with_mac, verify_message
from hybrid_encryption import hybrid_encrypt, hybrid_decrypt, generate_rsa_keypair

def test_symmetric_encryption():
    print("\nTesting Symmetric Encryption:")
    key = b'12345678'  # 8-byte key
    plaintext = "hello"

    # ECB mode
    ciphertext_ecb = des_encrypt_ecb(plaintext, key)
    decrypted_ecb = des_decrypt(ciphertext_ecb, key, 'ECB')
    print(f"ECB Mode -> Ciphertext: {ciphertext_ecb.hex()}, Decrypted: {decrypted_ecb}")

    # CBC mode
    ciphertext_cbc = des_encrypt_cbc(plaintext, key)
    decrypted_cbc = des_decrypt(ciphertext_cbc, key, 'CBC')
    print(f"CBC Mode -> Ciphertext: {ciphertext_cbc.hex()}, Decrypted: {decrypted_cbc}")

    # CFB mode
    ciphertext_cfb = des_encrypt_cfb(plaintext, key)
    decrypted_cfb = des_decrypt(ciphertext_cfb, key, 'CFB')
    print(f"CFB Mode -> Ciphertext: {ciphertext_cfb.hex()}, Decrypted: {decrypted_cfb}")

    # OFB mode
    ciphertext_ofb = des_encrypt_ofb(plaintext, key)
    decrypted_ofb = des_decrypt(ciphertext_ofb, key, 'OFB')
    print(f"OFB Mode -> Ciphertext: {ciphertext_ofb.hex()}, Decrypted: {decrypted_ofb}")

def test_message_authentication():
    print("\nTesting Message Authentication:")
    key = b'sharedkey'
    message = "hello"

    # Generate MAC
    message_with_mac = create_message_with_mac(message, key)
    print(f"Message with MAC: {message_with_mac}")

    # Verify MAC
    is_authentic = verify_message(message_with_mac, key)
    print(f"Message Verification: {'Authentic' if is_authentic else 'Failed'}")

def test_hybrid_encryption():
    print("\nTesting Hybrid Encryption:")
    plaintext = "hello"

    # Generate RSA keys
    private_key, public_key = generate_rsa_keypair()

    # Encrypt
    ciphertext = hybrid_encrypt(plaintext, public_key)
    print(f"Ciphertext: {ciphertext.hex()}")

    # Decrypt
    decrypted_plaintext = hybrid_decrypt(ciphertext, private_key)
    print(f"Decrypted Plaintext: {decrypted_plaintext}")

def run_tests():
    print("Starting Tests...")
    test_symmetric_encryption()
    test_message_authentication()
    test_hybrid_encryption()
    print("\nAll Tests Completed.")

if __name__ == "__main__":
    run_tests()
