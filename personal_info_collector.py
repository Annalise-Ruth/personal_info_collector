#Make a loop to continue asking the user until the user chooses to exit
#Prompt user to enter their Full name, address, contact number, email address and date of birth
#Store the input calues in a dictionary


while True:
    input("Input your name: ")
    input("Input your address: ")
    input("Input your cellphone number(+63): ")
    input("Input your email address: ")
    input("Input your date of birth(mm/dd/yyyy): ")
    

    add_input = input("Do you wish to continue(Yes?No): ")
    if add_input == "Yes" or add_input == "yes":
      pass
    elif add_input == "No" or add_input == "no":
       break

