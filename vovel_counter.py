print("Vowel Counter")
while True:
    word=input("Enter the text or Quit to Exit :")
    if word.lower()==quit:
        print("Good Bye")
        break
    vowel=0
    for letter in word.lower():
        if letter in ["a","e","i","o","'u"]:
            vowel+=1
    print(f"The text have {vowel} vowels!")
