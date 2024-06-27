empty_dict = {}
print(empty_dict)

phone_book = {
    "batman": 234,
    "superman": 34,
    "ghost":23
}

print(phone_book)

#The dict() Constructor
empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)

#Accessing Values#
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))

#Adding/Updating Entries 
phone_book["newHero"] = 234
print(phone_book)

#Removing Entries 
#If we want to use the deleted value, the pop() or popitem() methods would work better:
del phone_book["Cersei"]
print(phone_book)

#Length of a Dictionary 
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(len(phone_book))
#Checking Key Existence 
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print("Batman" in phone_book)
print("Godzilla" in phone_book)

#Copying Contents #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}
# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

#Dictionary Comprehension
#However, to iterate the dictionary, we’ll use the dict.items() operation which turns a dictionary into a list of (key, value) tuples.
houses = {1: "swarn", 2: "suraj", 3: "jon", 4: "sam"}
print(houses)
new_house = {n*2 : house + "!" for(n, house) in houses.items()}
print(new_house)