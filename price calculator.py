# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
price = 0
if size == "S":
  price += 15
  print(f"Cost of the smal prizza is: {price}")
elif size == "M":
  price += 20
  print(f"Cost of the medium prizza is: {price}")
else:
  price += 25
  print(f"Cost of the medium prizza is: {price}")
if add_pepperoni == "Y":
  if size == "S":
    price += 2
  else:
    price += 3
if extra_cheese == "Y":
  price += 1
print(f"Your final bill is $ {price}")
print("Thank you for shopping us")

