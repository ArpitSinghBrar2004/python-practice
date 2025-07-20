import time
print("\n Countdown timer")
print ("count down from your chosen seconds !")

while True:
    seconds = int (input("\n enter seconds to countdown from :"))
    print(f"staring count from {seconds} seconds.! ")

    for i in range(seconds,0,-1):
        print(f"{i} seconds remaining ...")
        time.sleep(1)
    
    print("\n Countdown Complete !")
    again= input("\n start another countdown? (yes/no):").lower()
    if not again.startswith("y"):
        print("Good bye !")
        break