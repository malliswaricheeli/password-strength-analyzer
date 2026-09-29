import re

def analyze_password(password):
    score = 0
    feedback = []

    # 1. Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase length to at least 8 (ideally 12+) characters.")

    # 2. Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 3. Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 4. Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one numerical digit (0-9).")

    # 5. Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    # Determine strength rating based on total score
    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# --- Execution Example ---
if __name__ == "__main__":
    user_pass = input("Enter a password to test: ")
    rating, suggestions = analyze_password(user_pass)
    
    print(f"\nPassword Strength: {rating}")
    if suggestions:
        print("Suggestions for Improvement:")
        for item in suggestions:
            print(f" - {item}")
    else:
        print("Great job! Your password meets all standard policy requirements.")
