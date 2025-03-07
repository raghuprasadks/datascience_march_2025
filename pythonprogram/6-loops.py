
'''
# Loops in python
# for loop
lst=[1,2,3,4,5]
for i in lst:
    print(i)
tup=(10,20,30)
for i in tup:
    print(i)
for i in range(0,10):
    print(i)

for i in range(10,22):
    print(i)

# using step
for i in range(1,10,2):
    print(i)


# Print the table of the number given as input
# 1. take user input
# 2. print the table of that number(upto 10)
# enter a number - 5


num=int(input("Enter a number: "))
for i in range(1,11):
    print(num*i)

# 2 x 1 =2
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n, "x",i, "=", n*i)
'''


# while loop

n=1
while n<5:
    print(n)
    n+=1

# print from 5 to 11 using while loop
'''
n=5
while n<12:
    print(n)
'''
# Jumping statements in python

# break
# continue
# pass

# break

for i in range(1,11):
    print(i)
    if i==5:
        break

# continue
for i in range(1,11):
    if i==5:
        continue
    print(i)