#Indexy_listy 0,1,2,3,4
first_list = [1,2,3,4,5]

print(first_list)
print(first_list[3])

# odwracanie listy
print(first_list[::-1])

first_list.append(6)
print(first_list)

first_list[3] = 200
print(first_list)

del first_list[3]
print(first_list)

first_list = [1,'Kasia', 'Kasia',3,4,5,100]
print(first_list)
first_list.remove('Kasia')
print(first_list)