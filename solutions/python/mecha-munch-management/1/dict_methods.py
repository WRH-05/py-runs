def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if item in current_cart:
            current_cart[item]+=1
        else:
            current_cart[item]=1
    return current_cart

def read_notes(notes):
    cart={}
    for item in notes:
        if item in cart:
            cart[item]+=1
        else:
            cart[item]=1
    return cart

def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}

    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment_cart[item] = [quantity, aisle, refrigeration]
    sorted_fulfillment_cart = dict(sorted(fulfillment_cart.items(), reverse=True))

    return sorted_fulfillment_cart

def update_store_inventory(fulfillment_cart, store_inventory):
    for item, details in fulfillment_cart.items():
        if item in store_inventory:
            order_quantity = details[0]
            store_quantity = store_inventory[item][0]
            new_quantity = store_quantity - order_quantity

            if new_quantity > 0:
                store_inventory[item][0] = new_quantity
            else:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory