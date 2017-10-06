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

