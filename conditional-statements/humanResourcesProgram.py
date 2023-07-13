# 1.
assessment_score = 85
location = "Canada"

# 2.
if location == "US" and assessment_score >= 75:
    print(f"Your assessment score is {assessment_score}/100! You're hired!")

# 3.
else:
    print(f"Thank you for your interest, we regret to inform you that we will not be moving forward with your "
          f"application.")

# 4.
assessment_score = 85
location = "Canada"

if (location == "US" or location == "Canada") and assessment_score >= 75:
    print(f"Your assessment score is {assessment_score}/100! You're hired!")
else:
    print(f"Thank you for your interest, we regret to inform you that we will not be moving forward with your "
          f"application.")

# 5.
assessment_score = 85
location = "Canada"

if (location == "US" or location == "Canada") and assessment_score >= 75:
    print(f"Your assessment score is {assessment_score}/100! You're hired!")

elif location != "US" and location != "Canada" and assessment_score >= 75:
    print(f"Apologies, you are based in {location} but this role requires you to be based in the US/Canada. Would you "
          f"be interested in another role?")

else:
    print(f"Thank you for your interest, we regret to inform you that we will not be moving forward with your "
          f"application.")
