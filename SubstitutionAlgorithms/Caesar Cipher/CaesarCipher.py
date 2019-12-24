##Caesar Cipher


import string


def alphabettonum(data):
    number_equivalent = []
    for element in data:
        number_equivalent.append(characters.index(element))
        #print(characters.index(element))
    return number_equivalent

def numtoalphabets(data):
    text_equivalent = ""
    for number in data:
        text_equivalent = text_equivalent + str((characters[number]))
        #print(str((characters[number])))
    return text_equivalent
    


characters = list(string.ascii_lowercase)

plain_text = input("Enter The Message (lowercase)")
plain_text_number_equivalent = alphabettonum(plain_text)


key = input("Enter the Key (lowercase and single letter)")
key_number_equivalent = (ord(key)-97)   #sotheord(key)actuallygivesandasciivalueinordertobringitto26rangesubtracted97





cipher_text_number_equivalent = []

for i in range(0,len(plain_text)):
        cipher_text_number_equivalent.append(((plain_text_number_equivalent[i]+key_number_equivalent)%26))
        #print(cipher_text_number_equivalent)


cipher_text =  numtoalphabets(cipher_text_number_equivalent)


print("Plain-Text" + ": {}".format(plain_text))
print("Encrypted-Text" + ": {}".format(cipher_text))

        

print

