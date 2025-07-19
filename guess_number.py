import random
print("wellcome to number guessing game")
print("I am thinking of a number between 1 and 100. you have 10 attempts")

playing=True

while playing:
    secre_number = random.randint(1,10)
    attempts = 0
    max_attempts=10
    game_over = False
    while attempts<max_attempts and not game_over:
        try:
            guess=int(input(f"Atempts {attempts +1}/{max_attempts}.Enter your Guess"))
        except:
            print("Please enter a valid number")
            continue
        attempts +=1
        if guess < secre_number:
            print("too low! Try a higher number !")
        elif guess>secre_number:
            print("too high! Try a lower number !")
        else:
            print(f"congrats! you guessed the number {secre_number} in {attempts} attempts")
            game_over=True
        if attempts < max_attempts and not game_over:
            print(f"you have {max_attempts-attempts} attempts left !")
    if  not game_over:
        print(f"Game over! The number was {secre_number}")
    play_again=input("would you like to play again? (yes/no): ").lower()
    if play_again.startswith("y"):
        print("new game starting ...\n")
    else:
        print("goodbye!")
        playing=False
