print("Reverse Name Generator")

while True:
    name=input("Enter the name:")
    reversed_name=name[::-1]
    print(f"your reversed name {reversed_name}")
    ans=input("\n do you want to try another name (y/n) :")
    if ans.lower()!="y":
        print("thank you")
        break
    