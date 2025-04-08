import re
import random
import string
import getpass

#password strength checker
def check_password_generator(password):
    length_error=len(password)<8
    uppercase_error=re.search(r"[A-Z]", password) is None
    digit_error=len(r"\d",password)is None
    lowercase_error=re.search(r"[a-z]", password)is None
    symbol_error=re.search(r"[!@#$%^&*();|''<>]", password)is None

    errors=[length_error,uppercase_error,digit_error,lowercase_error,symbol_error]
    score= 5-sum(errors)

    #Detailed feedback
    feedback=[]
    if length_error:
        feedback.append("Password should be atleast 8 characters")
    if uppercase_error:
        feedback.append("Include an uppercase")
    if lowercase_error:
        feedback.append("Include an lowercase")
    if digit_error:
        feedback.append("Include a digit")
    if symbol_error:
        feedback.append("Include a special character")

    if score <= 2:
        strength = "Pfft! You can do better"
    elif score ==3 or score==4:
        strength = "Hm, that looks fine"
    else:
        strength = "DAMN THAT'S STRONG"
    
    return strength, feedback

#Password Generator
def generate_pass(length=12):
    if length < 8:
        return "Password too short! Must be atleast 8 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#User Menu
def main():
    print("Password Tool🔐")
    print("1️. Check password strength 🕵️🔍")
    print("2️. Generate a strong password 🧑‍💻💪")
    choice=input("Choose an option (1 or 2): ")

    if choice=='1':
        print("\n Enter your password (input hidden): ")
        user_password=getpass.getpass()
        strength, feedback = check_password_generator(user_password)
        print(f"\n ☑️ Password strength: {strength}")
        if feedback:
            print("📝Suggestions to improve:")
            for tip in feedback:
                print("- "+tip)

    elif choice=='2':
        try:
             length = int(input("Enter desired password length (min 8): "))
             generated = generate_pass(length)
             print(f"\n Your strong password: {generated}")
        except ValueError:
         print("Please enter a valid number")
        
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run it!
if __name__ == "__main__":
    main()


