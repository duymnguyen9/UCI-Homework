answer = "no"
account = 1000
print("Welcome to your personal bank!")
print("Please Enter your password:")
password = input("> ")
while password.lower() != "password":
    print("Wrong Password! Please Try Again!")
    password = input("> ")
while answer.lower() != "yes":
    print("Please Enter Your Options:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit Program")
    choice = int(input("Choice:  "))
    if choice == 1:
        print("Your outstanding balance is $" + str(account))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif choice == 2:
        account = account + int(input("Deposit Amount: "))
        print("Your outstanding balance is $" + str(account))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif choice == 3:
        print("Withdraw Amount: ")
        print("Your outstanding balance is $" + str(account))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif choice == 4:
        print("Thank you for banking with us")
        answer = "yes"
    else:
        print("Please Enter a valid choice!")
    