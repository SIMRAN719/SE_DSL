'''Write a Python program to compute following computation on matrix:
a) Addition of two matrices B) Subtraction of two matrices
c) Multiplication of two matrices d) Transpose of a matrix
'''

#SIMRAN SAH
#B-44

mat1,mat2,mat3=[],[],[]
def accept(row,col,mat):
    for i in range(row):
        k=[]
        mat.append(k)
        for j in range(col):
            b=int(input("enter the number in the matrix at position (%s,%s) : "%(i,j)))
            k.append(b)
def add(row1,col1,row2,col2,mat):
    mat.clear()
    if row1==row2 and col1==col2:
        for i in range(row1):
            k=[]
            mat.append(k)
            for j in range(col1):
                t=mat1[i][j]+mat2[i][j]
                k.append(t)
    else:
        print("Addition of two matrices are not possible since row and column of both the matrices are not same")
    print("Addition of two matrices : ",mat)
def sub(row1,col1,row2,col2,mat):
    mat.clear()
    if row1==row2 and col1==col2:
        for i in range(row1):
            k=[]
            mat.append(k)
            for j in range(col1):
                t=mat1[i][j]-mat2[i][j]
                k.append(t)
    else:
        print("Subtraction of two matrices are not possible since row and column of both the matrices are not same")
    print("Subtraction of two matrices : ",mat)
def multi(row1,col1,row2,col2,mat):
    mat.clear()
    if row1==row2 and col1==col2:
        for i in range(row1):
            p=[]
            mat.append(p)
            for j in range(col2):
                t=0
                for k in range(col1):
                    t+=mat1[i][k]*mat2[k][j]
                p.append(t)
    else:
        print("Multiplication of two matrices are not possible since row of first matrix and column of second matrix are not same")
    print("Multiplication of two matrices : ",mat)
def trans(row,col,mat):
    mat3.clear()
    for i in range(row):
        k=[]
        mat3.append(k)
        for j in range(col):
            t=mat[j][i]
            k.append(t)
    print("Transpose of matrix :",mat3)
def choice(a,b,c,d):
    z=input("Would you like to try other options?(y=yes/n=no) :")
    if z=='y' or z=='Y':
        menu(a,b,c,d)
    elif z=='n' or z=='N':
        print("Thank you for using the program")
    else:
        print("Enter valid entry")
        choice(a,b,c,d)
def menu(a,b,c,d):
    print("---MENU---")
    print("""1. Addition of two matrices
2. Subtraction of two matrices
3. Multiplication of two matrices
4. Transpose of a matrix
5. All operations
6. Exit""")
    z=int(input("enter your choice ="))
    if z==1:
        add(a,b,c,d,mat3)
        choice(a,b,c,d)
    elif z==2:
        sub(a,b,c,d,mat3)
        choice(a,b,c,d)
    elif z==3:
        multi(a,b,c,d,mat3)
        choice(a,b,c,d)
    elif z==4:
        print("transpose of 1st matrix")
        trans(a,b,mat1)
        print("transpose of 2nd matrix")
        trans(c,d,mat2)
        choice(a,b,c,d)
    elif z==5:
        add(a,b,c,d,mat3)
        sub(a,b,c,d,mat3)
        multi(a,b,c,d,mat3)
        print("transpose of 1st matrix")
        trans(a,b,mat1)
        print("transpose of 2nd matrix")
        trans(c,d,mat2)
    elif z==6:
        print("Thank you for using the program")
    else:
        print("Enter valid entry")
        menu(a,b,c,d)
a=int(input("enter the row of the 1st matrix : "))
b=int(input("enter the column of the 1st matrix : "))
accept(a,b,mat1)
c=int(input("enter the row of the 2nd matrix : "))
d=int(input("enter the column of the 2nd matrix : "))
accept(c,d,mat2)
menu(a,b,c,d)
            
            
