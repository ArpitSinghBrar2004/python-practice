# table_of_n_number 
num_1=int(input("enter a number you want table of"))
ans=0
if num_1>0:
    for i in range(1,10+1):
        ans=num_1*i
        print(f"{num_1}*{i}={ans}")
        i+1
elif num_1==0:
    print("enter a number >0")