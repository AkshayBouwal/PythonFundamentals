newPass = input("Enter new password: ")
confirmPass = input("Re - enter new password: ")

if newPass == confirmPass:
    print("Congratulations, you are logged in successfully!")
elif newPass.lower() == confirmPass.lower():
    print("Mismatch in cases please check your password")
else:
    print("Passwords do not match")