import random
print("Enter the word")
print("Unscamble the letters to find the word !")

words =["python","codeing","game","computer","fun","learn"]

while True:
    original_word = random.choice(words)
    letters= list(original_word)
    random.shuffle(letters)
    scrambled="".join(letters)
    print(f"\n  Scrambled word : {scrambled}")
    guess=input("whats the word ?:").lower()
    if guess==original_word:
        print("congrats ! you win !")
    else:
        print(f"sorry ! the word was : {original_word}")
    again = input ("do you want to play agian ?(y/n)").lower()
    if not again.startswith("y"):
        print("goodbye!")
        break