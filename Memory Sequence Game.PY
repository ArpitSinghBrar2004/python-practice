import random 
import time
import os
def clear_screen():
    # clear terminal
    os.system("cls" if os.name =="nt" else "clear")
print("***Memory Sequence Game***")
print("Remember the sequence and type it back !")
print("\nRules")
print("watch the number appear one by one ")
print("after the sequence is shown , type it back in order")
print("each round adds one more number to remembr")
print("How far can you go \n ")
input("press enter to start ....")
sequence=[]
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1,9))
    
    clear_screen()

    print(f"\n==Round {current_round}==")
    print(f"remember this sequence of {len (sequence)} numbers:")

    for number in sequence:
        time.sleep(1)
        print(f"\n{number}")
        time.sleep(1)
        clear_screen()

    print("now repeat the sequence by typing each number ,seprated by spaces:")
    player_ans= input(">")
    try:
        player_sequnece = [int (num) for  num in player_ans.split()]
    except ValueError:
        print("please enter numbers only !")
        game_over=True
        continue
    if player_sequnece == sequence:
        print(f"congrats ! you remembred all {len(sequence)} numbers !")
        current_round +=1
        time.sleep(2)
    else:
        print(f"Game over! you remembred all {current_round -1} numbers !")
        print(f"THE CORRECT SEQUENCE WAS :{"".join(str(num) for num in sequence)}")
        game_over = True
    if game_over:
        play_again = input("play again ? (yes/no):").lower()
        if play_again.startswith("y"):
            sequence=[]
            current_round=1
            game_over=False 
        else:
            print("thanks for playing")

