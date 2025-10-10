def create_inventory(items):
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
                if inventory[item] < 0:
                    inventory[item] = 0
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
        return inventory
    return inventory


def list_inventory(inventory):
    listed = []
    for item, quantity in inventory.items():
        if quantity > 0:
            listed.append((item, quantity))
    return listed