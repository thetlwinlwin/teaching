plaintext = input('Enter your data: ')
key = input('Enter the key: ')

ciphertext = ''

len_of_key = len(key)
len_of_text = len(plaintext)

for i in range(len_of_text):
    denary = ord(plaintext[i])
    key_idx = i % len_of_key
    encrypt = denary + int(key[key_idx])
    ciphertext = ciphertext + chr(encrypt)

print('ciphertext', ciphertext)
