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
print ([x for x in my_list if x > 50])