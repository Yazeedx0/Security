# **README - Security Project Test Suite**

## **Overview**
This project implements various security mechanisms such as **symmetric encryption**, **message authentication**, and **hybrid encryption** in Python. The provided test suite allows users to test and compare different cryptographic techniques using the **DES algorithm** (in different modes), **Message Authentication Codes (MACs)**, and **Hybrid Encryption** (using RSA for key exchange).

## **Project Structure**
The project consists of the following main components:

1. **Symmetric Encryption (DES)** - Supports encryption in the following modes:
   - ECB (Electronic Codebook)
   - CBC (Cipher Block Chaining)
   - CFB (Cipher Feedback)
   - OFB (Output Feedback)
   
2. **Message Authentication** - Ensures the integrity and authenticity of messages using a MAC.
   
3. **Hybrid Encryption** - Combines RSA public-key encryption for key exchange and DES for encrypting the actual message.

4. **Test Suite** - A Python script (`test_all.py`) to test the different cryptographic methods, verify correct implementation, and display the results.

## **Installation**

### **1. Clone or Download the Project**
You can either clone or download the project files from the repository.

### **2. Set up Python Virtual Environment**

Create a virtual environment using the following command:

```bash
python -m venv myenv
3. Activate the Virtual Environment
Once the virtual environment is created, activate it using the following commands:
```
Windows:
```plaintext
myenv\Scripts\activate
```
4. Install Dependencies
Install the necessary dependencies using pip. You can install the required libraries by running the following command in the terminal:

```plaintext
pip install pycryptodome
This library provides the cryptographic functions needed for the encryption and decryption processes.
```
How to Use the Test Suite
Once the environment is set up and dependencies are installed, you can run the test suite by executing the test_all.py script.

```plaintext
python test_all.py
```
The test suite will guide you through different cryptographic operations. The available options include:
```
How to Use the Test Suite
Symmetric Encryption (DES)

When prompted, select 1 for "Data Confidentiality Assurance by Symmetric Encryption".
Provide an 8-byte key (e.g., YAZEEDKA).
Select a mode (ECB, CBC, CFB, or OFB).
You can choose to Encrypt or Decrypt a message.
The system will display the ciphertext for encryption and the plaintext for decryption.
Message Authentication

Select 2 for "Message Authentication Assurance".
Enter a shared key and a message to generate a MAC.
The program will display the message with the MAC.
You can choose to verify the authenticity of the message by entering the message and its MAC.
Hybrid Encryption

Select 3 for "Data Confidentiality Assurance by Hybrid Encryption".
Enter a plaintext message to encrypt using RSA for key exchange and DES for encryption.
The ciphertext will be displayed, and you can also decrypt it to verify the result.
Exit

To exit the program, select 4.
Expected Output
When running the tests, you will receive outputs like:

Encrypted ciphertext in different modes (ECB, CBC, etc.)
Decrypted plaintext after successful decryption
MAC values for message authentication
Hybrid encryption results with RSA and DES
For example, an encryption in CBC mode might output:

```plaintext
Ciphertext (CBC mode): f554107b78a47132cfe4ffcb9c2e86df417cd50362a66c4c
If decryption is performed successfully, the original plaintext will be displayed:
```
```plaintext
Decrypted plaintext (CBC mode): YAZEEDKAMEL
```
Symmetric Encryption (DES):
We use the DES algorithm from the pycryptodome library for encryption.
The plaintext is padded and encrypted in different modes (ECB, CBC, CFB, OFB).
Decryption is done by reversing the encryption process, using the same key and mode.
Message Authentication:
We generate a MAC using a shared secret key to ensure data integrity.
Verification ensures that the message has not been tampered with by checking the MAC.
Hybrid Encryption:
RSA is used for key exchange to securely exchange the encryption key.
The message is encrypted using DES (symmetric encryption) after the secure key exchange.
Conclusion
This test suite allows users to explore key concepts in symmetric encryption, message authentication, and hybrid encryption. It provides hands-on experience with modern cryptographic techniques using Python.
