import random as r

rand_number=r.randint(1,10) # generate random number including 1 to 10
print(rand_number)
random_floating_point=r.random() # generate a random floating number between 0 and 1.0 not including 1.0
print(random_floating_point)

random_floating_number_5=random_floating_point * 5
print(random_floating_number_5)

"""The code above generates a random floating number between 0 to 5 but not including five, additionally you can 
modify this code to be any floating number ranging from 0 to the number you not including the final number"""