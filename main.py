import random

def check_eligibility():
    print("=== Intramurals Eligibility Checker ===\n")

    registered = input("Are you registered online? (yes/no): ").lower()
    medical = input("Do you have a medical clearance? (yes/no): ").lower()
    
    grade = int(input("Enter your grade level (7-12): "))
    section = input("Enter your section: ")

    teams = [
        "Blue Bears",
        "Red Bulldogs",
        "Yellow Tigers",
        "Green Hornets"
    ]

    if registered != "yes":
        print("\n❌ Not Eligible")
        print("➡ Please register online for the Intramurals.")
        return

    if medical != "yes":
        print("\n❌ Not Eligible")
        print("➡ Please secure a medical clearance.")
        return

    if grade < 7 or grade > 10:
        print("\n❌ Not Eligible")
        print("➡ Only students from Grades 7–10 are allowed to join.")
        return

    team = random.choice(teams)
    print("\n🎉 Congratulations!")
    print("You are ELIGIBLE to join the Intramurals.")
    print(f"🏆 Assigned Team: {team}")
    print(f"📚 Grade & Section: Grade {grade} - {section}")

check_eligibility()
