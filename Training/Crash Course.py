#Calling variables in string. Num replace first {} and name replaces second {}
num = 5
name = 'Sec'
print ('Number is {} and name is {}'.format(num,name))
#Assigning specific names
print ('Number is {first} and name is {second}'.format(first=num,second=name))

#Indexing
s = 'hello'
#First character
print (s[0])
#Last character
print (s[-1:])
#Starting from second to last
print (s[1:])
#Starting from first till not including third element
print (s[:3])

#Appending to an existing list
my_list = ['a','b','c',1]
my_list.append('e')
print(my_list)
my_list.append(2)
print(my_list)

#Changing an element of an list
my_list[0] = 'A'
print(my_list)

#Nested lists
nested = ['A','B',['C','D',['E','F',['G']]]]
print(nested[2])
print(nested[2][2])
print(nested[2][2][2])

#Tupple
my_tupple = ('a','b','c')
#Changing an element of a tupple is immutable
my_tupple[0] = 'd'

#Set is a collection of unique elements
print ({1,1,1,1,1,2,2,2,2,3,3,3,3})
#Distinct list elements
print(set([1,1,1,1,1,2,2,2,2,3,3,3,3]))

#If-else
if 1<2:
    print('A')
elif 1 == 2:
    print('C')
else:
    print('B')

#For
seq= [1,2,3,4,5]

for num in seq:
    print (num)

#While
i = 1

while i < 5:
    print ('number is: {}'.format(i))
    i = i +1

#Appending number to a list in a for loop
my_list = []
seq = list(range(1,10))
for i in seq:
    my_list.append(i**2)

print(my_list )

#Creating function and calling in a for loop
def square(num):
    return num**2

my_list = []
seq = list(range(1,10))
for i in seq:
    my_list.append(square(i))
print(my_list )

#For filtering list we need to iterate through the list's elements and filter each of them
for x in my_list:
    if x > 50:        
        print(x)
        
#Tuple Unpacking
x = [(1,2),(3,4),(5,6)]

for item in x:
    print(item)
    
for item1,item2 in x:
    print(item1)
    print(item2)
    
#Exercises
#1
print (7**4)

#2
s = "Hi there Sam!"
mylist =[]
mylist = s.split()

#3
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]

#4
def domainGet(string):
    print(string[string.index('@')+1:])

domainGet('seckindinc@gmail.com')

#5
import re
def wordMatch(string):
    match = re.search('dog',string)
    if match:
        print ("Found")
        print(1)
    else:
        print ("Not Found")
        print(2)
        
wordMatch("My dog is gone")

#6
i = 0
import re
def occourenceCount(string):
    for item in string.split():
        match = re.search('dog',string)
        if match:
            global i
            i += 1
    print("Found",i,"times")

occourenceCount("dog dog dog")

#7
seq = ["soup","dog","salad","cat","great"]
seq_new = []
import re
for item in seq:
    if item[0] == "s":
        seq_new.append(item)

print (seq_new)