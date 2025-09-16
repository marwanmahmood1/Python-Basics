# =======================
#      IF STATEMENTS
# =======================

# These are the three main statements we use for decision-making based on factors specified by the user:

# 1- Simple if statement
age = 20
if age >= 18:
    print("You are an adult.")

# 2- if - else statement
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's not too hot.")

# 3- if - elif (else if) - else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# We could also implement some applications to further enhance the decision-making process for better results:

# if statements using logical operators (and/or)
has_passport = True
has_ticket = False

if has_passport and has_ticket:
    print("You can board the flight.")
elif has_passport and not has_ticket:
    print("You need a ticket!")
else:
    print("No passport, no travel.")

# Nested if statements
number = 10
if number > 0:
    if number % 2 == 0:
        print("Positive and even.")
    else:
        print("Positive and odd.")
