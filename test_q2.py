my_set={45,85,6,56,58,74}
my_list=list(my_set)
number = 56 
if number in my_list:
    index=my_list.index(number)
    square_root=number**0.5
    square=number**2
    print(f"{round(square_root,2)} is square root of {number}")
    print(f"{square} is square root of {number}")
    print(f"index of {number} is  {index}")
else:
    print ("number is not in list")

