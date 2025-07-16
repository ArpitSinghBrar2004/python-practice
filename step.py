print("🚶Step counter 🚶‍♀️")
goal=int(input ("🎖 what is your daily step goal?🎖"))
total_steps=int(input("✨How many steps have you taken today ?✨"))
remaining= goal-total_steps
if remaining>0:
    print(f"🎯you need {remaining} more steps to reach your goal")
else:
    print(f"⭐️congratulations! you've exceed your goal by {-remaining} steps!⭐️")
