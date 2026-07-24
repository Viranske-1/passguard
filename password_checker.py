import math

password = input("Enter your password: ")

special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

score = 0

# Check password properties once
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in special_characters for char in password)

# Check password length
if len(password) >= 8:
    print("✅ Password length is good.")
    score += 20
else:
    print("❌ Password is too short.")

# Check uppercase letters
if has_upper:
    print("✅ Contains uppercase letter.")
    score += 20
else:
    print("❌ No uppercase letter found.")

# Check lowercase letters
if has_lower:
    print("✅ Contains lowercase letter.")
    score += 20
else:
    print("❌ No lowercase letter found.")

# Check numbers
if has_digit:
    print("✅ Contains number.")
    score += 20
else:
    print("❌ No number found.")

# Check special characters
if has_special:
    print("✅ Contains special character.")
    score += 20
else:
    print("❌ No special character found.")

# Display security score
print(f"\nSecurity Score: {score}/100")

# Display password strength
if score < 40:
    print("🔴 Password Strength: Weak")
elif score < 80:
    print("🟡 Password Strength: Medium")
else:
    print("🟢 Password Strength: Strong")

# Calculate character set size for entropy
charset_size = 0

if has_lower:
    charset_size += 26

if has_upper:
    charset_size += 26

if has_digit:
    charset_size += 10

if has_special:
    charset_size += 32

# Calculate entropy
if charset_size > 0:
    entropy = len(password) * math.log2(charset_size)
else:
    entropy = 0

print(f"Estimated Entropy: {entropy:.2f} bits")
