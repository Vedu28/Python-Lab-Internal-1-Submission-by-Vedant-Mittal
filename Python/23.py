#23 matrix transpose
x=[[1,2,4],[4,5,6],[7,0,9]]
y=[[6,3,7],[8,3,9],[3,2,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for row in range(len(x)):
    for column in range(len(x[0])):
        result[row][column]=x[column][row]
for r in result:
    print(r)
