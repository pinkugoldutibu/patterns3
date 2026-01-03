RowSize = int(input("enter the number of rows: "))
if RowSize %2==0:
    halfiamrow = int(RowSize/2)
else:
    halfiamrow = int(RowSize/2)+1
space = halfiamrow - 1
for i in range (1, halfiamrow +1):
    for j in range(1, space +1): 
        print(end=" ")
    space = space - 1 
    num = 1
    for j in range(2 * i - 1):
        print(end = str(num))
        num = num+1 
    print()
space = 1
for i in range(1, halfiamrow):
    for j in range(1, space+1):
        print(end=" ")
    space = space +1
    num = 1
    for j in range(1, 2*(halfiamrow - i )):
        print(end = str(num))
        num = num+1
    print()
