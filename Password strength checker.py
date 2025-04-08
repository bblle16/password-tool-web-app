import re
def check_password_strength(password):
    length_error=len(password)<8
    digit_error=re.search(r"\d", password)is None
    uppercase_error=re.search(r"[A-Z]", password)is None
    lowercase_error=re.search(r"[a-z]", password)is None
    symbol_error=re.search(r"[!@#$%^&*(){}|<>?;:'']", password)is None

    errors=[length_error,digit_error,uppercase_error,lowercase_error,symbol_error]
    score = 5 - sum(errors)

    if score <= 2:
        return "Pfft! You can do better"
    elif score == 3 or score == 4:
        return "Hm, that looks fine"
    else:
        return "DAMN THAT'S STRONG"
    
user_password = input("Enter your password: ")
strength = check_password_strength(user_password)
print(f"Password Strength: {strength}")