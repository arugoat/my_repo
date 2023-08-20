n=int(input("enter columns no."))
l=[]
checker=0
def matrixformer(l,n):
 
 for i in range(n):
    
    l.append([])
    for j in range(n):
        l[i].append(0)
        duplicate=l
def safe(list1,i,j,n):
    for k in range(0,n):
        if list1[k][j]=="Q" :
            return False
    for k in range(0,n):
        if list1[i][k]=="Q" :
            return False
    for k in range(0,n):
        for l in range(0,n):
         if list1[k][l]=="Q" and (k-l==i-j or k+l==i+j) :
            return False
    return True
def printSol(board):
 for i in range(n):
  for j in range(n):
   print (board[i][j],end=' ')
  print()

def solveNQUtil(board, col,n):
    # base case: If all queens are placed
    # then return true
    if col >= n:
        return True
 
    for i in range(n):
 
        if safe(board, i, col,n):
            # Place this queen in board[i][col]
            board[i][col] = "Q"

            # recur to place rest of the queens
            if solveNQUtil(board, col + 1,n) == True:
                return True
 
            #the above function is used to check if situation is suitable for subsequent columns
            
            board[i][col] = 0
 
    # if the queen can not be placed in any row in
    # this column col  then return false
    return False
 
# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one  of the
# feasible solutions.
counter=0
def solveNQ(board):
 
    if solveNQUtil(board, 0,n) == False:
        print ("Solution does not exist")
        global checker
        checker=1
        return False
 
    printSol(board)
    return True
    counter+=1
p=[] 
matrixformer(l,n)
solveNQ(l)
p.append(l)



def solveNQUnique(board, col,n,p):
    # base case: If all queens are placed
    # then return true
    
    if col >= n:
        return True
 
    for i in range(n):
 
        if safe(board, i, col,n):
            # Place this queen in board[i][col]
            board[i][col] = "Q"
            if board not in p:
            # recur to place rest of the queens
              if (solveNQUnique(board, col + 1,n,p) == True):
                
                return True
 
            #the above function is used to check if situation is suitable for subsequent columns
            
            board[i][col] = 0
 
    # if the queen can not be placed in any row in
    # this column col  then return false
    return False

def solveNQuniq(board,u,):
 
    if solveNQUnique(board, 0,n,u) == False:
        print ()
        global checker
        checker=1
        return False
 
    printSol(board)
    return True
 
while checker!=1:
        print()
        print("next solution is \n")
        duplicate=[]
        matrixformer(duplicate,n)         
        solveNQuniq(duplicate,p)
        p.append(duplicate)
        counter+=1



print("the number of solutions is ",counter)
