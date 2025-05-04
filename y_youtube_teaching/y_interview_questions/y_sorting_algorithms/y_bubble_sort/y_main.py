
import numpy 
import random
from y_plotting import *

var_len = 30

var_axis_X = numpy.linspace(0, var_len, num=var_len)
var_y = [random.randint(0,var_len) for _ in range(0,var_len) ]


sorting_y = var_y

var_bar_colors = ['tab:blue' for _ in range(0,var_len)]
var_traverse_color = ['tab:blue' for _ in range(0,var_len)]



for i in range(0,var_len) :
    if i == (var_len-1) :
        var_bar_colors[(var_len-1)-i] = 'tab:green'
        var_traverse_color[(var_len-1)-i] = 'tab:green'
    
    for j in range(0,(len(var_y)-1)) :
        #if var_traverse_color[j] != 'tab:green':
        var_traverse_color[j] = var_bar_colors[j]
        if j != (len(var_y)-2) :
            var_traverse_color[j+1] = 'tab:red'
        if sorting_y[j]>sorting_y[j+1] :
            temp = sorting_y[j]
            sorting_y[j] = sorting_y[j+1]
            sorting_y[j+1] = temp
        mth_plot(var_axis_X , sorting_y , var_traverse_color , var_bar_colors)
        pplt.pause(.01)

    var_bar_colors[(var_len-1)-i] = 'tab:green'
    var_traverse_color[(var_len-1)-i] = 'tab:green'



pplt.show()