import string
import numpy as np
import collections 

characters = list(string.ascii_lowercase)




def numberstotext(data):

    textequivalent = ""
    for element in data:
        textequivalent = textequivalent+characters[element]
    return textequivalent




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
        if('j' in plain):
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


def encryptingplaintext(matrix,texttotbeencrypted):
    data = []
    for i in range(0,len(texttotbeencrypted)-1):
        if(i%2==0):
            text1 = texttotbeencrypted[i]
            text2 = texttotbeencrypted[i+1]
            print(text1,text2)
            row1,column1 = np.where(matrix == text1)
            print(np.where(matrix == text1))
            row2,column2 = np.where(matrix == text2)
            print(np.where(matrix == text2))
            row1[row1==4]=0
            row2[row2==4]=0
            column1[column1==4]=0
            column2[column2==4]=0
            try:
                if(row1[0] == row2[0]):
                    data.append(matrix[row1[0],column1[0]+1])
                    data.append(matrix[row2[0],column2[0]+1])
                    continue
                if(column1[0] == column2[0]):
                    print(row1[0],row2[0])
                    print(column1[0],column2[0])
                    data.append(matrix[row1[0]+1,column1[0]])
                    data.append(matrix[row2[0]+1,column2[0]])
                    continue
                else:
                    data.append(matrix[row1[0],column2[0]])
                    data.append(matrix[row2[0],column1[0]])
                    continue
            except Exception as e:
                print(e)

    for j in range(0,len(data)):
        data[j] = int(data[j])
        
    return data
        
                
        
    
    
plain_text = (input("Enter Plain Text")).replace(" ","").lower()


if(len(plain_text)%2==1):
    if(plain_text[-1]=="x"):
        plain_text = plain_text + ("y")
    else:
        plain_text = plain_text + ("x")

plain_text_modified = redundancyCheck(plain_text)

plain_text_number_equivalent = texttonumbers(plain_text_modified)
print(plain_text_number_equivalent)

key = input("Enter the key:").replace(" ","").lower()

key_number_equivalent = texttonumbers(key)

key_number_equivalent_modified = keyredundancycheck(key_number_equivalent)      #redundanciesremoved


cipher_matrix = matrix(key_number_equivalent_modified,plain_text_modified)
print(plain_text_number_equivalent)

cipher_text_number_equivalent = encryptingplaintext(cipher_matrix,plain_text_number_equivalent)


#print(plain_text_number_equivalent)
#print(cipher_text_number_equivalent)


print("Plain-Text : {}".format(plain_text))
print("EncryptedText : {}".format(numberstotext(cipher_text_number_equivalent)))






    
    
