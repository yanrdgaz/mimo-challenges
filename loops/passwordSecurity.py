# 1.
password_length = 6
counter = 1
permutations = 1

# 2.
while counter <= password_length:
    permutations = permutations * counter
    counter += 1
print(f"The possible combination of a {password_length}-character password is: {permutations}")

# 3.
attempts = 5
max_lock = permutations / attempts
max_lock = int(max_lock)
print(f"The maximum number of times the account might be locked is {max_lock} times.")

# 4.
locks = 0
total_lock_time = 0
lock_time_multiplier = 5

# 5.
for i in range(max_lock):
    locks += 1
    total_lock_time += locks*lock_time_multiplier
    print(f"Your account is locked for {lock_time_multiplier*locks} minutes")

# 6.
print(f"Assuming the hacker only got the password right with the last possible combination, your account would have "
      f"been locked for {total_lock_time} minutes in total.")
