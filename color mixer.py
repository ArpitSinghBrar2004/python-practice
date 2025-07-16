print ("color mixer")
color_mixer={
    ("red","blue"):"purple",
    ("red","yellow"):"orange",
    ("blue","yellow"):"green",
    ("blue","green"):"teal",
    ("white","red"):"pink",
    ("red","green"):"brown",
}
while True:
    color1 = input("\n Enter the 1st color :").lower()
    color2 = input("\n enter the 2nd color: ").lower()
    mix= None

    if (color1,color2) in color_mixer:
        mix = color_mixer[(color1,color2)]
    if mix :
        print(f"when you mix {color1} and {color2},you get {mix}!")
    else:
        print("I don't know what those colors make when mixed.")
    if not  input("\n mix more colors ?(y/n)").lower().startswith("y"):
        print("good bye")
        break