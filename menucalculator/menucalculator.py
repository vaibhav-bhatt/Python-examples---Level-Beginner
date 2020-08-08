import json

with open("itemprices.json") as json_file:
    menu_card = json.load(json_file)

def calculate_order_total(order):
    global menu_card
    order_list = list(order)
    total = sum([menu_card[item] for item in order_list])
    print(f"Your order total is {total}")

menu = '''
====== MENU for today: =======
      1. "Chicken Strips": 280,
      2. "French Fries": 140,
      3. "Hamburger": 160,
      4. "Hotdog": 120,
      5. "Large Drink": 100,
      6. "Medium Drink": 75,
      7. "Milk Shake": 85,
      8. "Salad": 125,
      9. "Small Drink": 60
'''
def take_orders():
    take = True
    while take:
        print(menu)
        order = input("Please entre your order")
        calculate_order_total(order)
        repeat = input("Do you want to place another order ? Y/N")
        if repeat == 'n' or repeat =='N':
            take = False

if __name__ == "__main__":
    take_orders()