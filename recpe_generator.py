import random
print("Random Recipe Generator")
proteins = ["chicken","eggs","fish","tofu","beef","paneer"]
veggies= ["broccoli","carots","spinach","bell peppers","mushroom"]
carbs = ["rice", "pasta","potatoes","quinoa","bread"]
methods = ["baked","grilled","stir-fried","roasted","sauteed"]
flavors=["garlic", "lemon","spicy","herb","sweet & sour"]
while True:
    protein=random.choice(proteins)
    veggi=random.choice(veggies)
    carb=random.choice(carbs)
    method=random.choice(methods)
    flavor=random.choice(flavors)
    print(f"\n Your Randon Recipe is :{flavor} {method} {protein} with {veggi} and {carb}")

    if not input("\n Generate another one? (y/n): ").lower().startswith("y"):
        print("Good Bye")
        break

