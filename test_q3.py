dic={"name":"Arpit","age":21,"course":"DS"}
name=dic["name"]
cource=dic["course"]
print ("Name:",name)
print ("Cource",cource)
reversed_name=name[::-1]
reversed_cource=cource[::-1]
print ("Cource:",reversed_cource)
print ("Name:",reversed_name)
for key in dic:
    if key=="course":
        print(dic[key])

#take 6 input from user than find min no. without min func 
li=[]
while True:
    num=int(input("Enter number you want to add in list "))
    li.append(num)
    if len(li)==6:
        li.sort()
        print(f"{li[0]} is the smallest number")
        print(f"{li[5]} is the largest number ")

        break
