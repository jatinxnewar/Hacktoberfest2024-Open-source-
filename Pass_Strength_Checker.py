import re

# Function to check the password strength
def check_password_strength(password):
    strength = {"length": False, "digit": False, "uppercase": False, "lowercase": False, "special": False}
    
    # Check password length (at least 8 characters)
    if len(password) >= 8:
        strength["length"] = True

    # Check if it contains at least one digit
    if re.search(r"\d", password):
        strength["digit"] = True

    # Check if it contains at least one uppercase letter
    if re.search(r"[A-Z]", password):
        strength["uppercase"] = True

    # Check if it contains at least one lowercase letter
    if re.search(r"[a-z]", password):
        strength["lowercase"] = True

    # Check if it contains at least one special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength["special"] = True

    # Assess overall strength
    if all(strength.values()):
        return "Strong"
    elif strength["length"] and (strength["digit"] or strength["uppercase"] or strength["lowercase"]):
        return "Medium"
    else:
        return "Weak"

# Function to display password feedback
def give_feedback(password):
    feedback = []
    
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r"\d", password):
        feedback.append("Password should contain at least one digit.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password should contain at least one special character.")
    
    if feedback:
        print("Feedback to strengthen your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password is strong!")

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
    
    if strength != "Strong":
        give_feedback(password)

if __name__ == "__main__":
    main()
