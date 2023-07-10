#!/usr/bin/env python3
"""
Khaled Aldasouki
19-4-2023
"""

import os
from platform import platform 
import time


"""Helper function used to clear the terminal"""
def clear():
    os.system("clear")

"""
Function used to create a shortcut to a file or directory in the users home directory
asks the user for the file/directory absolute path and for the name of the shortcut
"""
def add_link():

    #get the users home directory
    home = os.path.expanduser("~")

    filepath = input("Enter the full path to the file or directory: ")
    filename = input("Enter the name of the shortcut you want to create: ")

    #check that the file or directory exists
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist")

    #make sure the shortcut we're trying to create doesn't exist already
    elif os.path.exists(home + '/' + filename):
        print(f"File {home + '/' + filename} already exists")
        
    else:
        #create the shortcut and inform the user
        os.symlink(filepath,home+"/"+filename)
        print(f"symlink created between {filepath} and {filename}")
    
    

"""
function used to remove a shortcut from the home directory
asks the user for the shortcut name
"""
def remove_link(): 
    filename = input("Enter the name of the shortcut file you want to delete: ")  

    #get the users home directory
    home = os.path.expanduser("~")
    
    #try to remove the shortcut, if an error is raised inform the user that the shortcut doesn't exist
    try:
        os.readlink(home+"/"+filename)
        os.unlink(home+"/"+filename)
        print(f"removed link for {filename}")

    #if the file we're trying to unlink doesn't exist
    except FileNotFoundError:
        print(f"Error: {home + '/' + filename} does not exist")

    #if the given file is not a shortcut (shouldn't get deleted)
    except OSError:
        print(f"Error: {home + '/' + filename} is not a shortcut")

"""
Function used to report shortcuts in the user's home directory
"""
def report_links():
    #get the users home directory
    home = os.path.expanduser("~")
    print("Shortcut         Destination")
    os.system("ls -la " + home + """ | grep ^l | awk {'print $9"   "$10"   "$11'}""")

"""
Main function called when the program is run 
"""
def main():
    clear()
    if platform == "win32":
        print("This tool is made for Linux and cannot be used on Windows.")
        time.sleep(5)
    #repeat until the user chooses to quit the program
    else:
        while True:

                #prompt the user for an option
                print("\t **************************************************\n \
                *****************Shortcut Creator*****************\n \
                **************************************************")
                print("Choose an option:\n \
                    1. Add a shortcut to your home directory \n \
                    2. Remove a shortcut from your home directory \n \
                    3. Report all shortcuts in the home directory\n   ")
                option = input("Please pick an option (1-3) or type 'Q/q' to quit: ")

                clear()
                #call the appropriate function depending on the chosen option
                if option == '1':
                    add_link()
                elif option == '2':
                    remove_link()
                elif option == '3':
                    report_links()
                    time.sleep(2)
                elif option.upper() == 'Q' or option.upper() == "QUIT":
                    print("Quitting...")
                    time.sleep(1)
                    break
                #if the user doesn't enter a valid option, inform them 
                else:
                    print("Invalid option. Please try again.")

                time.sleep(3)
                clear()

if __name__ == "__main__":
    main()





