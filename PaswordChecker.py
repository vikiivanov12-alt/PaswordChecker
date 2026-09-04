import re

def check_password_strength(password):
    score = 0

    # Дължина
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Главни + малки букви
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1

    # Цифри
    if re.search(r"\d", password):
        score += 1

    # Специални символи
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>/?\\|]", password):
        score += 1

    return min(score, 5)

password = input("Enter your password: ")

score = check_password_strength(password)

strength_levels = {
    0: "Very Weak",
    1: "Weak",
    2: "Medium",
    3: "Good",
    4: "Very Good",
    5: "Excellent",
}

print(f"Password strength: {strength_levels[score]}")
print(f"Score: {score}/5 ({score/5:.2f})")
