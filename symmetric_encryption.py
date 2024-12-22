from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def des_encrypt_ecb(plaintext, key):
    """Encrypts plaintext using DES in ECB mode."""
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), DES.block_size))

def des_encrypt_cbc(plaintext, key):
    """Encrypts plaintext using DES in CBC mode."""
    iv = os.urandom(DES.block_size)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(plaintext.encode(), DES.block_size))

def des_encrypt_cfb(plaintext, key):
    """Encrypts plaintext using DES in CFB mode."""
    iv = os.urandom(DES.block_size)
    cipher = DES.new(key, DES.MODE_CFB, iv)
    return iv + cipher.encrypt(pad(plaintext.encode(), DES.block_size))

def des_encrypt_ofb(plaintext, key):
    """Encrypts plaintext using DES in OFB mode."""
    iv = os.urandom(DES.block_size)
    cipher = DES.new(key, DES.MODE_OFB, iv)
    return iv + cipher.encrypt(pad(plaintext.encode(), DES.block_size))

def des_decrypt(ciphertext, key, mode):
    """Decrypts ciphertext using DES in the specified mode (ECB, CBC, CFB, OFB)."""
    try:
        if mode == 'ECB':
            cipher = DES.new(key, DES.MODE_ECB)
            return unpad(cipher.decrypt(ciphertext), DES.block_size).decode()
        elif mode == 'CBC':
            iv = ciphertext[:DES.block_size]
            cipher = DES.new(key, DES.MODE_CBC, iv)
            return unpad(cipher.decrypt(ciphertext[DES.block_size:]), DES.block_size).decode()
        elif mode == 'CFB':
            iv = ciphertext[:DES.block_size]
            cipher = DES.new(key, DES.MODE_CFB, iv)
            return unpad(cipher.decrypt(ciphertext[DES.block_size:]), DES.block_size).decode()
        elif mode == 'OFB':
            iv = ciphertext[:DES.block_size]
            cipher = DES.new(key, DES.MODE_OFB, iv)
            return unpad(cipher.decrypt(ciphertext[DES.block_size:]), DES.block_size).decode()
        else:
            raise ValueError("Invalid mode. Supported modes are 'ECB', 'CBC', 'CFB', and 'OFB'.")
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None