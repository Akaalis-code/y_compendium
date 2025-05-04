import math
import numpy 
import scipy.integrate as integrate
from scipy import signal #for sawtooth wave

import matplotlib.pyplot as pplt

import y_input_graph

#print(pplt.style.available)
#pplt.style.use('dark_background')
pplt.style.use('fivethirtyeight')

var_fig = pplt.figure()
var_figMgr = pplt.get_current_fig_manager()
var_figMgr.full_screen_toggle()

gs = var_fig.add_gridspec(2,3)
Axes1 = var_fig.add_subplot(gs[0, :])
Axes2 = var_fig.add_subplot(gs[1, 0])
Axes4 = var_fig.add_subplot(gs[1, 1])
Axes3 = var_fig.add_subplot(gs[1, 2])


Axes2.set_xticklabels([])

Axes3.set_xticklabels([])

Axes4.set_xticklabels([])
Axes4.set_yticklabels([])


var_axis_X = numpy.linspace(0, 2 * numpy.pi , num=100)
var_n = 100 # number of waves used for construction

var_a0 = 0 # a0 value
var_lst_an = ['NA'] # list of Cosine weightages
var_lst_bn = ['NA'] # list of Sine weightages





def mthd_get_coef(para_the_func , para_n ,para_an_or_bn):
    # integrate.quad  is giving tuple as output , in which zero th index contains integration awnser , tuple[1] contains error
    if para_n == 0 and para_an_or_bn == 'an':
        a0 = (0.318) * ((integrate.quad(lambda x:para_the_func(x) , 0, (2 * numpy.pi)))[0])
        return a0
    if para_n != 0 and para_an_or_bn == 'an':    
        an = (0.318) * ((integrate.quad((lambda x:para_the_func(x) * numpy.cos(para_n * x)) , 0 , (2 * numpy.pi)))[0])
        return an
    if para_n != 0 and para_an_or_bn == 'bn':    
        bn = (0.318) * ((integrate.quad((lambda x:para_the_func(x) * numpy.sin(para_n * x)) , 0 , (2 * numpy.pi)))[0])
        return bn
    return 'NA'


var_lst_f_of_X = []
def mthd_output(para_n , para_a0 , para_lst_an , para_lst_bn , para_axis_X):

    for cntr in range(0 , len(para_lst_an)) :
        if cntr == 0 :
            f_of_x = (para_a0)*(1/2) 
        else :
            #print('f_of_x in an : ',f_of_x)
            f_of_x = f_of_x + para_lst_an[cntr] * (numpy.cos( (cntr) * (para_axis_X) ))
            f_of_x = f_of_x + para_lst_bn[cntr] * (numpy.sin( (cntr) * (para_axis_X) ))
        var_lst_f_of_X.append(f_of_x)
    return f_of_x






def mth_plot_graph (para_axis_x ,para_main_func, para_generated_func , para_cntr):
    Axes1.cla()
    #Axes1.set_ylim(0, 12) 
    #Axes1.set_title("FOURIER REGRESSION")
    #Axes1.set_xlabel("TIME")
    Axes1.set_ylabel("STOCK PRICE SAMPLE DATA")
    Axes1.scatter(para_axis_x,para_main_func ,color='red' )
    Axes1.plot(para_axis_x,para_generated_func )
    #Axes1.legend(['Input sample data like stock price', 'Fourier regression'] , loc='upper left')
    #Axes1.text(3.16,1,'Fourier series output')
    #Axes1.text(3.16,0.5,' a0 + sigma({an * COS(n*x)+bn * SIN(n*x)} , range-> 1 , Infinity)' , fontsize =  'small')
    #mth_sin_and_cosine_plot(var_a0 , var_lst_an , var_lst_bn , para_cntr)
    if para_cntr == 0 :
        Axes2.plot(para_axis_x , var_a0)
    else :
        Axes2.plot(para_axis_x , var_lst_an[para_cntr] * numpy.cos( para_cntr * para_axis_x))
        Axes2.text(1,-1.25,'an * COS(n*x)')

        Axes3.plot(para_axis_x , var_lst_bn[para_cntr] * numpy.sin( para_cntr * para_axis_x))
        Axes3.text(1,-0.75,'bn * SIN(n*x)')

        Axes4.cla()
        Axes4.set_xticklabels([])
        Axes4.set_yticklabels([])
        Axes4.text(0,0.8,'a0 = {0}'.format(var_a0))
        def mthd_my_rounding_up(para_val) :
            if round(para_val , 5) == 0 :
                return 0
            else :
                return round(para_val , 5)
        Axes4.text(0,0.6,'an * COS(n*x) = {0} * COS({1}*x)'.format(mthd_my_rounding_up(var_lst_an[para_cntr]) , para_cntr) , fontsize =  'small' )
        Axes4.text(0,0.4,'bn * SIN(n*x) = {0} * SIN({1}*x)'.format(mthd_my_rounding_up(var_lst_bn[para_cntr]) , para_cntr) , fontsize =  'small' )




# def mthd_input_func(para_x):
#     return signal.sawtooth((2 * numpy.pi * para_x)/3.14)

def mthd_input_func(para_x):
    return 5/(1+(math.e)**(-para_x+3.14))


var_the_func = y_input_graph.mth_input_func



for i in range (0,var_n) :
    if i == 0 :
        var_a0 = mthd_get_coef(var_the_func , i , 'an')
    else :
        var_lst_an.append(mthd_get_coef(var_the_func , i , 'an'))
        var_lst_bn.append(mthd_get_coef(var_the_func , i , 'bn'))

for i in range (0,var_n):
    if i == 0 :
        if abs(var_a0) < 0.05 :
            var_a0 = 0
    else :
        if abs(var_lst_an[i]) < 0.00001:
            var_lst_an[i] = 0
        if abs(var_lst_bn[i]) < 0.00001:
            var_lst_bn[i] = 0

print('var_a0 :' , var_a0)
print('var_lst_an :' , var_lst_an)
print('var_lst_bn :' , var_lst_bn)
var_f_of_x = mthd_output(var_n , var_a0 , var_lst_an , var_lst_bn , var_axis_X)




array=numpy.array
for i in range(1,len(var_lst_f_of_X)) :
    #mth_plot_graph (var_axis_X , var_the_func(var_axis_X) , var_lst_f_of_X[i] , i)
    mth_plot_graph (var_axis_X , y_input_graph.var_data_stock_price , var_lst_f_of_X[i] , i)
    pplt.pause(.01)

pplt.show()