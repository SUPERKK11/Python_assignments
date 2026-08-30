from User_resgistration import user_registration
class menu():
    def __init__(self):
        print("1. Registration")
        print("2. Login")
        print("3. exit")
        user_input=int(input("enter the number/choice: "))
        if user_input == 1:
            user_name=input("enter your name : ")
            user_email=input("enter your email: ")
            user_age=int(input("enter your age: "))
            user_password=input("enter the password: ")
            R1=user_registration(user_name,user_email,user_age,user_password)