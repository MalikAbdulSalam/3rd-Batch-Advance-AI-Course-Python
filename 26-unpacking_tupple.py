fruits = ("apple", "banana", "cherry")

(a, b, c ) = fruits

print(a)
print(b)
print(c)




# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


print("=" * 40)
fruits = ("apple", "banana", "cherry")

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a,*red) = fruits
print(a)
print(red)





# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)



# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, a,red) = fruits
print(green)
print(tropic)
print(red)
print(a)