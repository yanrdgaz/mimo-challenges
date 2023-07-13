# We'll print the number of read or unread notifications that a user received. Tasks (2): If unread is not 0,
# print You have {unread} unread messages. Use f-string to display the value of unread inside the string. Else print
# No unread messages. Check your {read} read messages. Use f-string to display the value of read inside the string.

read = 5
unread = 4

if unread != 0:
    print(f"You have {unread} unread messages")

else:
    print(f"No unread messages. Check your {read} read messages")
