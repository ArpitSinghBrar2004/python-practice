import time
import random

word_pairs={
    "sky" :["blue","cloud","bird","fly","sun"],
    "water":["drink","ocean","swim","fish","boat"],
    "food":["eat","cook","tasty","meal","restaurant"],
    "music":["song","dance","listen","band","rythm"],
    "book":["read","story","page","author","library"],
    "tree":["leafe","green","forest","wood","shade"],
    "car":["drive","road","wheel","travel","speed"],
    "dog":["pet","bark","walk","loyal","puppy"]
}
print("\n== Word Associattion Game ==")
print("Resond with a related word quickly !")

score=0
rounds=0

while True:
    prompt = random.choice(list(word_pairs.keys()))
    related_words = word_pairs[prompt]

    print(f"\n promt word : {prompt.upper()}")
    print("quick! type a word related to this prompt")

    start_time=time.time()
    response= input(">").lower().strip()
    response_time = time.time() - start_time

    print("response time",response_time)

    if response in related_words:
        points=max(1,5 -int(response_time))
        score+=points
        print(f"good association ! +{points} points (answered in {response_time:.1f}s)")
    else:
        print(f"not a common association .related word included :{','.join(related_words)}")
    rounds +=1
    print(f"score:{score}/{rounds*5}possible points")
    if input("\n play again?(yes/no):").lower().startswith('n'):
        print(f"final score : {score}.thanks for playing ")
        break