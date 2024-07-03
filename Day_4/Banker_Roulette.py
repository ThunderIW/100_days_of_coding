import random
names="Angela, Ben, Jenny, Michael, Chloe"
names_list=names.split(',')
print(names_list)
random_banker=random.randint(0,len(names_list)-1)
print(f"{names_list[random_banker]} is going to buy the meal today")

