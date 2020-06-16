# motorcycle = []
#
# # or
#
# motorcycle = ['honda', 'yamaha']
# motorcycle.append('dukati')
# motorcycle.append('bmw')
# print(motorcycle)
#
# # ['honda', 'yamaha', 'dukati', 'bmw']
# # inserting item at any index
#
# motorcycle.insert(2, 'ktm')
# print(motorcycle)
#
# # ['honda', 'yamaha', 'ktm', 'dukati', 'bmw']
#
# # motorcycle.pop() # removes last item
# # print(motorcycle)
#
# last_item = motorcycle.pop() #pop() also return last removed item
# print(last_item)
#
# removed_item = motorcycle.pop(1) #removed item using pop() at any given index
# print(removed_item)
#
# motorcycle.append('kawaskai')
# motorcycle.append('bmw')
#
# print(motorcycle)
#
#
# del motorcycle[2]
# print('temperory sorted')
# temp_sorted = sorted(motorcycle)
# print(temp_sorted)
# print(motorcycle)
#
# # Permanently sorted
# motorcycle.sort()
# motorcycle.sort(reverse=True) #in reverse
# print(motorcycle)
#
# print(motorcycle.reverse()) #it will reverse the order as it is not alphabetically
#
# # create list of numbers using range() function
# numbers = list(range(1,10))
# print(numbers)
#
# numbers = list(range(1,10, 2)) #'2' is step to increment numbers
# print(numbers)
#
# # squares of all the numbers i the list
# for num in numbers:
#     print(num**2)
#
# #list comprehension
# print('list comprehension')
# square = [num**2 for num in numbers]
# print(square)

for num in range(1, 21):
    print(num)



