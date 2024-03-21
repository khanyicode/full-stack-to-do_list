

import csv

def signup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("User signed up successfully!")
