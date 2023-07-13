# Entering certain establishments like a club depends on being over the age limit and having a reservation. Let's
# write a Python program to check if a person can enter. Tasks (2): If age is greater than or equal to 18 and
# hasReservation is True, set the result to True. Print Entry granted:  followed by the result. For example,
# if the result is False, then print Entry granted: False.

age = 21
hasReservation = True
result = False

if age >= 18 and hasReservation:
    result = True
    print(f"Entry granted: {result}")

else:
    print(f"Entry granted: {result}")
