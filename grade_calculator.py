print("Grade Claculator")
score=[]

while True:
    scores = input("Enter a score or ('Done to exit '):")
    if scores.lower()=="done":
        print("Good Bye")
        break
    score.append(float(scores))
    average=sum(score)/len(score)
    print(f"Average score:{average:.1f}")
    if average>=90:
        print("Grade:A")
    elif average>=80:
        print("Grade:B")
    elif average>=70:
        print("Grade:C")
    else:
        print("Grade:D or F")