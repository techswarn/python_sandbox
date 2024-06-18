#Append
num_list = [];
num_list.append(1)
num_list.append(2)
num_list.append(3)
num_list.append(1)
print(num_list)

#Insert
num_list.insert(2, 10)
print(num_list)

#POP

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)

#REMOVE delete a perticular value from the list
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Raven"]
print(houses)
houses.remove("Raven")
print(houses)

# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)

#List slicing
num_list = [1,2,3,4,5,6,7,8,9]
print(num_list[0:5])

#Index Search
cities = ["Mangalore", "bangalore", "mysore"]
print(cities.index("Mangalore"))

#IN operator to check if it exists
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

#list sort
num_list = [2,3,1,5,4,6,8,7,0,9]
num_list.sort()
print(num_list)