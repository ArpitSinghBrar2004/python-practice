import random

print("Music Artist Recommender")
geners={
    "rock":["AC/DC","Queen","Led Zeppelin"],
    "pop":["Taylor Swift" , "ED Sheeran", "Ariana Grande"],
    "hip-hop":["Kendrick Lamar","Drake","j.cole"]
}
choice=input("what genre do you like? (rock/pop/hip hop):")
if choice not in geners:
    print("sorry, I don't Know that genre.")
else:
    print(f"check out {random.choice(geners[choice])}")
