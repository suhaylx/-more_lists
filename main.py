basket = [1,4,6,8,0,634,890,574547]
new_list_is_it_changed = basket.append(100) 
#append helps to add item (object) to the list 

print(basket)
print(new_list_is_it_changed)

basket.extend([1001,12, 11, 11, 34,1222,1201,101])
#extend method is used to add lists to list 
print(basket)

basket.insert(1,-1)
print(basket)
# insert method is used for adding item in to some idex for example here we are adding -1 to the position  1 

basket.remove(100)
print(basket)
#removing 100 from list

basket.pop()
print(basket)
#removing last item from list

basket.pop(1)
print(basket)
#removing from item in the index of 1

basket.reverse()
print(basket)
#removing reverse the list

print(basket.index(1001))
#printing index of item 


print(-1 in basket)
#identifying is -1 in our basket
print(basket.count(11))

#basket.sort()
print(basket)

print(sorted(basket))
#backet.sort() sorts list with modifying the given list     sorted(basket) creates new sorted list from given list

new_list = "-".join(["creates", 'new', 'sorted', 'list', 'from', 'given', 'list'])
print(new_list)
#output will be creates-new-sorted-list-from-given-list