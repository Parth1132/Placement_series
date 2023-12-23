tup=(1,2,3,76,132,567,876)             #tuples are ordered collections of data items.
print(type(tup), tup)

#tuples are immutable(meaning they cant be changed after creation)


print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-3]) #incase of negative indexing subtract the index from the 
                     #length of the tuple

print(len(tup))


if 76 in tup:
  print("yes 76 is present in the tuple")

tup2=tup[1:4]
print(tup2)