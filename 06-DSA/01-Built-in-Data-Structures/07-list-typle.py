my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
my_tuple = tuple(my_list)
print(my_list)

#Alternative
my_new_tuple = (my_list[0], my_list[len(my_list) - 1], len(my_list))
print(my_new_tuple)