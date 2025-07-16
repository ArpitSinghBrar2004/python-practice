num=int(input("Enter the number you want to check is prime"))
a=False
if num>1:
    for i in range(2,num):
        if num%i ==0:
            a=True
            break
if a:
    print(f"{num}number is not prime ")
else:
    print(f"{num} number is prime")