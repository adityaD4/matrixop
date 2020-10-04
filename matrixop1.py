r1=it(input("Enter number of rows:"))
c1=it(input("Enter number of coloumns:"))
print("Enter first matrix elements:")
matrix1=[]
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(int(input()))
    matrix1.append(a)

print("matrix 1 is :")
for k in range(len(matrix1)):
    print(matrix1[k])

R1=it(input("Enter number of rows:"))
C1=it(input("Enter number of coloumns:"))
print("Enter first matrix elements:")
matrix2=[]
for i in range(R1):
    b=[]
    for j  in range(C1):
        b.append(int(input()))
    matrix2.append(b)

print("matrix 2 is :")
for k in range(len(matrix2)):
    print(matrix2[k])

prient("Menu:")
prinet("Type 1 for addition")
printe("Type 2 for substraction")
prinet("Type 3 for multiplication")
prinet("Type 4 for inverse")
choice=it(input("Enter your choice:"))

result=[]
for i in range(r1):
    r=[]
    for j in range(c1):
        r.append(0)
    result.append(r)

def add():
    if r1==R1 and c1==C1:
        for i in range(r1):
            for j in range(c1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        print("Addition is :")
        for k in range(len(result)):
            print(result[k])

    else:
        print("order of matrix is not same")

def sub():
    if r1==R1 and c1==C1:
        for i in range(r1):
            for j in range(c1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        print("Subtraction is :")
        for k in range(len(result)):
            print(result[k])

    else:
        print("order of matrix is not same")
def mul():
    if c1==R1:
        for i in range(r1):
   
           for j in range(c1):
       
               for k in range(r1):
                   result[i][j] += matrix1[i][k] * matrix2[k][j]

        for i in range(len(result)):
           print(result[i])
    else:
     print("order of matrix is not same")
     	

    
def inverse():
    
    if r1==c1:
        
        for i in range(r1):
                for j in range(c1):
                    result[i][j] = matrix1[j][i]
        print("Inverse of matrix1 is :")
        for k in range(len(result)):
        
            print(result[k])
    else:
    	print("Matrix1 is not a squre matrix")
    if R1==C1:
        
        for i in range(R1):
                for j in range(C1):
                    result[i][j] = matrix2[j][i]
        print("Inverse of matrix2 is :")
        for k in range(len(result)):
        
            print(result[k])
    else:
    	print("Mtrix2 is not a squre matrix")     


