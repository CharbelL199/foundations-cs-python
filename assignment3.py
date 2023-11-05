#system POS

items = [["tomato", 1], ["potato", 2], ["chocolate", 3], ["soap", 5]]

AddedItems = []
discount_code = "1234"

def addItem():
  itemName = input("Enter the item you would like to add: ,Tomato, Potato, Chocolate, Soap:")
  for item in items:
      if itemName.lower() == item[0].lower():
          itemQty =input("Enter the quantity:")
          if itemQty.isdigit():
              itemQty = int(itemQty)
              AddedItems.append([item[0],itemQty])
              print("Item added!")
              return
          else:
              print("Invalid quantity. Please enter a valid number:")
              return
  print("Item Not Found")

    
def checkTotal():
   total = 0
   for item in AddedItems:
       itemName, itemQty = item
       for i in items:
           if i[0] == itemName:
               total += i[1] * itemQty
   return total
        
def applyCoupon():
    code = input("Enter your discount code: ")
    if code == discount_code:
        return 0.10  # 10% discount
    else:
        print("Invalid discount code. No discount applied.")
        return 0
        
# def checkout():


def newOrder():
  choice = -1
  while choice != 4:
    print("Enter")
    print("1. To add an item")
    print("2. To check total")
    print("3. To add a coupon")
    print("4. To checkout")
    choice = int(input())
    if choice == 1:
      addItem()
    elif choice == 2:
      total = checkTotal()
      print("Total",total,"$")
    elif choice == 3:
      # addCoupon()
      coupon_discount = applyCoupon()
      print("Coupon applied")
    elif choice == 4:
      total_order = checkTotal()
      total_discounted = total_order * (1 - coupon_discount)
      print("Total of order without coupon:", total_order)
      print(f"Total with a {coupon_discount * 100}% discount: {total_discounted}$")
      print("Thank you for your purchase!")
      AddedItems.clear()
      return
      print("Checkout")


#Menus
def MainMenu():
  choice = -99
  while choice != 2:
    print("Enter")
    print("1 to start a new order")
    print("2 to close the program")
    choice = int(input())
    if choice == 1:
      print("new order")
      newOrder()
    elif choice == 2:
      print("Bye Bye")
    else:
      print("Invalid input")


MainMenu()
# newOrder()
