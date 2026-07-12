# shorter version solution
def calculate_love_score(name1, name2 ):
    names = (name1 + name2).lower()

    true_score = 0 
    for letter in "true":
        true_score += names.count(letter)

    love_score = 0
    for letter in "love":
        love_score += names.count(letter)
    
    print(f"{true_score}{love_score}")

calculate_love_score("Tarannum Bano","Saghir Alam")

#   2nd method long detail simple  version how to calculate_love_score

# def calculate_love_score(name1, name2):
#     combined_names = (name1 + name2).lower()

#     true_score = (
#         combined_names.count("t") +
#         combined_names.count("r") +
#         combined_names.count("u") +
#         combined_names.count("e")
#     )

#     love_score = (
#         combined_names.count("l") +
#         combined_names.count("o") +
#         combined_names.count("v") +
#         combined_names.count("e")
#     )

#     score = int(str(true_score) + str(love_score))
#     print(score)


calculate_love_score("SAGHIR ALAM", " SANA TARANNUM")

# 3rd method  udemy version of solution

# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
    
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
    
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
    
# calculate_love_score("tarannum bano", "saghir alam")


