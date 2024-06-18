jon_snow = ["Jon snow", "Winterfell", 23]
print(jon_snow)

print(len(jon_snow))

#Using range()

num_seq = range(0,10)
num_list = list(num_seq)
print(num_list)

num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
print(list(num_seq))

#List-Ception!

world_cup_winners = [[2006, "india"], [2045, "US"], [2354, "Fuji"]]
print(world_cup_winners)

#Sequential Indexing
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0]) 

#Merging Lists#

list1 = [1,2,3,4]
list2 = [2,4,5,6]

listnew = list1 + list2
print(listnew)

#extend can also be used.
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)