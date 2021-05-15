import matplotlib.pyplot as plt
import math
print("Please enter the f(x):")
eq=str(input())
#input should be in the form of y=f(x)
#power is denoted by ^
print("Please enter the lower limit:")
ll=float(input())
print("Please enter the upper limit:")
ul=float(input())
step_size=0.00001  #precision
step=ll
x_axs=[]
y_axs=[]
Sum=0
while(step<=ul):

    y = eq.replace('x', str(step))
    y = eval(y) #this gives sum of given expression
    Sum=(Sum+(y*step_size))
    x_axs.append(step)
    y_axs.append(y)
    step+=step_size #step size

# print(x_axs,y_axs)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x_axs,y_axs,color="green",linewidth=2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
print("Area= "+str(Sum)+"Sq. Units")