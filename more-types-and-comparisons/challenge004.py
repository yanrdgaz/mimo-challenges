# Lorde forgot her password and she's using a program to restore it. The program checks if her new password is
# different from the old one. It also makes Lorde enter the new password twice to make sure it's written correctly.
# Let's finish that program! Tasks (2): Use the inequality operator in the compare_old_new to show that the passwords
# are not the same. Make sure that the new_password matches the repeat_new_password

old_password = "hello123"
new_password = "goodbye321"
compare_old_new = old_password != new_password
repeat_new_password = "goodbye321"
compare_new = new_password == repeat_new_password

print(f"Is new password different from old password? {compare_old_new}")
print(f"Has new password been introduced correctly? {compare_new}")
