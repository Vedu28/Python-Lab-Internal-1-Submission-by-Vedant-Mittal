#c
height = 5
for row in range(1, height+1):
    if(row%2!=0):
        print(" " * (height-row)+" *"*row)  
