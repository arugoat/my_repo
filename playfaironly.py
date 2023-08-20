def jremover(x):
    u=x.replace("j","i")
    return u

def conversionofinput(x):
    x.lower()
    newx=''
    for i in x:
        if i==" ":
            continue
        else:
            newx+=i
    return newx 


def merging2(x):
    a=0
    list1=[]
    for u in range(0,len(x)-1,2):
        list1.append(x[u:u+2])
        a=u
    
    return list1


#taking "x" as the filler
def fillers(x):
    newword=x
    length = len(x)
    if length%2 == 0: # used to check if no of characters are even
        for i in range(0,length, 2):
            if (x[i] == x[i+1]) and (x[i]!="x"):
                newword = x[0:i+1] + 'x' + x[i+1:]
                
                newword=fillers(newword)
                break
            elif x[i] == x[i+1] and x[i]=="x":
                newword = x[0:i+1] + 'q' + x[i+1:]
                
                newword=fillers(newword)
                break

            else:
                newword = x
    else:
        for i in range(0, length-1, 2):
            if (x[i] == x[i+1]) and (x[i]!="x"):
                newword = x[0:i+1] + 'x' + x[i+1:]
                newword=fillers(newword)
                break
            elif (x[i] == x[i+1]) and x[i]=="x":
                newword = x[0:i+1] + 'q' + x[i+1:]
                
                newword=fillers(newword)
                break
            else:

                newword = x
    if len(newword)%2==1:
        if newword[-1]=="x":
            newword=x+"q"
        else:
            newword=x+"x"
        newword=fillers(newword)
    return newword
list1= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def matrixcreater(key,set1):
    finallist = []
    for i in key:
        if i not in finallist:
            finallist.append(i)
    for i in list1:
        if i not in finallist:
            finallist.append(i)
 
    matrix = []
    while len(finallist)>0:
        matrix.append(finallist[:5])
        finallist = finallist[5:]
 
    return matrix

def finder(matrix,element):
    for i in range(5):
        for u in range(5):
            if matrix[i][u]==element:
                return i,u


def rowencryption( matrix,r_a, c_a, r_b, c_b):
    
    #when characters are in same column)
    
    encrypt1 = matrix[r_a][(c_a+1)%5]
    
 
    encrypt2 = matrix[r_b][(c_b+1)%5]
    return str(encrypt1)+str(encrypt2)

def rowdecryption(matrix, r_a, c_a, r_b, c_b):
    
    #when characters are in same column)
    
    encrypt1 = matrix[r_a][(c_a-1)%5]
    
 
    encrypt2 = matrix[r_b][(c_b-1)%5]
    return str(encrypt1)+str(encrypt2)


def columnencrption( matrix,r_a, c_a, r_b, c_b):
    
    
    #when character is in last column)
    
    encrypt1 = matrix[(r_a+1)%5][c_a]
    
 
    encrypt2 = matrix[(r_b+1)%5][c_b]
    return str(encrypt1)+str(encrypt2)

def columndecryption( matrix,r_a, c_a, r_b, c_b):
    
    
    #when character is in last column)
    
    encrypt1 = matrix[(r_a-1)%5][c_a]
    
 
    encrypt2 = matrix[(r_b-1)%5][c_b]
    return str(encrypt1)+str(encrypt2)




def normalencryption(matrix, r_a,c_a,r_b,c_b):
    encrypt1=matrix[r_a][c_b]
    encrypt2=matrix[r_b][c_a]
    return str(encrypt1)+str(encrypt2)

def normaldecryption(matrix, r_a,c_a,r_b,c_b):
    encrypt1=matrix[r_a][c_b]
    encrypt2=matrix[r_b][c_a]
    return str(encrypt1)+str(encrypt2)


def encrypter(plaintext,key):
    encryptedtext=""
    encryptabletext=conversionofinput(jremover(plaintext))
    finalplaintext=merging2(fillers(encryptabletext))
    matrix=matrixcreater(key,list1)
    for i in range(0,len(finalplaintext)):
                   
                   r_a,c_a =finder(matrix,finalplaintext[i][0])
                   r_b,c_b=finder(matrix,finalplaintext[i][1])
                   if r_a==r_b:
                       encryptedtext+= rowencryption(matrix,r_a,c_a,r_b,c_b)
                   elif c_a==c_b:
                       encryptedtext+= columnencrption(matrix,r_a,c_a,r_b,c_b)
                   else:
                       encryptedtext+= normalencryption(matrix,r_a,c_a,r_b,c_b)
    print("the encrypted text is: ",encryptedtext)
    return encryptedtext

def decrypter(encryptedtext,key):
    plaintext=""
    decryptabletext=conversionofinput(jremover(encryptedtext))
    finalencryptedtext=merging2(fillers(decryptabletext))
    matrix=matrixcreater(key,list1)
    
    
    for i in range(0,len(finalencryptedtext)):
                   
                   r_a,c_a =finder(matrix,finalencryptedtext[i][0])
                   
                   
                   r_b,c_b=finder(matrix,finalencryptedtext[i][1])
                   if r_a==r_b:
                       plaintext+= rowdecryption(matrix,r_a,c_a,r_b,c_b)
                   elif c_a==c_b:
                       plaintext+= columndecryption(matrix,r_a,c_a,r_b,c_b)
                   else:
                       plaintext+= normaldecryption(matrix,r_a,c_a,r_b,c_b)
    print("the decrypted text is ",plaintext)
    return plaintext


key=input("Enter key: ")

TextTobeEncrypted=input("Enter text to be encrypted: ")
EncryptedText=encrypter(TextTobeEncrypted,key)
print ("Encrypted Text is: ", EncryptedText)

TextToBeDecrypted=input("Enter encrypted text: ")
DecryptedText=decrypter(TextToBeDecrypted,key)
print ("Decrypted Text is: ", DecryptedText)        




