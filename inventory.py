stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		print(v, k)
		item_total += v
	print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
	test = {i:dragonLoot.count(i) for i in dragonLoot}
	for i in addedItems:
		for k in inventory.keys():
			if i == k:
				inventory[k] += 1
	test.update(inventory)
	return test

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin','gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)