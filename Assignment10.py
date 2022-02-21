#Bethany Mehring
#Assignment 10

import os # import operating system

def main(): #defing the main function
    directory= input('What directory are we saving to? ') #getting directory name from user
    if os.path.isdir(directory): #if directory is a valid directory on the os
    
        fileName= input('What is the file name? ') #getting user input
        fileName+='.csv' #adding file type

        name= input('What is your name? ') #getting user input
        address= input('What is your address? ') #getting user input
        phone= input('What phone number can we reach you at? ') #getting user input

        path=os.path.join(directory, fileName) #joining together values to create path

        with open(path,'w') as file_object: #opening file with the purpose of writing into it
                userInfo=(name+','+address+','+phone) #assigning user information to a value
                file_object.write(userInfo) # writing user information to the file
        
        with open(path) as file_object:
                print(file_object.read()) #reading file
        

        again=input('Would you like to enter a new file in another directory? (Y for yes anything else to escape) ') #getting user input
        if again== 'Y': # if statement to go again
            file_object.close() #close the open file
            main()# go back to the beginning of main
        else:
            file_object.close() #close open file
            exit()

    else: #if directory is not valid, prompting user with info and asking starting main again
        print("Not a valid directory, please try again.")
        main()
main() 