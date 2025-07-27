# global variables
is_user_registered = False
is_user_login = False
is_admin_login = False
selected_category = ""

def categoires():
    global selected_category
    categories_list = [
        "Home and Kitchen",
        "Health and Personal Care",
        "Electronics",
        "Toys and Games",
        "Beauty and Personal Care",
        "Clothing, Shoes and Jewelry",
        "Sports and Outdoors",
        "Pet Supplies"
    ]

    # loop to show the categories
    for i in range(len(categories_list)):
        print(f" {i + 1}: {categories_list[i]}")

    #loop that will keep asking user to select a category till a valid input is not received
    while True:
        try:
            user_choice = int(input("Select a Category form the List: "))
            if(user_choice < 1 or user_choice > len(categories_list)):
                print("Invalid Option Selected ..... Try Again!")
            else:
                selected_category = categories_list[user_choice - 1]
                break
        except ValueError:
            print("Only Integers are Accepted.... Try Again")

    # now showing user the category it selected
    view_category(selected_category)

# method that shows selected category of the user
def view_category(category_name):
    print("===============================================")
    print(f"|            {category_name}                 |")
    print("===============================================")

    file_name = category_name + ".txt"

    # calling search category function to allow user to search for the product
    search_products(file_name)

# Search Method to look for the Product
def search_products(filename):
    #prompting the user to search for the product
    keyword = input("Enter the Product Name to Search: ").strip().lower()

    # Variable for checking if the Product Record Exists
    found = False
    try:
        # Opening the file in read mode to read data from the file
        with open(filename, "r") as file:
            print(f"Getting Results for {keyword} .......")
            for line in file:
                #checking is the searched keyword is in the list
                if keyword in line.lower():
                    # Storing data of line in a list
                    parts = line.strip().split('|')

                    #Storing the value at  index 0  in product_name variable
                    product_name = parts[0].strip()
                    # Storing the value at  index 1 in product_name variable
                    rating =  parts[1].strip()
                    # Storing the value at  index 2  in product_name variable
                    monthly_sales = parts[2].strip()
                    print("Found:", product_name)
                    found = True

                    # After product is found then showing next menu
                    print("\nWhat would you like to see?")
                    print("1. Rating")
                    print("2. Monthly Sales")
                    print("3. Recommendation (based on both)\n")


                    while True:
                        try:
                            choice = input("Enter your choice (1-3): ").strip()
                            if(int(choice) < 1 or int(choice) > 3):
                                print("Invalid Input ..... Try Again")
                            else:
                                break
                        except ValueError:
                            print("Only Integres are Accepted.... Try Again")

                    #checking what user selected from the sub menu
                    if choice == "1":
                        print("Ratings :", rating)
                    elif choice == "2":
                        print("Monthly Sales: ", monthly_sales)
                    else:
                        print("Ratings : ", rating)
                        print("Monthly Sales : ", monthly_sales)

                        #Checking product progress & then based on that giving feed back to the user
                        if(float(rating) >= 4.5 and int(monthly_sales) >= 1500 ):
                            print("Highly Recommended Product")
                            print("This is a Winning Product!")

                        elif(float(rating) >= 4.0 and int(monthly_sales) >= 1000):
                            print("A Good Product but You can Also Explore More Options")
                        else:
                            print(" This Product is Not Recommended!")

                    break  # Stop after first match
        # not
        if not found:
            print("No Record Exists!")
    except FileNotFoundError:
        print("File Does Not Exist!")


    input("Press Enter to go Next: ")

    # showing choice menu to user to decidde where to go
    choice_menu()

    user_choice = input("Your Choice: ")
    if (user_choice[0].upper() == 'Y'):
        view_category(selected_category)
    elif (user_choice[0].upper() == 'A'):
        categoires()
    else:
        print("**********  THANKS FOR USING OUR TOOL   **********")
        print("Logging Out......")
        exit()

def edit_category():
    admin_selection = input("Enter the Name of the Category to Edit: ")
    category = admin_selection
    while True:
        print("Write data in Format: Product | Rating | Monthly Sales")

        # Opening file in append mode to add data to the existing file
        with open(category+".txt","a") as file:
            #taking input from admin to store in the file
            data = input()
            # writing data to the file
            file.write("\n" + data )

            print("Data Written to the ", category," file Successfully")

        input("Press Enter to go to Next Step: ")

        # Getting admin choice after writing to the file
        admin_choice = input("Do You Want to add More Items in the Category(Y/N)")

        #Checking Admin's Choice
        if(admin_choice[0].upper() !='Y'):
            print("**********  THANKS FOR USING OUR TOOL   **********")
            print("Logging Out......")
            break


#method for showing menu for user choice
def choice_menu():
    print("********       USER CHOICE      *********")
    print("| =>   SEARCH MORE  ->   (PRESS 'Y')    |")
    print("| =>   MAIN MENU    ->   (PRESS 'A')    |")
    print("| =>   EXIT ->     (PRESS ANY OTHER)    |")
    print("-----------------------------------------")

#method for checking the passwrod strength
def is_strong(password):
    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False
    has_letter = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isalpha():
            has_letter = True
        if char.isupper():
            has_upper = True
        if not char.isalnum():  # special characters
            has_special = True

    return has_digit and has_letter and has_upper and has_special

# methods that checks for duplicate names
def duplicate_user(username):
    try:
        with open("registrations.txt", "r", encoding="utf-8") as file:
            for line in file:
                details = line.strip().split("|")
                if username == details[0]:
                    return True
    except FileNotFoundError:
        return False
    return False

def register_user():
    global is_user_registered
    while True:
        username = input("Enter Your Name: ")

        #Checking if the name is already taken
        if duplicate_user(username):
            print("User Name Already Taken")
            print("Kindly Use Another User-Name")
            continue

        password = input("Enter a strong Password: ")

        if not is_strong(password):
            print("Weak Password! .... Kindly Enter a Strong Password")
        else:
            print("***** Registered Successfully *******")
            is_user_registered = True

            # After the Registration is successfull the writing registration records in registration file
            try:
                with open("registrations.txt", "a") as file:
                    file.write(f"{username}|{password}\n")

            except FileNotFoundError:
                print("File Does Not Exist!")
            except IOError:
                print("Error While Writing to the file")
            break

# User Login Method
def login_user():
    global is_user_login
    is_login = False
    attempts = 3
    while  not is_login:
        user_name = input("Enter User-Name: ")
        password = input("Enter Your Password: ")

        #opening file to read data from
        try:
            with open("registrations.txt","r") as file:
                for line in file:
                    details = line.strip().split("|")
                #checking if the login details matched
                    if(user_name == details[0] and password == details[1]):
                        print("******** Login Successfully ********")
                        is_user_login = True
                        is_login = True
                if(not is_login):
                    attempts -= 1
                    if(attempts == 0):
                        break
                    print(("Attempts" if attempts > 1 else "Attempt" )," Left: ",attempts)
        except FileNotFoundError:
            print("File Does Not Exists!")


# Admin Login Method
def login_admin():
    global is_admin_login
    attempts = 3
    name_admin = "Masab"
    pass_admin = "Masab@ICTProject"

    print("==================================================");
    print("|     << Welcome to Admin Login Section >>       |");
    print("==================================================");

    while True:
        admin_name = input("Enter Admin Name: ")
        admin_pass = input("Enter Admin Password: ")

        #checking if login details matched
        if(admin_name == name_admin and  admin_pass == pass_admin):
            is_admin_login = True

        if(is_admin_login):
            print("*****  ADMIN LOGIN SUCCESSFULLY  *****")
            break
        else:
            attempts -= 1
            print("Invalid Credentials .... You have ", attempts," attempts left!")
         #Checking if all the attempts used
        if(attempts == 0 ):
            print("*****  ADMIN LOGIN FAILED  *****")
            print("You have wasted all your Attempts!")
            print("Logging Out.....")
            exit()

def show_user_login_menu():

    print("=========================================")
    print("|    1: REGISTER                         |")
    print("|    2: LOGIN                            |")
    print("=========================================")

    #loop that will keep prompting the user to enter valid option
    while True:
        try:
            user_option = int(input("Select an Option from MENU: "))
            if (user_option < 1 or user_option > 2):
                print("Invald Input....Kindly Select a valid input")
            else:
                break
        # Exception handled if input data is other than integer
        except ValueError:
            print("Only Integers are allowed .... Try Again")

    #chceking what user selected from the menu
    if(user_option == 1):
        register_user()
        #after successfull registration prompting user to now login
        if(is_user_registered):
            print("Kindly Now Enter Your Details to Login")
            login_user()
    else:
        login_user()

     # if user is successfully login then showing next menu to the user
    if(is_user_login):
        categoires()

def show_admin_menu():
    print("==================================================");
    print("|          << Welcome to Admin MENU >>            |");
    print("==================================================");
    print("|  1: Edit Category                               |")
    print("|  2: Exit                                        |")
    print("==================================================");

    while True:
        try:
            admin_option = int(input("Select an Option from MENU: "))
            # varifying that whether user selected valid option if not prompt again
            if (admin_option < 1 or admin_option > 2):
                print("Invalid Input....Kindly Select a valid input")
            else:
                break
        except ValueError:
            print("Only Integers are allowed .... Try Again")

    #Checking the Admin's choice
    if(admin_option == 1 ):
        edit_category()
    else:
        exit()



# START OF THE MAIN LOGIC
print("========================================")
print("|        Product Hunting Tool           |")
print("========================================")
print("|            LOGIN AS:                  |")
print("|    1: USER                            |")
print("|    2: ADMIN                           |")
print("=========================================")

while True:
    try:
        user_option = int(input("Select an Option from MENU: "))
        # varifying that whether user selected valid option if not prompt again
        if(user_option < 1 or user_option > 2):
            print("Invald Input....Kindly Select a valid input")
        else:
            break
    except ValueError:
        print("Only Integers are allowed .... Try Again")
# checking what the user selected from the menu
if(user_option == 1):
    show_user_login_menu()
else:
    login_admin()

#showing Admin menu to Admin if login Successfully
if(is_admin_login):
    show_admin_menu()