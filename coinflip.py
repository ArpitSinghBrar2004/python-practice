import random
print("Coin Flip Game")
print("guess heads or tails :")

while True:
    guess=input(" \n Enter your guess (heads/tails)").lower()
    if guess != "heads" and guess != "tails":
        print("please enter 'heads' or 'tails'")
        continue
    flip = random.choice(["heads","tails"])
    print(f"\n coin shows :{flip}")
    if guess==flip:
        print("you Won! You guessed correctly.")
    else:
        print("sorry,wrong guess .Try again!")
    again=input("\n play again ? (Yes,No):").lower()
    if not again.startswith("y"):
        print("goodbye!")
        break