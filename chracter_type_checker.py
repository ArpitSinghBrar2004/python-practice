print("Character type checker ")
char= input("Enter the Character")
if char.isalpha():
    print(f"{char} is alphabet")
elif char.isnumeric():
    print(f"{char} is number")
else:
    print(f"{char} is a special Character ")