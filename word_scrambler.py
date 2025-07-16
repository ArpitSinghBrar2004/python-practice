import random

print("word scrambler")
while True:
    word=input("enter a word to scramble(or Quit to exit)")
    if word.lower() =="quit":
        print("Goodbye!")
        break
    letters = list(word)
    random.shuffle(letters)
    print(f"scrambled:{"".join(letters)}")