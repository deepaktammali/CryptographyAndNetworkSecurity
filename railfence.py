import string
import numpy as np

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


def encryption(data):
    odd = []
    even = []
    for i in range(0,len(data)):
        if(i%2==0):
            odd.append(data[i])
        else:
            even.append(data[i])
    for element in even:
        odd.append(element)
            
    return odd
            

characters = list (string.ascii_lowercase)
plain_text = input("Enter The Plain Text").replace(" ","").lower()
plain_text_number_equivalent =alphabettonum(plain_text)

cipher_text_number_equivalent = encryption(plain_text_number_equivalent)

cipher_text = numtoalphabets(cipher_text_number_equivalent)

print("Plain-Text" + ": {}".format(plain_text))
print("Encrypted-Text" + ": {}".format(cipher_text))




