from math import *
from numpy import *
from matplotlib import *
from pylab import *


x_vals = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
y_vals = [0,0,0,0,0,0,0,0,0,15,0,0,15,0,0,30,0]

headroom = max(y_vals)+5

plot(x_vals, y_vals, marker='o', linestyle='-', color='r')
ylabel('Time Excercising (minutes)')
xlabel('Day')
title('Minutes Spent Excercising-ABAB Design')
axvline(x=5.5)
axvline(x=10.5)
axvline(x=12.5)
axis([1,18,0,headroom])
show()

baseline_x = x_vals[0:5]
baseline_y = y_vals[0:5]
plot(baseline_x, baseline_y, marker='o', linestyle='-', color='r')
ylabel('Time Excercising (minutes)')
xlabel('Day')
title('Minutes Spent Excercising-Baseline')
axis([1,5,0,headroom])
show()

intervention_one_x = x_vals[0:10]
intervention_one_y = y_vals[0:10]
plot(intervention_one_x, intervention_one_y, marker='o', linestyle='-', color='r')
ylabel('Time Excercising (minutes)')
xlabel('Day')
title('Minutes Spent Excercising-First Intervention')
axis([1,10,0,headroom])
show()