text = 'Hello Zaira!'
text2 = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
    
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message
    
def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)
    
print(f'Encrypted text: {text2}')
print(f'Key: {custom_key}')
# encryption = encrypt(text, custom_key)
# print(encryption)
# decryption = decrypt(encryption, custom_key)
# print(decryption)
