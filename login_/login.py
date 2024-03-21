
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

        print("Invalid username or password.")
        
        reset_choice = input("Would you like to reset your password? (y/n): ")
        if reset_choice.lower() == 'y':
            reset_password(username)
            
            
            
def reset_password(username):
    new_password = input("Enter a new password: ")

    rows = []
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                rows.append([username, new_password])
            else:
                rows.append(row)

    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Password reset successfully.")
        
        
 
        
