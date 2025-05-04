import numpy
import matplotlib.pyplot as pplt
import scipy.integrate as integrate

var_data_time = numpy.linspace(0, (2 * numpy.pi), num=100)
#numpy.random.randint(0, high=10, size=100)
var_data_stock_price = numpy.array([6, 6, 0, 6, 8, 6, 5, 2, 1, 9, 2, 2, 3, 5, 8, 8, 4, 8, 0, 8, 3, 7, 8, 1, 8, 7, 0, 1, 8, 4, 7, 8, 1, 8, 2, 5, 1, 2, 1, 8, 2, 3, 4, 4, 4, 4, 0, 2, 8, 7, 0, 7, 3, 5, 6, 3, 5, 3, 3, 9, 2, 1, 0, 0, 4, 6, 9, 1, 6, 2, 9, 3, 1, 8, 9, 9, 7, 2, 3, 9, 4, 5, 0, 9, 2, 5, 6, 0, 8, 3, 4, 9, 3, 5, 7, 9, 5, 8, 1, 7])
# print(var_data_time)
# print(var_data_stock_price)
def mth_input_func(para_x):
    for cnt in range(0,len(var_data_time)):
        
        if var_data_time[cnt] <= para_x < var_data_time[cnt+1]:
            i=cnt
            j=cnt+1
            return (var_data_stock_price[j] - var_data_stock_price[i])/(var_data_time[j] - var_data_time[i])*(para_x - var_data_time[i])+(var_data_stock_price[i])

# mth_input_func(var_data_time)
# pplt.scatter(var_data_time , var_data_stock_price , color='red')
#print((integrate.quad((lambda x:mth_input_func(x) * numpy.cos(3*x)) , 0 , (2 * numpy.pi)))[0])
# print(mth_input_func(0))
# print(mth_input_func(0.1))
# print(mth_input_func(0.2))
# print(mth_input_func(0.6))

# print(mth_input_func(1))
# print(mth_input_func(2))
# print(mth_input_func(3))

# pplt.plot(mth_input_func , var_data_stock_price)
# pplt.show()