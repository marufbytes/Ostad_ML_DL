student = ["Maruf", "Sadib", "Shohag"]
#student =' ["Maruf", "Sadib", "Shohag"]'  #String
print(student)
print(type(student))


print("\n")
cart=["Rice", "Egg"]
#cart.append(cart)  #Only add to the last
cart.insert(1,"Salt")  #can declare index position
print(cart)

print("\n")
cart2=["Rice", "Egg","Rice","Oil","Onion"]
cart2.pop()
print(cart2)
cart2.remove("Egg")
print(cart2)

print("\n")
cart3=["Rice", "Egg","Rice","Oil","Onion"]
index=0
while index<len(cart3):
    print(f"Index = {index} --- Item: {cart3[index]}")
    index=index+1



#enumarete
print("\n")
for index, item in enumerate(cart3):
    print(f"Index = {index} --- Item: {item}")



#sublist
print("\n")
cart4=["Rice", "Egg","Rice","Oil","Onion"]
print(cart4[1:3])

