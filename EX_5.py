#MAP(), FILTER(), and REDUCE()

#MAP()
def cube(a):
    return a*a*a

l = [1,2,3,4,5,6]
newl = []
for item in l:
    newl.append(cube(item))

print(newl)

#using lambda function 
newl = list(map(lambda x:x*x*x,l))
print(newl)

#FILTER()
l = [1,2,3,4,5,6]

def filter_function(l):
    return l>4

newl = list(filter(filter_function,l))
print(newl)

#REDUCE
from functools import reduce

#list of numbers
l = [1,2,3,4,5]

#calculate sum of numbers using reduce function
sum = reduce(lambda x,y:x+y,l)

#print the sum
print(sum)

#using def keyword 
from functools import reduce

def mysum(x,y):
    return x+y

l = [1,2,3,4,5]
sum = reduce(mysum,l)

print(mysum)