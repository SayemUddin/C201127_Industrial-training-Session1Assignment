number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



age = int(input("Enter your age: "))
residency = input("Are you a resident (yes/no): ").lower()

if age >= 60 and residency == "yes":
    print("Congratulations! You are eligible for a senior citizen discount.")
else:
    print("Sorry, you are not eligible for a senior citizen discount.")




correct_username = "user123"
correct_password = "password123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome, " + username + ".")
else:
    print("Invalid username or password. Please try again.")





temperature = 30
weather = "sunny"

if weather == "sunny":
    if temperature > 25:
        print("It's a perfect beach day.")
    elif temperature > 15:
        print("It's a nice day for a walk.")
    else:
        print("It's sunny but too cold, stay home.")
elif weather == "snowy":
    if temperature < 0:
        print("Great day for skiing.")
    else:
        print("Snowy but not ideal for skiing, stay home.")
else:
    print("Not a sunny or snowy day, best to stay indoors.")
