num=10 
max_row=4
for row in range(1,max_row+1):
    print(" "*(max_row-row),end=" ")
    for _ in range(row):
        if num<=6:
            print(f"{num}",end=" ")
        else:
            print(num,end=" ")
        num-=1
    print()
