# -----------------------------
# The Pickpoct - Jones Example
# -----------------------------
innocentVillager = ['pear', 'harp', 'wallet', 'pet rat', 'football card',
                    'picture of donkey']  # creates Innocent Villager list
pickpocket = []  # creates empty pickpocket list
print(innocentVillager)  # prints both lists out
print(pickpocket)

while True:
    x = int(input(
        'Give me the index place of item you want me to steal?~'))  # asks user input and converts it into an integer
    pickpocket.append(innocentVillager[x])  # appends the index given by user to pickpocket list
    del innocentVillager[x]  # deletes the item in innocent villager list

    print(innocentVillager)  # prints both lists out
    print(pickpocket)
    print('')
    if len(innocentVillager) == 0:  # little extra when the length of innocent villager list is 0.
        print("RIP Villager. :'( ")
        break

InnoVill = ['phone', 'wallet', 'gum', 'headphones', 'glasses']
PickpInven = []
while True:
    print('Innocent Villager', InnoVill)
    print()
    print('PickPocket Inventory', PickpInven)
    print()
    steal = input('What do you want me to steal?-> ')

    if steal in InnoVill:
        InnoVill.remove(steal)
        PickpInven.append(steal)
        print(InnoVill)
        print(PickpInven)
    else:
        print('That item does not exist')

villager = ['pear', 'harp', 'wallet', 'pet rat', 'football card', 'picture of donkey', 'box of wheaties']
inventory = []

print("")
print("this is what the villager has ")
print(villager)

while True:
    print("")
    steal = int(input("give me the index of what you want me to steal: "))
    print("")
    got = villager.pop(steal)
    inventory.append(got)
    print("this is what the villager has left ")
    print(villager)
    print("")
    print("this is what the pickpocket has stolen ")
    print(inventory)

# the pickpocket
