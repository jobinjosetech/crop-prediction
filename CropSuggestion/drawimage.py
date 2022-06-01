
# importing the required module
import matplotlib.pyplot as plt
from database import *
crops=[]
yields=[]
q="select * from cropyield where place='%s' and year='%s'" %("NICOBARS","2000")
res=select(q)
if res:
	for row in res:
		crops.append(row['crop'])
		yields.append(row['output'])
 
	print(crops)
	print(yields)
	 
	# plotting the points
	plt.plot(crops, yields)
	 
	# naming the x axis
	plt.xlabel('x - axis')
	# naming the y axis
	plt.ylabel('y - axis')
	 
	# giving a title to my graph
	plt.title('My first graph!')
	 
	# function to show the plot
	plt.show()