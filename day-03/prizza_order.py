print("welcome to python pizza deliveries!")
size = (input("what size pizza do you want? S,M,or L: "))
bill = 0
if size == "s":
   bill = 15
   print("please pay $15")
elif size == "m":
   bill += 20
   print("please pay $20")
elif size == "L":
   bill += 25
   print("please pay $25")
else:
   print("you have write wrong inputs")   

pepperoni = input("do you want pepperoni on your pizza? y or n:")
if pepperoni == "y":
   if size == "s":
      bill += 2
else:
   bill += 3
extra_cheese = input("do you want extra cheese? y, n:")
if extra_cheese == "y":
   bill += 1
print(f"your final bill is: ${bill}.")