#Make a loop to continue asking the user until the user chooses to exit
#Prompt user to enter their Full name, address, contact number, email address and date of birth
#Store the input calues in a dictionary

user_information = {}
collector = []
user_input = True
add_input = True


while user_input:
    name = input("Input your fullname: ")
    address = input("Input your address: ")
    number = input("Input your cellphone number(+63): ")
    email = input("Input your email address: ")
    birthday = input("Input your date of birth(mm/dd/yyyy): ")

    user_information = {
        "Full name": name,
        "Address": address,
        "Cellphone number": number,
        "Email address": email,
        "Birth date": birthday 
    }

    collector.append(user_information)
    
    while add_input:
        try:
            choice = input("Do you wish to add another user information?(Yes?No): ")
            if choice == "yes":
                break
            elif choice == "no":
                user_input = False
                break
            else:
                raise Exception("Invalid Input")
        except Exception:
            print(Exception)

print(collector)