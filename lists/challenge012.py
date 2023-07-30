# You decide to plan your daily meals using Python lists. Tasks (4): Within the variable meals, create a list
# containing your meals for breakfast, lunch, and dinner in this order: "omelet", "salad", and "chicken". Alter the
# first print statement to include the lunch menu. A friend stops by with pizza! Change the meals list dinner value (
# the last value) to "pizza". Alter the second print statement to include the current dinner menu item!

meals = ['omelet', 'salad', 'chicken']

print(f"Lunch menu: {meals[1]}")

meals.insert(2, 'pizza')

print(f"Dinner menu: {meals[2]}")
