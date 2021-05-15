import matplotlib.pyplot as plt
import math

print("Please enter the f(x):")
eq = str(input())
# input should be in the form of y=f(x)
# power is expressed form math module

print("Please enter the value of x:")
x = float(input())

fig = plt.figure()
ax = fig.add_subplot(111)
step_size = 0.01  # precision

y = eq.replace('x', str(x))
y = eval(y)  # this gives sum of given expression

ax.scatter(x, y, color="red")

# finding two nearest point seperated by step_size on curve to find slope
x1 = x - step_size
x2 = x + step_size

y1 = eval(eq.replace('x', str(x1)))
y2 = eval(eq.replace('x', str(x2)))

ax.scatter(x1, y1, color="r")
ax.scatter(x2, y2, color="r")

try:
    slope = (y2 - y1) / (x2 - x1)
except(ZeroDivisionError):
    print("inf")
    slope = 'inf'

# finding more points on tangent line by using two point form
x3 = x - step_size * 2000  # multiplication can vary with step_size
y3 = slope * (x3 - x1) + y1

x4 = x + step_size * 2000
y4 = slope * (x4 - x1) + y1

ax.plot([x3, x1, x2, x4], [y3, y1, y2, y4], color="r", linewidth=1)

ll = x - 50  # setting lower limit to plot graph
ul = x + 50  # setting upper limit

step = ll
x_axs = []
y_axs = []
while (step <= ul):
    y = eq.replace('x', str(step))
    y = eval(y)  # this gives sum of given expression
    x_axs.append(step)
    y_axs.append(y)
    step += step_size  # step size

ax.plot(x_axs, y_axs, color="green", linewidth=2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
print("Slope= ", slope, " Ans.")