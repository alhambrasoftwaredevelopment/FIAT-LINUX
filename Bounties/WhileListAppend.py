numcounter = 0
list = []
print("print 'leave' if you would like to exit")
while 1 != 0:
    nameadd = input("give me a name   ")
    numcounter = numcounter + 1
    list.append(nameadd)
    print("")
    print ("round:", numcounter, "   '", nameadd + " ' has been added to the list")
    print("The complete list is now:" + str(list))
    print("the length of the list is " + str(len(list)))
    print("")
    if nameadd == "leave":
        break
