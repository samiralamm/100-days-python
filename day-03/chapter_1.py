print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
# if height = 120:
# if height ==120:
if height >= 120:
# if height <= 120:
      print("you can ride the rollercoaster")
      age = int(input("what is your age? "))
      if age <= 12:
        bill = 5
        print("please pay $5.")
      elif age <= 18:
        bill = 7
        print("please pay $7")
      else:
           bill = 12
           print("please pay $12.")  
           want_photo = input("do you want to have photo taken ? type y for yes and n for no.")
           if want_photo == "y":
        #   add $3 bill
            bill += 3
            # bill = bill + 3
           print(f"your final bill is ${bill}")

else:
      print("sorry you have to grow taller before you can ride.")
      