from symmetric_encryption import des_encrypt_ecb, des_encrypt_cbc, des_encrypt_cfb, des_encrypt_ofb, des_decrypt
from message_authentication import create_message_with_mac, verify_message
from hybrid_encryption import hybrid_encrypt, hybrid_decrypt, generate_rsa_keypair

def main():
    while True:
        print("\nSelect a security mechanism:")
        print("1. Data Confidentiality Assurance by Symmetric Encryption")
        print("2. Message Authentication Assurance")
        print("3. Data Confidentiality Assurance by Hybrid Encryption")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Data Confidentiality Assurance by Symmetric Encryption (DES)
        if choice == '1':
            key = input("Enter an 8-byte key (must be 8 characters): ")
            if len(key) != 8:
                print("Error: Key must be exactly 8 characters long.")
                continue
            key = key.encode()

            # ECB mode is the default
            mode = 'ECB'
            print("\nECB (Electronic Code Book) mode is selected by default.")
            
            # Ask user to select an additional chaining mode (CBC, CFB, or OFB)
            print("\nSelect a chaining mode for comparison:")
            print("1. CBC (Cipher Block Chaining)")
            print("2. CFB (Cipher Feedback)")
            print("3. OFB (Output Feedback)")
            mode_choice = input("Enter your choice (1-3): ").strip()

            if mode_choice == '1':
                additional_mode = 'CBC'
            elif mode_choice == '2':
                additional_mode = 'CFB'
            elif mode_choice == '3':
                additional_mode = 'OFB'
            else:
                print("Invalid mode choice. Defaulting to CBC.")
                additional_mode = 'CBC'

            action = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

            if action == 'E':
                plaintext = input("Enter plaintext: ")
                # Default to ECB for the first encryption
                ciphertext = des_encrypt_ecb(plaintext, key)
                print(f"Ciphertext (ECB mode): {ciphertext.hex()}")

                # Encrypt with the additional selected mode
                if additional_mode == 'CBC':
                    ciphertext_cbc = des_encrypt_cbc(plaintext, key)
                    print(f"Ciphertext (CBC mode): {ciphertext_cbc.hex()}")
                elif additional_mode == 'CFB':
                    ciphertext_cfb = des_encrypt_cfb(plaintext, key)
                    print(f"Ciphertext (CFB mode): {ciphertext_cfb.hex()}")
                elif additional_mode == 'OFB':
                    ciphertext_ofb = des_encrypt_ofb(plaintext, key)
                    print(f"Ciphertext (OFB mode): {ciphertext_ofb.hex()}")

            elif action == 'D':
                ciphertext_hex = input("Enter ciphertext (hex): ")
                try:
                    ciphertext = bytes.fromhex(ciphertext_hex)
                    decrypted_plaintext = des_decrypt(ciphertext, key, mode)
                    if decrypted_plaintext:
                        print(f"Decrypted plaintext (ECB mode): {decrypted_plaintext}")

                    # Decrypt with the additional selected mode
                    if additional_mode == 'CBC':
                        ciphertext_cbc = bytes.fromhex(input("Enter CBC ciphertext (hex): "))
                        decrypted_cbc = des_decrypt(ciphertext_cbc, key, 'CBC')
                        print(f"Decrypted plaintext (CBC mode): {decrypted_cbc}")
                    elif additional_mode == 'CFB':
                        ciphertext_cfb = bytes.fromhex(input("Enter CFB ciphertext (hex): "))
                        decrypted_cfb = des_decrypt(ciphertext_cfb, key, 'CFB')
                        print(f"Decrypted plaintext (CFB mode): {decrypted_cfb}")
                    elif additional_mode == 'OFB':
                        ciphertext_ofb = bytes.fromhex(input("Enter OFB ciphertext (hex): "))
                        decrypted_ofb = des_decrypt(ciphertext_ofb, key, 'OFB')
                        print(f"Decrypted plaintext (OFB mode): {decrypted_ofb}")
                except Exception as e:
                    print(f"Error during decryption: {e}")

        # Message Authentication Assurance
        elif choice == '2':
            key = input("Enter a shared symmetric key: ").encode()
            message = input("Enter the message: ")
            message_with_mac = create_message_with_mac(message, key)
            print(f"Message with MAC: {message_with_mac}")

            verify = input("Do you want to verify a message? (y/n): ").strip().lower()
            if verify == 'y':
                message_to_verify = input("Enter the message with MAC: ")
                if verify_message(message_to_verify, key):
                    print("Message is authentic.")
                else:
                    print("Message verification failed.")

        # Data Confidentiality Assurance by Hybrid Encryption
        elif choice == '3':
            private_key, public_key = generate_rsa_keypair()
            plaintext = input("Enter plaintext to encrypt: ")
            ciphertext = hybrid_encrypt(plaintext, public_key)
            print(f"Ciphertext: {ciphertext.hex()}")

            decrypted_plaintext = hybrid_decrypt(ciphertext, private_key)
            print(f"Decrypted Plaintext: {decrypted_plaintext}")

        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
