password = input("Enter password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.islower() for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1

if strength <= 1:
    print("Weak Password")
elif strength == 2 or strength == 3:
    print("Medium Password")
else:
    print("Strong Password")
