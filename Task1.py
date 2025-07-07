import string

letters =  " " + string.ascii_lowercase 
letters = list(letters)

print("*** Caesar Cipher Encryption & Decryption ***")

num = int(input("Enter shift value (integer): "))

list1 = (letters[num:])
list2 = (letters[:num]) 

encrypt = list1 + list2 


while(True):
    choice = input("(*Press Q to quite*)\nDo you want to Encrypt or Decrypt (E/D): ").lower()
    if(choice == 'q'):
        break

    if(choice == 'e'):
        #Encrypt
        message = input("Enter Your Encrypt message: ").lower()
        n = ""

        for i in message:
            index = letters.index(i)
            n += encrypt[index]
        print(f"Encrypted message: {n}")
        continue


    if(choice == 'd'):
        #Decrypt
        n = input("Enter Your Decrypt message: ").lower()
        message = ""

        for i in n:
            index = encrypt.index(i)
            message += letters[index]
        print(f"Decrypted message: {message}")
        continue