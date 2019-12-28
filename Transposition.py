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



def encryption(key,plain):
    cipher_number_equivalent = []
    key = np.array(key).reshape(1,-1)
    shapekey=key.shape
    plain = list(plain)
    #print(len(plain)%shapekey[1],len(plain),shapekey[1])
    if((len(plain)%shapekey[1])!=0):
        for i in range(0,shapekey[1]-(len(plain)%shapekey[1])):
            value = 25-i
            plain.append(value)
            #print(plain)
        plain=np.array(plain)
        #print(len(plain)%shapekey[1],len(plain),shapekey[1])
    plain = np.array(plain)
    plain=plain.reshape(-1,shapekey[1])
    for i in range(0,plain.shape[0]):
        print("")
        for j in range(0,plain.shape[1]):
            print(characters[plain[i,j]],end=" ")

    key = key.reshape(-1,).tolist()
    #print(key)
    for element in key:
        #print(element)
        for i in range(0,plain.shape[0]):
            cipher_number_equivalent.append(plain[i,element-1])
    
    print("")
    return cipher_number_equivalent
    



characters = list (string.ascii_lowercase)
plain_text = input("Enter The Plain Text").replace(" ","").lower()

plain_text_number_equivalent =alphabettonum(plain_text)



  
key = list(input("Enter The Key Order(separated by commas)").split(","))

for i in range(0,len(key)):
    key[i] = int(key[i])
print(key)

cipher_text_number_equivalent = encryption(key,plain_text_number_equivalent)

cipher_text = numtoalphabets(cipher_text_number_equivalent)


print("Plain-Text" + ": {}".format(plain_text))
print("Encrypted-Text" + ": {}".format(cipher_text))





