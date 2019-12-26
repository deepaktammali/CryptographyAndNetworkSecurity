
import string
import numpy as np
import collections 

characters = list(string.ascii_lowercase)



def texttonumbers(data):
    
    numberequivalent = []
    for element in data:
        numberequivalent.append(characters.index(element))
    return numberequivalent

def redundancyCheck(data):
    for i in range(0,len(data)-1):
        if(data[i]==data[i+1]):
            if(data[i+1]=="x"):
                data = data.replace("{}{}".format(data[i+1],data[i+1]),"{}y".format(data[i+1]))
            else :
                data = data.replace("{}{}".format(data[i+1],data[i+1]),"{}x".format(data[i+1]))
    print(data)
    return data

def matrix(key,plain):
    temp_cipher_matrix  = np.zeros([1,25])
    numberszeroto25 = list(x for x in range(0,26))
    datalength = len(key)
    for i in range(0,datalength):
        temp_cipher_matrix[0,i]=key[i]

    if('9' in key or '8' in key):
        numberszeroto25.remove(9)
        numberszeroto25.remove(8)
    else :
        if('9' in plain):
            numberszeroto25.remove(8)
        else:
            numberszeroto25.remove(9)
        
    for number in key:
        if(number in numberszeroto25):
            numberszeroto25.remove(number)
            print(number,numberszeroto25)
            
    for i in range(datalength,25):
        temp_cipher_matrix[0,i]=numberszeroto25[i-datalength]

    temp_cipher_matrix = temp_cipher_matrix.reshape(5,5)

    for i in range(0,5):
        print('\n')
        for j in range(0,5):
            print(characters[int(temp_cipher_matrix[i,j])],end=" ")
    return temp_cipher_matrix
    
        
    
           

def keyredundancycheck(data):
    data.reverse()
    elemrepcount = collections.Counter(data)
    repetitions = list(elemrepcount.values())
    elements = list(elemrepcount.keys())

    for i in range(0,len(repetitions)):
        if(repetitions[i]>1):
            for j in range(0,repetitions[i]-1):
                data.remove(elements[i])
            
    data.reverse()               
    print(data)
    return data
                
        
    
    
plain_text = (input("Enter Plain Text")).replace(" ","").lower()


if(len(plain_text)%2==1):
    if(plain_text[-1]=="x"):
        plain_text = plain_text + ("y")
    else:
        plain_text = plain_text + ("x")

plain_text_modified = redundancyCheck(plain_text)


key = input("Enter the key:").replace(" ","").lower()

key_number_equivalent = texttonumbers(key)

key_number_equivalent_modified = keyredundancycheck(key_number_equivalent)      #redundanciesremoved


cipher_matrix = matrix(key_number_equivalent_modified,plain_text_modified)









    
    
