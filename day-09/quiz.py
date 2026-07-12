# Which line of code will change the starting_dictionary to the final_dictionary?

def dictionary_add():
    starting_dictionary = {
    "a": 9,
    "b": 8,
}

    final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
# answer
    starting_dictionary["c"] = 7
    final_dictionary = starting_dictionary
    print(starting_dictionary)
    print(final_dictionary)


# # Which line of code will produce an error?
def error_debug():
    dict = {"a": 1,"b": 2,"c": 3,}

    dict["c"] = [1,2,3]

    for key in dict: 
        dict[key] += 1

    dict[1] = 4


# # Which line of code will print "Steak"?

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order["main"] [2] [0])
error_debug()
dictionary_add()
