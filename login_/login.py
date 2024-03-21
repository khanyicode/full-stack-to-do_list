

import csv

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful!")
                return

        print("Invalid username or password. Please try again.")
        
