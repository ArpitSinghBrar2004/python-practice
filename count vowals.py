my_string=input("enter String \n")
lower_case=my_string.lower()
vowal_count=0
for char in lower_case:
    if char in {'a','e','i','o','u'}:
        vowal_count+=1
print(f"Totl vowals:{vowal_count}")