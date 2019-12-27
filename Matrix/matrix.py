#The script uses python 3 and above version

with open('input.txt', 'r') as m:
    matrix = [[int(number) for number in line.split(',')] for line in m]

# prints Matrix

print(matrix)


def column(matrix, c):
    return [row[c] for row in matrix]



cl = input("Enter the column to be extracted:")
cl = int(cl)
cols  = column(matrix, cl)

# prints coloumn Values
print(cols)

# prints row value

row = int(input("Enter the row to be extracted:"))
print(matrix[row])

#quardrant
q = int(input("Enter the number to be quardrant:"))
qrdnt =  [matrix[q][:2], matrix[q][:2]]
print(qrdnt)
