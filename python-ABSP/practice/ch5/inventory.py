#! python3
# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory[addedItems[i]] = inventory.get(addedItems[i], 0) + 1 
    return inventory

displayInventory(stuff)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 
stuff = addToInventory(stuff, dragonLoot)
print("\n" + " Dragon Slayer ".center(50, "*") + "\n")
displayInventory(stuff)
