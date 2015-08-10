# -*- coding: utf-8 -*-
"""
Created on Sun Aug 02 19:50:18 2015

@author: chris
"""

from matplotlib import pyplot as plt
from collections import Counter


#Plot
years=[i for i in range (1950,2020,10)]
gdp=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()


#Histogram 1
movies=["Annie Hall","Ben-Hur","Casablanca","Gandhi","West Side Story"]
ac_awards=[5,11,3,8,10]

#Add 0.1 to the left coordinates
xs=[i+0.1 for i,_ in enumerate(movies)]
print xs

plt.bar(xs,ac_awards)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

plt.xticks([i+0.5 for i,_ in enumerate(movies)],movies)
plt.show()

#Histogram 2
grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]
decile= lambda grade: grade//10*10
histogram=Counter(decile(grade)for grade in grades)

plt.bar([x-4 for x in histogram.keys()],histogram.values(),8)
plt.axis([-5,105,0,5])
plt.xticks([i*10 for i in range(0,11)])
plt.ylabel("# of Students")
plt.xlabel("Decile")
plt.title("Distribution of Exam 1 Grades")
plt.show()

#Histogram 3

mentions=[500,505]
years=[2013,2014]

plt.bar([2012.6,2013.6],mentions,0.8)
plt.axis([2012.5,2014.5,499,506])
plt.xticks(years)
plt.ticklabel_format(useOffset=False)
plt.show()

#Line Charts
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

total_error=[x+y for x,y in zip(variance,bias_squared)]
xs=[i for i,_ in enumerate(variance)]

plt.plot(xs,variance,'g-',label='variance')
plt.plot(xs,bias_squared,'r-.',label='biais^2')
plt.plot(xs,total_error,'b:',label='total error')
plt.title('The Bias-Variance Tradeoff')
plt.xlabel('model complexity')
plt.legend(loc=9)
plt.show()

#Scatterplots
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends,minutes)
for label,friend_count,minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
                 xy=(friend_count,minute_count),
                 xytext=(5,-5),
                textcoords="offset points")
plt.title("Daily Minutes vs. Number of Friends")
plt.show()

