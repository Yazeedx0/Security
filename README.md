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
```
# 2. Activate the virtual environment
# Windows:
myenv\Scripts\activate

# 3. Install Dependencies
# Install the necessary dependencies using pip
```plaintext
pip install pycryptodome
```
