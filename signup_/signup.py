import csv

def signup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                print("Username already exists. Please login.")
                return

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("User signed up successfully!")
