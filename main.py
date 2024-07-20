import requirements

def choice():
  coffee = input("What would you like? (espresso/latte/cappuccino): ")
  return coffee

ison = True

while(ison):
  userInput = choice()

  if userInput == "report": 
    print(f'''WATER = {requirements.resources["water"]}ml
MILK = {requirements.resources["milk"]}ml
COFFEE = {requirements.resources["coffee"]}ml
PROFIT = ${requirements.resources["profit"]}ml ''')

  elif userInput == "espresso" or "latte" or "cappuccino":
    if  requirements.resources["water"] < requirements.MENU[userInput]["ingredients"]['water'] or requirements.resources["coffee"] < requirements.MENU[userInput]["ingredients"]['coffee'] or requirements.resources["milk"] < requirements.MENU[userInput]["ingredients"]['milk']:
      print("Insufficient Resources !!!😵😵😵")
      ison = False
    else:
      print("Please insert coins.")
      quarters = int(input("How many quarters: "))
      dimes = int(input("How many dimes: "))
      nickles = int(input("How many nickles: "))
      pennies = int(input("How manu Pennies: "))

      requiredMoney = requirements.MENU[userInput]["cost"]
      inputMoney = pennies*1/100 + dimes*10/100 + nickles*5/100 + quarters*25/100
      
      if requiredMoney > inputMoney:
        print(f'''Insufficient amount given
        ${inputMoney}, Here's you Refund.''')
      else:
        print(f"Here is ${inputMoney - requiredMoney} in change.")
        print(f"Here is your {userInput} ☕ Enjoy!")
        requirements.resources["profit"] += requiredMoney

      requirements.resources["water"] -= requirements.MENU[userInput]["ingredients"]['water']
      requirements.resources["coffee"] -= requirements.MENU[userInput]["ingredients"]['coffee']
      if userInput == "latte" or "cappuccino":
        requirements.resources["milk"] -= requirements.MENU[userInput]["ingredients"]['milk']

