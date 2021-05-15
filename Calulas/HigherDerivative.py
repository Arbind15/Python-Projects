import matplotlib.pyplot as plt
import math
import numpy as np

print("Please enter the f(x):")
eq = str(input())
# input should be in the form of y=f(x)
# power is expressed form math module

print("Please enter the value of x:")
x = float(input())

fig, axs = plt.subplots(3)
step_size = 0.01  # precision

ll = x - 50  # setting lower limit to plot graph
ul = x + 50  # setting upper limit
step = ll
x_axs = []
y_axs = []
while (step <= ul):
    # print("x")
    y = eq.replace('x', str(step))
    y = eval(y)  # this gives sum of given expression
    x_axs.append(step)
    y_axs.append(y)
    step += step_size  # step size

axs[0].plot(x_axs, y_axs, color="green", linewidth=2)
axs[0].set_xlabel("x")
axs[0].set_ylabel("F(x)")
y = eq.replace('x', str(x))
y = eval(y)
axs[0].scatter(x, y, color="r")
# print("y")
step = ll
x_axs = []
y_axs = []
# print(step)
# print(ul)
# finding two nearest point seperated by step_size on curve to find slope
x1 = x - step_size
x2 = x + step_size
y1 = eval(eq.replace('x', str(x1)))
y2 = eval(eq.replace('x', str(x2)))

try:
    slope = (y2 - y1) / (x2 - x1)
except(ZeroDivisionError):
    print("inf")
    slope = 'inf'
print("F'(x) = ", slope)
axs[1].scatter(x, slope, color="r")



x1 = ll
x2 = x1+step_size
while(step<=ul):
    # print(step)
    # print("y")
    y = eq.replace('x', str(step))
    y1 = eval(eq.replace('x', str(x1)))
    y2 = eval(eq.replace('x', str(x2)))
    try:
        slope = (y2 - y1) / (x2 - x1)
        y_axs.append(slope)
    except:
        # print("inf")
        y_axs.append(None)
    x_axs.append(step)

    step += step_size
    x1 = x1 + step_size
    x2 = x2 + step_size



axs[1].plot(x_axs, y_axs, color="green", linewidth=2)
axs[1].set_xlabel("x")
axs[1].set_ylabel("F'(x)")


i=0
yy=[]
for xx in x_axs:
    try:
        slope2=(y_axs[i+1] - y_axs[i]) / (x_axs[i+1] - x_axs[i])
        yy.append(slope2)
        if(round(xx,4)==round(x,4)):
            axs[2].scatter(x, slope2, color="r")
            print("F''(x) = ", slope2)
    except:
        yy.append(None)
        # print("inf ",xx)
    i+=1

axs[2].plot(x_axs, yy, color="green", linewidth=2)
axs[2].set_xlabel("x")
axs[2].set_ylabel("F''(x)")

plt.show()
