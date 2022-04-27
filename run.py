#!/usr/bin/env python3.8
import pyperclip 
from ast import If
from credentials import Credentials,User



def create_user(username, password):
    '''
    creates a new user
    '''
    new_user = User(username, password)
    return new_user
def save_user(user):
    '''
    method to save a newly created user
    '''
    user.save_user()
    
def delete_user(user):
    '''
    method to delete a user
    '''
    user.delete_user()        
def create_credentials(sitename,username, password):
    '''
    method to create new credential
    '''
    new_credentials = Credentials(sitename,username, password)
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
    
def search_credentials(name):
    '''
    function to find credentials by account name
    '''
    return Credentials.search_credentials(name)

def display_credentials():
    '''
    functions that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def authenticate(name,password):
    '''
    method to check if a uer already exists in the users list
    '''
    return Credentials.aunthenticate(name,password)

def main():
    print("Hello There, Welcome to Password Locker...")
    print("Please find navigation around the locker below")
    print("\n")    
    print("\n")
    
    while True:
        print("lg.....to login to your account")
        print("sn.....to Sign-Up and create account.")
        print("ex.....to exit")
        short_code = input("Enter your input:").lower().strip()
        
        if short_code == "lg":
                        print("Enter your login credentials")
                        username = input("username:")
                        password = input("password:")
                        
                        user = authenticate(username,password)
                        
                        
                        if user == username:
                            print(f"hi, {username}, please select usercode to navigate")  
                            
                            while user == True:
                                print("Choose an option to continue")
                                print("nc....to create new credentials")
                                print("dc....to display credentials")
                                print("fc....to find credentials")
                                print("da....to delete account credentials")
                                print("uc....to update credentials")
                                print("cc....to copy credentials ")
                                print("ex....to exit password locker")
                                print("\n")                       
                                                      
                            
                                short_code = input("shortcode:").lower().strip()
                                print("\n")
                                
                                if short_code == "nc":
                                    print("Enter new account credentials details")
                                    site_name = input("sitename:").strip()
                                    user_name = input("username:").strip()
                                    
                                    while True:
                                        
                                        print("tp....to type in password")
                                        print("gp....for generated password")
                                        
                                        choice = input("choice:").lower().strip()                                        
                                        
                                        print("\n")
                                        if choice == "tp":
                                            print("enter login")
                                            password = input("enter desired password:")
                                            break
                                        elif choice == "gp":
                                            print("enter desired password length, should be between 8 and 12 characters")
                                            len= int(input("password length:"))
                                            
                                            if len > 12 or len < 8:
                                                print("enter correct password length please")
                                                
                                            else:
                                                password = Credentials.generate_password(len)
                                                print(f"your password is {password}")
                                                break
                                        else:
                                            print("error! please choose correct short codes.")
                                    
                                    password = password.strip()
                                    
                                    if site_name == "" or user_name == "" or password == "":
                                        print("enter correct details to create account!")
                                    else:
                                        save_credentials(create_credentials(site_name,user_name,password))
                                     
                                    
                                elif short_code == "dc":
                                    if display_credentials():
                                        
                                        for credentials in display_credentials():
                                            print(f"{credentials.sitename} \n {credentials.username} \n {credentials.password} ")
                                            
                                    else:
                                        print("You do not have any save credentials!")
                                        
                                elif short_code == "cc":
                                    print("Please enter account name whose credentials is to be copied.")
                                    
                                    account_name = input("account name:").strip()
                                    if search_credentials(account_name):
                                        pyperclip.copy(account.password)
                                        print("password copied ")
                                    else:
                                        print("account not found")
                                  
                                    
                                    
                                    
                                elif short_code == "da":
                                    print("Enter the account name you want to delete")
                                    account_name = input("account name:").strip()
                                    
                                    if search_credentials(account_name):
                                        account = search_credentials(account_name)
                                        delete_credentials(account)
                                        if display_credentials():
                                            for credential in display_credentials():
                                                print("your remaining accounts are:")
                                                print(f"{credential.sitename} \n {credential.username} \n {credential.password}")
                                        
                                        else:
                                            print("no remaining accounts")
                                            
                                    else:
                                        print("account not found")
                                            
                                    
                                    
                                    
                                elif short_code == "fc":
                                    print("enter account you want to find")
                                    print("Y/N")
                                    account_name = input("account name:").strip()
                                    if search_credentials(account_name):
                                        account = search_credentials(account_name)
                                        print("account \n username \n password")
                                        print(f"{account.sitename} \n {account.username} \n {account.password}")
                                    else:
                                        print("account not found")
                                elif short_code == "ex":
                                        print(f"thank you {username} for using password locker ")
                                        break
                                    
                                else:
                                    print("please chose correct short codes.")
                                        
                                        
        elif short_code == "sn":
            print("Enter Your details")
            username = input("Enter username:").strip()
            print("\n")        
        
        
            while True:
                print("Please choose the options below: \n tp.....to type in your password \n gp.....to be generated a password")
                
                choice = input("choice:").lower().strip()
               
                if choice == "tp":
                   password = input("Enter password")
                   break
                elif choice == "gp":
                    print("enter password length, it should be between 8-12 characters")
                    len = int(input("length:"))
                    
                    if len > 12 or len < 8:
                        print("please choose correct length!")
                        
                    else:
                        password = Credentials.generate_password(len)
                        print(f"your password is {password}")
                        break
                else:
                    print("please choose valid short codes")
                    
            password = password.strip()
            if password == "" or username == "" :
                print("failed! account fields cannot be empty!")
                
            else:
                save_user(create_user(username,password))
                print("account created successfully")
                print(f" use username:{username} password:{password} to login")
                
                
        elif short_code == "ex":
            print("Thank you for using password locker!")
            
            
        else:
            print("please chose the short codes provided")
                        
            

if __name__ == '__main__':
    main()  
                    
        
                                    
                                
                                
                                          
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
if __name__ == "__main__":
    main()
                            
        

        
        
    