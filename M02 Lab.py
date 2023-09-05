#Name: Korey Hawkins
#Date: 8/31/23
#This program decides whether the student has made Dean's list
#or Honor Roll.

#Requesting the last name of user
lastname = input("Enter Student Last Name: ")

#Checking if the last name entered 'ZZZ' or not.
while lastname != "ZZZ":
    #Asking the user to enter student First name.
    firstname = input("Enter Student First Name")
    #Asking the user to enter Student GPA
    gpa = float(input("Enter Student GPA:  "))
    #Checking if the gpa is 3.5 or more
    #If it is then student has made the Dean's List
    if gpa >= 3.5:
        print("{} {} has made the Dean's List.".format(firstname, lastname))
    #Checking if the GPA is 3.25 or more
    #Then student has made Honor Roll
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstname, lastname))
    lastname = input ("\nEnter Student Last Name: ")
    #Repeating process until 'ZZZ' is entered