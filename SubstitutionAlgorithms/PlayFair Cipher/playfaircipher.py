
import string


characters = list(string.ascii_lowercase)




def texttonumbers(data):
    
    numberequivalent = []
    for element in data:
        numberequivalent.append(characters.index(element))

def redundancyCheck(data):
    for i in range(0,len(data)-1):
        if(data[i]==data[i+1]):
            if(data[i+1]=="x"):
                data = data.replace("{}{}".format(data[i+1],data[i+1]),"{}y".format(data[i+1]))
            else :
                data = data.replace("{}{}".format(data[i+1],data[i+1]),"{}x".format(data[i+1]))
    print(data)
    return data
        
    


plain_text = (input("Enter Plain Text")).replace(" ","").lower()


if(len(plain_text)%2==1):
    if(plain_text[-1]=="x"):
        plain_text = plain_text + ("y")
    else:
        plain_text = plain_text + ("x")

plain_text_modified = redundancyCheck(plain_text)
    
    
