plain=input("Enter string to be encrypted: ")
key=int(input("Enter key(supposed to be an integer): "))

def matrixcreater():
    matrix=[]
    for i in range(0,key):
        matrix.append([])
        for u in range(0,len(plain)):
            matrix[i].append("")
    return matrix

def encrypendmatrix(plain,key,matrix):
    row=0
    check=0
    for i in range(len(plain)):
    
      matrix[row][i]=plain[i]
      if row==0:
        check=1 
      elif row==key-1:
        check=0
      if check==1:
          row+=1
      else:
          row-=1
    print("final matrix is: ")
    for i in range(0,key):
        print(matrix[i])
    
str=""
def encryption(matrix,str):
    for i in matrix:
        for u in i:
        
            str+=u
    return str
matrix=matrixcreater()
encrypendmatrix(plain,key,matrix)
encryptedstring=encryption(matrix,str)
endencryption=encryptedstring.replace(" ","")
print("end encryption is: ", endencryption)

                 














