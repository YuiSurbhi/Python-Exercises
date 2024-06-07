#lambda_function 

#1)
answer = lambda a:a**2
cube = lambda x:x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(answer(2))
print(cube(3))
print(avg(2,4,7))

#passing function in a function 
def appl(fx,value):
    return fx(value)

print(appl(cube,6))

#2)
my_function = lambda x: x*5
print(my_function(3))
print(my_function(4))
print(my_function(8))
 
#using def keyword 
def my_function(a):
    return a**2

print(my_function(6))

#using lambda 
my_function = lambda a:a**2
print(my_function(2))