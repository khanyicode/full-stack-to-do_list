
from signup_.signup import *
from login_.login import *

def main():
    while True:
        choice = input("1. Signup\n2. Login\n3. Exit\nChoose an option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()