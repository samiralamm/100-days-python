import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','2','#','$','%','&','*','+',]
print("welcome to the password generator!")
nr_letters = int(input("how many letters would you like in your password: "))
nr_symbols = int(input(f"how many symbols would you like? "))
nr_numbers = int(input(f"how many number would you like?\n"))
# # easy level
# password = ""
# # range(1,101)
# # nr_letter = 4 
# for char in range(1, nr_letters ):
#     # 1-4
#     random_char = random.choice(letter)
#     password += random.choice(letter)
#     # print(random_char)
#     # password += random_char
#     # print(password)
# for char in range(1, nr_letters + 1):
#     password += random.choice(symbols)   

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

# hard level
password_list = []
# range(1,101)
# nr_letter = 4 
for char in range(1, nr_letters ):
    # 1-4
    random_char = random.choice(letter)
    password_list += random.choice(letter)
    # print(random_char)
    # password += random_char
    # print(password)
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(symbols))   

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is: {password}")


          



          