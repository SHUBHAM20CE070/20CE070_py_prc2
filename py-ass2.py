#20CE070_SHUBHAM_PANCHAL
#PRAC-2_list,tuple,set,dictionary

#check whether a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

#merge two dictionary

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

#sum all the items in a dictionary.

my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))

#add a key to a dictionary.

d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

'''Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :dic1={1:10, 2:20}dic2={3:30, 4:40}dic3={5:50,6:60}'''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# create a tuple with different data types.

tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#create a tuple with numbers and print one item.

tuplex = 5, 10, 15, 20, 25
print(tuplex)

tuplex = 5,
print(tuplex)

# add an item in a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

# convert a tuple to a string.

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)

# find the length of a tuple.

tuplex = tuple("shubham")
print(tuplex)

print(len(tuplex))

#

num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 4 from the said set:")
num_set.discard(4)
print(num_set)

#create an intersection, Union, difference of sets.
#union
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])

setc = setc1.union(setc2)
print("Union of above sets:")
print(setc)

#intersection
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])

setz = setx & sety
print("intersection:")
print(setz)

#difference
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
  
print("Difference :", A - B)
  
# symmetric difference
print("Symmetric difference :", A ^ B)

# find maximum and the minimum value in a set.

setn = {5, 10, 3, 15, 2, 20}

print(type(setn))
print("\nMaximum value of the said set:")
print(max(setn))
print("\nMinimum value of the said set:")
print(min(setn))

#find the most common elements and their counts from list, tuple, dictionary.
