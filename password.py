# password = 'data'

# for attempt in range(1, 5):
#     if (attempt == 4):
#         print("One more attempt left")

#     user_input = input("Enter your password: ")

#     if user_input == password:
#         print("Welcome to the system")
#         break
#     else:
#         print("Incorrect password")

# send otp

OTP = "1234"
name = ""
for attempt in range(1, 4):
    if (attempt == 3):
        print("One more attempt left")

    user_otp = input("Enter the OTP: ")
    if user_otp != OTP:
        print("Try again!")
        continue
    else:
        name = input("Enter your name: ")
        print(f"Welcome {name} ji")
        break
