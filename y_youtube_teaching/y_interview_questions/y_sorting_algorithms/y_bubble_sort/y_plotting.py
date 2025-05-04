
#import matplotlib 
#matplotlib.use('tkAgg') 

import matplotlib.pyplot as pplt

pplt.style.use('fivethirtyeight')

var_fig = pplt.figure()
var_figMgr = pplt.get_current_fig_manager()
var_figMgr.full_screen_toggle()

gs = var_fig.add_gridspec(1,1)
Axes1 = var_fig.add_subplot(gs[0, :])


def mth_plot(para_x , para_y , para_bar_colors , var_rough= 'hi'):
    Axes1.cla()
    Axes1.bar(para_x, para_y, color=para_bar_colors)
    #Axes1.text(0,19,para_bar_colors,fontsize =  8)
    #Axes1.text(0,20,var_rough,fontsize =  8)



#pplt.show()        Use this is calling file to start the plot viewing thread