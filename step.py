print("🚶Step counter 🚶‍♀️")
goal=int(input ("\n🎖 what is your daily step goal?🎖\n"))
total_steps=int(input("\n ✨How many steps have you taken today ?✨\n "))
remaining= goal-total_steps
if remaining>0:
    print(f"🎯you need {remaining} more steps to reach your goal")
else:
    print(f"⭐️congratulations! you've exceed your goal by {-remaining} steps!⭐️")
