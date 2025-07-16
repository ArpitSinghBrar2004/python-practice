import random
firstName=["sky","star","Moon","Sun","fire","ice"]
lastName=["rider","walker","hunter","seeker","dancer","keeper","singer"]
print("Fantasy Name Generator")
cout=int(input("how many names do you want : "))
for i in range(cout):
    first_Name=random.choice(firstName)
    last_Name=random.choice(lastName)
    print(f"{first_Name}{last_Name}")
