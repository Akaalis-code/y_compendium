##########################################################################################################################################
### Objective of this file ==>>> To show how creating one variable from another variable through "=" symbol connects them to each other 
### even in context of changing just one variable automatically affects other
##########################################################################################################################################





### Simple variables with integers

# x = 123
# y = x

# print('Before : ',x,y)
# y = 5
# print('After : ',x,y)




### Simple variables with strings

# x = '123'
# y = x

# print('Before : ',x,y)
# y = '5'
# print('After : ',x,y)




### with list

# x = [1,1,1]
# y = x

# print('Before : ',x,y)
# y[1] = 22
# print('After : ',x,y)







### With dictionaries

x = {'A':1 , 'B':2 , 'C':3}
y = x

print('Before : ',x,y)
y['B'] = 22
print('After : ',x,y)










################################### rough work 

# import random

# lst_1 = [ random.randint(0,1000) for _ in range(0,10) ]
# lst_2 = lst_1

# print(lst_1)
# print(lst_2)






# import random

# lst_1 = [ random.randint(0,1000) for _ in range(0,10) ]
# lst_2 = [ random.randint(0,1000) for _ in range(0,10) ]

# print(lst_1)
# print(lst_2)



