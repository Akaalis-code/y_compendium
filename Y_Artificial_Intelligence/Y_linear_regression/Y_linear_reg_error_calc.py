# https://brilliant.org/wiki/linear-regression/
# coding linear regression in above link
# m=1.38 b=0.33
#m=2 b=3

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import time



fig = plt.figure()
ax = plt.axes(projection ='3d')
#m = np.outer(np.linspace(-5, 5, 11), np.ones(11))
m = np.outer(np.linspace(0, 2, 21), np.ones(21))
print(m)
print(" ")
print(" ")
print(" ")
print(" ")
b = m.copy().T
print(b)

def calc_graph (m,b,y_given,x_given):
    # print((x_given*m))
    # print(" ")
    # print(" ")
    # print(" ")
    # print(" ")
    # print(((x_given*m)+b))
    # print(" ")
    # print(" ")
    # print(" ")
    # print(" ")
    # print(((x_given*m)+b-y_given))
    # print(" ")
    # print(" ")
    # print(" ")
    # print(" ")
    d=((x_given*m)+b-y_given)*((x_given*m)+b-y_given)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    #print(d)

    return d

def plot_graph (ax,color_var,m,b,d):
    ax.plot_surface(m, b, d, cmap='viridis',edgecolor=color_var)
    ax.set_xlabel("m")

    ax.set_ylabel("b")

    ax.set_zlabel("d")
 
def d_summed():
    #d_summed_var=np.add(np.add(np.add(np.add(calc_graph(m,b,2,1),calc_graph(m,b,3,2)),calc_graph(m,b,7,4)),calc_graph(m,b,5,5)),calc_graph(m,b,11,7))
    d_summed_var = calc_graph(m,b,2,1) + calc_graph(m,b,3,2) + calc_graph(m,b,7,4) + calc_graph(m,b,5,5) + calc_graph(m,b,11,7)
    print("printing d_summed_var")
    print(d_summed_var)
    return d_summed_var

def ylog():
    pass

if __name__=='__main__':
    # d=calc_graph(m,b,2,1)
    # plot_graph(ax,'red',m,b,d)

    d=calc_graph(m,b,3,2)
    plot_graph(ax,'blue',m,b,d)


    # d=calc_graph(m,b,7,4)
    # plot_graph(ax,'green',m,b,d)

    # d=calc_graph(m,b,5,5)
    # plot_graph(ax,'yellow',m,b,d)

    # d=calc_graph(m,b,11,7)
    # plot_graph(ax,'pink',m,b,d)

    d=d_summed()
    plot_graph(ax,'pink',m,b,d)

    plt.show()


