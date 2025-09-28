import random
import string

def generate_password():
    print("🔐 Password Generator 🔐")
    
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("⚠️ Password should be at least 4 characters long.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure password includes at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    # Join to make final password
    final_password = ''.join(password)
    print(f"\n🔑 Generated Password: {final_password}")

# Run the generator
generate_password()
