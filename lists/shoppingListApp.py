# 1.
shopping_list = ["potato", "apple", "oil", "milk", "toilet paper"]

# 2.
shopping_list.append("batteries")
print(shopping_list)

# 3.
shopping_list.insert(0, "chocolate")
print(shopping_list)

# 4.
shopping_list.pop(0)
shopping_list.insert(0, "dark chocolate")
print(shopping_list)

# 5.
shopping_list.pop()
print(shopping_list)

# 6.
purchased_list = ["dark chocolate", "potato", "apple", "oil", "toilet paper", "fish fingers"]
unavailable_items = []

# 7.
for item in shopping_list:
    if item not in purchased_list:
        unavailable_items.append(item)

# 8.
if len(unavailable_items) > 0:
    print(f"Here's a list of items on your shopping list that you did not purchase: {unavailable_items}")
else:
    print(f"Good job! You bought everything on your shopping list!")

# 9.
special_items = []

# 10.
for item in purchased_list:
    if item not in shopping_list:
        special_items.append(item)

# 11.
if len(special_items) > 0:
    print(f"Here's a list of items you purchased but were not on your shopping list: {special_items}")
