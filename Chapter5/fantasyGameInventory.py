import pprint, copy

def displayInventory(inventory):
    print('Inventory:')
    sum = 0
    for k, v in inventory.items():
        print(v, k)
        sum += v
    print('Total number of items:', sum)

def addToInventory(inventory, addedItems):
    newInv = copy.copy(inventory)
    for item in addedItems:
        newInv[item] = newInv.get(item, 0) + 1
    return newInv

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)