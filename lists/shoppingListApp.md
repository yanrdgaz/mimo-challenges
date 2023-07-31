1. Rachel plans to go to the supermarket tomorrow. She checks the house and writes down a list of items she needs. Let's create a variable to represent the shopping list. Tasks (1): Create a shopping_list variable and set ["potato", "apple", "oil", "milk", "toilet paper"] as its value.

2. Rachel's dad wants her to buy some batteries for him. Let's append a new batteries item to the shopping list. Tasks (2): Call the append() function on shopping_list to append "batteries" to the shopping list.
Print shopping_list to confirm that the shopping list includes the batteries.

3. Rachel's sister, Riley, loves chocolate and Rachel knows a store in the supermarket where they sell fair-trade and really good quality chocolate. Since the store is at the entrance of the supermarket, let's make it the first item on the list to spare Rachel the detour! Tasks (1): Before the print statement, call the insert() function on shopping_list to insert "chocolate" as the first item of the shopping list. We can confirm that chocolate is on the shopping list when it is printed. 

4. Rachel just remembered that Riley only likes dark chocolate. We already inserted "chocolate" into the list but we can change it to "dark chocolate". Tasks (1): Before the print statement, change the value of the first element of the shopping_list from "chocolate" to "dark chocolate", using its list index. We can confirm the change when the list is printed.

5. Rachel's dad just called to inform Rachel that he found some batteries in the garage. Let's take the batteries out of the shopping list. Tasks (1): Before the print statement, call the pop() function on shopping_list to take "batteries" out of the shopping list. We can confirm that batteries are out of the shopping list when it is printed.

6. Rachel went for her grocery run and came back with a list of items she bought. Now, we want to help Rachel find out what she did not manage to buy. To begin, let's start by creating some variables. Tasks (2): Create a purchased_list variable and set ["dark chocolate", "potato", "apple", "oil", "toilet paper", "fish fingers"] as its value. Create a unavailable_items variable and set [] as its value.

7. Rachel wants to make sure that she's bought everything that was on the shopping list. Let's go through the shopping list and see if each item is on the purchased list as well. If it is not on the purchased list, we'll add it to the list of items that she did not purchase. Tasks (3): Loop through shopping_list using a for-loop. For every item in shopping_list, check if the item is not in purchased_list. If the above condition is fulfilled, append the item to unavailable_items.

8. Awesome! We have the items she didn't manage to buy. Let's print them so that Rachel can see what she needs to buy next time. If there are no items on the list, we'll print a message to let her know that she managed to purchase everything she needed. Tasks (4): After the for-loop, check if the length of unavailable_items is greater than 0. If the condition mentioned above is fulfilled, print this f-string: f"Here's a list of items on your shopping list that you did not purchase: {unavailable_items}" Code an else block after the if block. Print the following f-string within the else block: f"Good job! You bought everything on your shopping list!"

9. To better manage her budget, Rachel also wants to know if she purchased any items on impulse that were not on the shopping list. To get started, let's create a variable to store these items. Tasks (1): After the else block, create a special_items variable and store an empty list in it.

10. Let's go through the purchased list and see if there are items that were not on the shopping list. If it is not on the shopping list, we'll add it to the list of items that she purchased on impulse. Tasks (3): Loop through purchased_list using a for-loop. For every item in purchased_list, check if the item is not in shopping_list. If the above condition is fulfilled, append the item to special_items.

11. Great! We have the items she probably didn't need but bought anyways. Let's show them to Rachel so that she's aware. Tasks (2): Outside the for-loop, check if the length of special_items is greater than 0. If the condition mentioned above is fulfilled, print the following f-string: f"Here's a list of items you purchased but was not on your shopping list: {special_items}"

Congratulations! 
With that, we are all done with this shopping list app. Hopefully, this will help Rachel with her grocery shopping and budgeting next time. We are not running any tests in this lesson so feel free to explore and play around with the code. Perhaps you can append or insert more items to the list! Have fun!
