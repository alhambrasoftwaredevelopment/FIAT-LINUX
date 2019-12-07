openthis = input("print the name of the file you want to open  ")
emptylist = []
with open(openthis + '.txt', 'r') as f:
    datapoint = f.read()
    emptylist.append(datapoint)
    print(datapoint)

print (f.name)
print (f.mode)
print (emptylist)
