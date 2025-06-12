#factors_of_n_numbers 
num_2=int(input("enter a number you want factor of "))
if (num_2>1):
    for i in range(2,num_2):
        if(num_2%i==0):
            print(f"{i} is the factor of {num_2}")
else:
    print("enter a valid number")