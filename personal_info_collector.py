#Make a loop to continue asking the user until the user chooses to exit
#Prompt user to enter their Full name, address, contact number, email address and date of birth
#Store the input calues in a dictionary

import datetime


def validateInput(user):
    specialCharacters = ["-", ",", ".", "*", "'", "#"]
    output = ''
    #print(user)
    while True:
        try:
            match user:
                case "name":
                    output = input("Input your Full Name: ").upper()
                    for name in output:    
                        if not name.isalpha() and not name.isspace() and name not in specialCharacters:
                            raise ValueError("Wrong. Try again.")
                    break

                case "address":
                    output = input("Input your Address: ")
                    address = output.split()
                    requireAlpha = False
                    requireNumeric = False

                    for word in address:   
                        if not word.isnumeric() and not word.isalpha() and not word in specialCharacters:
                            for letter in word:
                                if not letter.isalpha() and not letter in specialCharacters:
                                    raise ValueError("Wrong. Try again.")
                        if word.isalpha():
                            requireAlpha = True
                        elif word.isnumeric():
                            requireNumeric = True

                    if not requireNumeric or not requireAlpha:
                        raise ValueError("Wrong. Try again.")
                          
                    break

                case "mobile_number":
                    output = input("Input your Mobile Number(+63): ")

                    if len(output) != 9 or not output.isnumeric():
                        raise ValueError("Wrong. Try again.")
                    break

                case "email":
                    output = input("Input your Email: ")
                    if ' ' in output or not '@' in output:
                        raise ValueError("Wrong. Try again.")
                    
                    tempList = output.split('@', 1)
                     
                    username = tempList[0] 
                    temp = tempList[1]

                    if '@' in temp:
                        raise ValueError("Wrong. Try again.") 
                        
                    tempList = temp.split('.', 1)

                    try:
                        mailServer = tempList[0]
                        domain = tempList[1]
                    except Exception:
                        raise ValueError("Wrong. Try again.")

                    for letter in mailServer:
                        if not letter.isalpha() and letter != '-':
                            raise ValueError("Wrong. Try again.")
                         
                    if not domain.isalpha():
                        raise ValueError("Wrong. Try again.") 
                    
                    break

                case "birth_date":
                    output = input("Input your date of birth(mm/dd/yyyy): ")
                    try:
                        dateInput = datetime.datetime.strptime(output, "%m/%d/%Y")
                    except Exception:
                        raise ValueError("Wrong. Try again.")
                    break

                case _:
                    pass

        except Exception as exception_:
            print(exception_)

    return output

def main():
    user_information = {}
    collector = []
    add_input = True

    user_input = True
    while user_input:
        name = validateInput("name")
        address = validateInput("address")
        number = validateInput("mobile_number")
        email = validateInput("email")
        birthday = validateInput("birth_date")

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
                choice = input("Do you wish to add another user information?(Yes?No): ").lower()
                if choice == "yes":
                    break
                elif choice == "no":
                    user_input = False
                    break
                else:
                    raise Exception("Invalid Input")
            except Exception:
                print(Exception)

    for index in range(len(collector)):
        print(collector)

main()
