# PRODIGY_Tast1
# CaesarCipher_Task

This task focuses on building a basic **Caesar Cipher** for text encryption and decryption using letter shifting. It helps understand basic string manipulation and substitution techniques in Python.

## 📌 Objective

Build a Caesar Cipher program in Python to encrypt and decrypt messages by shifting characters. Practice indexing, loops, and user input handling.

## 🛠️ Tools

- Python 3.x


## 📦 Deliverables

- caesar_cipher.py: A complete Python script
- Encrypt function with character shifting logic
- Decrypt function that reverses the shift
- Clean handling of lowercase characters and spaces
- User-defined shift value
- Looping input for continuous encryption/decryption
- Quit option using "Q"

## 📘 Guide

1. User runs the caesar_cipher.py file in any Python IDE or terminal.
2. Program asks for a **shift value** (e.g., 3).
3. User selects whether to encrypt (E) or decrypt (D) a message.
4. Program handles lowercase letters and spaces.
5. User can continue or quit the program using Q.

## 📂 File Description

The project includes:

- **Main Script:**
  - caesar_cipher.py

- **Functions & Flow:**
  - Get shift value and build substitution list
  - Prompt for user choice (E, D, or Q)
  - Encrypt: replace each character using the shifted list
  - Decrypt: reverse lookup from the shifted list
  - Loop until the user exits

- **Sample Logic:**
  - letters = " abcdefghijklmnopqrstuvwxyz"
  - encrypt = letters[num:] + letters[:num]
  - Loop through input message and shift characters using index lookup

## ⚠️ Notes

- Only supports **lowercase letters** and **spaces**
- Input is automatically converted to lowercase
- Does not support special characters or punctuation


## ✅ Outcome

🔐 A working Caesar Cipher that performs both encryption and decryption based on a user-defined shift value.                                                                                                                                                              
