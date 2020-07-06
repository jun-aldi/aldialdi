#A typical car can hold 4 passengers and 1 driver, 
#overall allowing 5 people to travel around. Given n number of people, 
#return how many cars are needed to seat everyone comfortably.
#ceil function untuk meningkatkan ke atas

from math import ceil
def cars_needed(x):
    car = ceil(x/5)
    return car

x=int(input("jumlah orang :"))
print("jumlah mobil : ",cars_needed(x))