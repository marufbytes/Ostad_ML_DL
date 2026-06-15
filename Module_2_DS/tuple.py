import sys

co_ordinate = (5,10,15)
print(co_ordinate)
print(co_ordinate[0])
print(co_ordinate[1])
print(co_ordinate[2])
print(co_ordinate[-2])
print(type(co_ordinate))
print("\n")


#conversion
color_list=["red","green","blue"]
print(type(color_list))
print(color_list)
color_touple=tuple(color_list)
print(type(color_touple))
print(color_touple)
print("\n")


#module
my_list=[1,2,3,4,5]
my_touple=(1,2,3,4,5)

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_touple))