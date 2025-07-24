#nested lists

matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(matrix[0])     
print(matrix[1][2]) 

#sum
total = 0
for row in matrix:
    for num in row:
        total+=num

print("Sum =", total)


#transpose
rows=len(matrix)
cols=len(matrix[0])

transpose=[]

for i in range(cols):
    new_row=[]
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

print("Transpose:")
for row in transpose:
    print(row)



#max in each row
for i,row in enumerate(matrix):
    max_value=max(row)
    print(f"Max in Row {i+ 1}: {max_value}")


#sum of diagonals

n=len(matrix)
sum = 0
for i in range(n):
    sum+=matrix[i][i]
print("Diagonal Sum:",sum)

# matrix multiplication

A = [[1, 2, 3],[4, 5, 6]]

B = [[7, 8],[9, 10],[11, 12]]

result = []

for i in range(len(A)): 
    row = []
    for j in range(len(B[0])):  
        sum = 0
        for k in range(len(B)): 
            sum += A[i][k] * B[k][j]
        row.append(sum)
    result.append(row)
