#!/usr/bin/env python3.8
import pyperclip, random, string
from credentials import Credentials
from userInfo import User

def create_user(username, password):
    '''
    creates a new user
    '''
    new_user = User(username, password)
    return new_user


def generate_login():
    '''
    function that generate a login
    '''
    phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase
    while True:
        try:
            length = int(input("Enter desired length of login "))
            login = random.sample(phrase,length)
            
        except ValueError:
            print("Enter a valid number please!")
            continue
        else:
            login = ("".join(login))
            return login
        
def create_credentials(accountname, login):
    '''
    function to create new credential
    '''
    new_credentials = Credentials(accountname, login)
    return new_credentials
       

def save_credentials(credentials):
    '''
    function to save credentials
    '''   
    credentials.save_credentials()
    
def delete_credentials(credentials):
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()
    
def find_credentials(names):
    '''
    function to find credentials by account name
    '''
    return Credentials.find_by_name(names)

def display_credentials():
    '''
    functions that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello There, Welcome to Password Locker...")
    print("Please find navigation around the locker below")
    print("\n")
    print("lg.....to login to your account")
    print("sn.....to Sign-Up and create account.")
    short_code = input().lower()
    print("\n")
    if short_code == "sn":
                        print("Enter UserName")
                        username = input()
                        
                        print("Enter Password")
                        password = input()
                        
                        print("Confirm Password")
                        confirm_password = input()
                        
                        while confirm_password != password:
                            print("Try again! passwords does not match!")
                            print("Enter password")
                            password = input()
                            print("Confirm Password")
                            confirm_password = input()
                            
                        else:
                            print(f"Hi {username}, Your account has been successfully created!")
                            print("\n")
                            print("Login to your account")
                            print("Enter your Username")
                            username_input = input()
                            print("Entre your Password")
                            password_input = input()
                            
                        while username_input != username or password_input != password:
                            print("Invalid username or password")
                            
                            print("Enter your Username")
                            username_input = input()
                            print("Enter your Password")
                            password_input = input()
                            
                        else:
                            print(f"Hi {username}, Welcome to Password LOcker")
                            while True:
                                print("Choose an option to continue")
                                print("nc....to create new credentials")
                                print("dc....to display credentials")
                                print("cc....to copy credentials to clipboard")
                                print("da....to delete account credentias")
                                print("ex....to exit password locker")
                              
                                short_code = input().lower()
                                if short_code == "nc":
                                    print("Enter account name")
                                    account_name = input()
                                    while True:
                                        print("Choose login with the short codes below")
                                        print("el....to enter login")
                                        print("gl....for generated login")
                                        print("ex....to exit")
                                        user_key = input().lower() 
                                        print("\n")
                                        if user_key == "el":
                                            print("enter login")
                                            login_input = input()
                                        elif user_key == "gl":
                                           login_input = generate_login()
                                           break
                                        elif user_key == "ex":
                                           break
                                        else:
                                          print("Check on your input")
                                     #create new credential and saves it     
                                    save_credentials(create_credentials(account_name,login_input))
                                    print(f"Your credentials for {account_name} has been created, the login is {login_input}")
                                    
                                elif short_code == "dc":
                                    if display_credentials():
                                        print("Your credentials are: \n")
                                        for credentials in display_credentials:
                                            print(f"{credentials.accountname} - {credentials.login}")
                                            
                                    else:
                                        print("You do not have any save credentials!")
                                        
                                elif short_code == "cc":
                                    print("Please enter account name whose credentials is to be copied.")
                                    accountname = input()
                                    findAccount = find_credentials(account_name)
                                    pyperclip.copy(findAccount.accountname)
                                    
                                    
                                elif short_code == "da":
                                    print("Enter the account name you want to delete")
                                    accountname = input()
                                    account = find_credentials(accountname)
                                    delete_credentials(account)
                                    
                                elif short_code == "ex":
                                    print("Are you sure you want to exit?")
                                    print("Y/N")
                                    userAnswer = input().upper()
                                    if userAnswer == "Y":
                                        print("Thank you for using password locker")
                                        break
                                    elif userAnswer == "N":
                                        print("choose any option to continue \n 'nc' to create new credential,\n 'dc' to display credentials,\n 'cc' to copy credentials,\n 'ex' to exit the application")
                                        short_code = input().lower()
                                        
                                        
    elif short_code == "lg":
        print("Enter Username")
        user_username = input()
        print("Enter password")
        user_password = input()
        
        while user_username != "Stacy" or user_password != "Stacy2009":
            print("Invalid username or password")
            
        else:
            print("Hi welcome back! ")
            while True:
                print("Choose a navigation option")
                print("nc....to create new credentials")
                print("dc....to display credentials")
                print("cc....to copy credentials")
                print("da....to delete account credentials")
                print("ex....to exit the application")
                short_code = input().lower()
                
                if short_code == "nc":
                    print("Enter account name")
                    account_name = input()
                    while True:
                        print("Choose login with the short codes below")
                        print("el => to enter login")
                        print("gl => for generated login")
                        print("ex => to exit")
                        user_key = input().lower() 
                        print("\n")
                        if user_key == "el":
                            print("enter login")
                            login_input = input()
                        elif user_key == "gl":
                            login_input = generate_login()
                            break
                        elif user_key == "ex":
                            break
                        else:
                            print("Check on your input")
                                     #create new credential and saves it     
                    save_credentials(create_credentials(account_name,login_input))
                    print(f"Your credentials for {account_name} has been created, the login is {login_input}")
                    
                elif short_code == "dc":
                    if display_credentials():
                        print("Your credentials are: \n")
                        for credentials in display_credentials:
                            print(f"{credentials.accountname} - {credentials.login}")
                                            
                    else:
                        print("You do not have any save credentials!")
                                        
                elif short_code == "cc":
                    print("Please enter account name whose credentials is to be copied.")
                    accountname = input()
                    findAccount = find_credentials(account_name)
                    pyperclip.copy(findAccount.accountname)
                                    
                                    
                elif short_code == "da":
                    print("Enter the account name you want to delete")
                    accountname = input()
                    account = find_credentials(accountname)
                    delete_credentials(account)
                                    
                elif short_code == "ex":
                    print("Are you sure you want to exit?")
                    print("Y/N")
                    userAnswer = input().upper()
                    if userAnswer == "Y":
                        print("Thank you for using password locker")
                        break
                    elif userAnswer == "N":
                        print("choose any option to continue \n 'nc' to create new credential,\n 'dc' to display credentials,\n 'cc' to copy credentials,\n 'ex' to exit the application")
                        short_code = input().lower()
                        
                    else:
                        print("Please select a valid option")
                        
                        
    else:
        print("Please choose a valid short code!")
        
if __name__ == "__main__":
    main()
            
        
                                        
                    
        
                                    
                                
                                
                                          
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
if __name__ == "__main__":
    main()
                            
        

        
        
    