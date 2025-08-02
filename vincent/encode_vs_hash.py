import hashlib

sentence = 'Hello Vincent from Hell!'

# ENCODING
# from one data format to another (binary,utf-8,hex)
# it is reversible

# change from string to binary
binary_format = ''
for char in sentence:
    binary_data = f'{ord(char):08b}'
    binary_format = binary_format + binary_data
print(binary_format)

# HASHING
# convert the data into fix length string
# use hashing algoritm
# irreversible

sentence_utf8 = sentence.encode('utf-8')
hashing = hashlib.sha256(sentence_utf8).hexdigest()
print(hashing)

# ENCRYPTION
# convert the data into non sense
# only reversible with the key
