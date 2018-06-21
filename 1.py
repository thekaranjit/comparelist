'''
Generate a random and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''

import random

lengthlist = int(input("Please input a Length of list ( Only in numbers) : "))
rangelist = int(input("Please input a Range of list ( Only in numbers) : "))

lista = random.sample(range(rangelist), lengthlist)
print('\n')

listb = random.sample(range(rangelist), lengthlist)
print('\n')
reslist = []

for element in lista:
    if element in listb:
        reslist.append(element)
        
    else:
        ("There are no Duplicates in the generated list")

print("Generated Random List 1 : ", lista)
print('\n')
print("Generated Random List 2 : ", listb)
print('\n')
print("The New List with Duplicate from List 1 & List 2 is  : ", reslist)










