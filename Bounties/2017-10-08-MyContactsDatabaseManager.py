print("")
print("")
print ("Welcome to your Contacts Manager")

print ("This is a persistent database manager which will allow you to: ")

mycontacts = []
userchoice = 0

while userchoice != 4:
    print ("")
    print("1) add contacts")
    print("2) look up a contact")
    print("3) display all contacts")
    print("4) exit contacts manager")
    userchoice = eval(input())

    if userchoice == 1:
        print("")
        print ("adding a contact to your database")
        name = input("enter contact name: First Last (no commas)")
        email = input("enter contact email: ahernandezmendoza3345@student.phoenixunion.org")
        phone = input("enter contact phone number: 602-555-5555")
        mycontacts.append([name, email, phone])

    elif userchoice == 2:
        print("")
        print ("looking up contact")
        keyword = input("enter lookup term: ")
        for checker in mycontacts:
            if keyword in checker:
                print (checker)
            else:
                print ("that term does not exist in your contacts")
    elif userchoice == 3:
        print("")
        contactlistlength = len(mycontacts)
        if contactlistlength == 0:
            print ("looks like you have no contacts so far in your database")
        else:
            print("")
            print ("displaying all contacts")
            print (mycontacts)
    elif userchoice == 4:
        print("")
        print ("Exiting Contacts manager")
    else:
        print ("invalid response")
outfile = open("Data01", "a")
for checker in mycontacts:
    outfile.write(",".join(checker) + "\n")
    outfile.close()
